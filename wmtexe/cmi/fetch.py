#! /usr/bin/env python
import os
import subprocess
import re
import types

import yaml
from distutils.dir_util import mkpath

from .utils import cd, check_output, system, read_first_of
from .git import git_repo_name, git_clone_or_update, git_repo_sha


def load_bmi_info(dir):
    with cd(dir):
        with open(os.path.join('.bmi', 'info.yaml'), 'r') as fp:
            info = yaml.load(fp)

        if 'summary' not in info:
            info['summary'] = read_first_of(['README.md', 'README',
                                           'README.txt']).strip()

        if 'license' not in info:
            info['license'] = read_first_of(['LICENSE', 'LICENSE.txt']).strip()

    return info


def load_bmi_api(dir):
    with cd(dir):
        with open(os.path.join('.bmi', 'api.yaml'), 'r') as fp:
            api = yaml.load(fp)
    api.pop('build')

    if isinstance(api['cflags'], dict) and 'pkgconfig' in api['cflags']:
        api['cflags'] = check_output(['pkg-config', '--cflags',
                                      api['cflags']['pkgconfig']]).strip()

    if isinstance(api['libs'], dict) and 'pkgconfig' in api['libs']:
        api['libs'] = check_output(['pkg-config', '--libs',
                                    api['libs']['pkgconfig']]).strip()

    return api


def load_build_script(dir):
    with cd(dir):
        with open(os.path.join('.bmi', 'api.yaml'), 'r') as fp:
            api = yaml.load(fp)
    return api['build']


def build_api(build):
    try:
        brew = build['brew']
    except KeyError:
        raise RuntimeError('only building with homebrew is supported')
    else:
        opts = brew.get('options', [])
        if isinstance(opts, types.StringTypes):
            opts = [opts]
        system(['brew', 'install', brew['formula']] + opts)


_THIS_DIR = os.path.dirname(__file__)


def main():
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument('repo', type=str, nargs='+',
                        help='GitHub repository for BMI implementation')

    args = parser.parse_args()

    proj = {
        'name': 'csdms',
        'language': 'c',
        'interfaces': [{
            'name': 'csdms.core.Bmi',
            'sidl': os.path.join(_THIS_DIR, 'data', 'csdms.core.Bmi.sidl')
        }],
        'bmi': []
    }
    for repo in args.repo:
        cache_dir = os.path.join('cache', git_repo_name(repo) +
                                 '-%s' % git_repo_sha(repo))

        git_clone_or_update(repo, dir=cache_dir)
        build_api(load_build_script(cache_dir))

        api = load_bmi_api(cache_dir)
        if 'name' not in api:
            api['name'] = re.sub('-', '', os.path.basename(repo).title())

        proj['bmi'].append(api)

    print yaml.dump(proj, default_flow_style=False)


if __name__ == '__main__':
    main()
