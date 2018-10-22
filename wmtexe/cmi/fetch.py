#! /usr/bin/env python
from __future__ import print_function

import os
import subprocess
import re
import types

import yaml
from distutils.dir_util import mkpath

from .utils import cd, check_output, system, read_first_of
from .git import git_repo_name, git_clone_or_update, git_repo_sha
from .project import empty_bmi_project, add_bmi_component
from . import api


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


def load_bmi_api(dir='.'):
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


def load_build_script(dir='.'):
    with cd(dir):
        with open(os.path.join('.bmi', 'api.yaml'), 'r') as fp:
            api = yaml.load(fp)
    return api['build']


def build_api(build):
    if isinstance(build, dict) and 'brew' in build:
        brew = build['brew']
        opts = brew.get('options', [])
        if isinstance(opts, str):
            opts = [opts]
        system(['brew', 'install', brew['formula']] + opts)
    else:
        raise RuntimeError('only building with homebrew is supported')


def cache_dir_from_repo(repo, branch='master'):
    return os.path.join('cache', git_repo_name(repo) +
                                 '-%s' % git_repo_sha(repo, branch=branch))


def component_name_from_repo(repo, name=None):
    name = name or re.sub('-', '', os.path.basename(repo).title())

    return '.'.join(['model', name])


def parse_repo_line(line):
    if ',' in line:
        repo, branch = line.split(',')
    else:
        repo, branch = line, 'master'

    return repo.strip(), branch.strip()

def main():
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument('repo', type=str, nargs='+',
                        help='GitHub repository for BMI implementation')

    args = parser.parse_args()

    proj = empty_bmi_project()
    for repo in args.repo:
        repo, branch = parse_repo_line(repo)

        cache_dir = cache_dir_from_repo(repo, branch=branch)

        git_clone_or_update(repo, dir=cache_dir, branch=branch)

        with cd(cache_dir) as _:
            bmi = api.load()
            api.execute_api_build()

        bmi['name'] = component_name_from_repo(repo, bmi.get('name', None))

        add_bmi_component(proj, bmi)

    print(yaml.dump(proj, default_flow_style=False))


if __name__ == '__main__':
    main()
