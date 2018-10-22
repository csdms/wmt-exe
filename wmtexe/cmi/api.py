#! /usr/bin/env python
from __future__ import print_function

import os
import types
import yaml

from .utils import cd, check_output, system
from .git import git_repo_name, git_clone_or_update, git_repo_sha


_REQUIRED_KEYS = set(['language', 'build', 'includes', 'cflags', 'libs',
                      'grids'])
_OPTIONAL_KEYS = set(['name', 'type', 'prefix'])
_VALID_KEYS = _REQUIRED_KEYS | _OPTIONAL_KEYS


def is_valid_api(api):
    if not isinstance(api, dict):
        print('not a dict')
        return False

    found_keys = set(api.keys())

    if not found_keys.issuperset(_REQUIRED_KEYS):
        return False

    if not found_keys.issubset(_VALID_KEYS):
        print('unknown key')
        return False

    return True


def is_valid_api_or_raise(api):
    if not is_valid_api(api):
        raise RuntimeError('invalid api yaml')


def generate_compile_opts(flags, opt):
    assert(opt in ['--cflags', '--libs'])

    if isinstance(flags, types.StringTypes):
        return flags

    try:
        return check_output(['pkg-config', opt,
                             flags['pkgconfig']]).strip()
    except KeyError:
        raise TypeError('bad type for flags')


def load(dir='.'):
    with cd(dir):
        with open(os.path.join('.bmi', 'api.yaml'), 'r') as fp:
            api = yaml.load(fp)

    is_valid_api_or_raise(api)

    api.pop('build')

    api['cflags'] = generate_compile_opts(api['cflags'], '--cflags')
    api['libs'] = generate_compile_opts(api['libs'], '--libs')

    return api


def load_build_script(dir='.'):
    with cd(dir):
        with open(os.path.join('.bmi', 'api.yaml'), 'r') as fp:
            api = yaml.load(fp)

    is_valid_api_or_raise(api)

    if isinstance(api['build'], dict) and 'brew' in api['build']:
        return api['build']
    else:
        raise RuntimeError('only building with homebrew is supported')


def execute_build(build):
    brew = build['brew']
    opts = brew.get('options', [])

    if isinstance(opts, types.StringTypes):
        opts = [opts]

    system(['brew', 'install', brew['formula']] + opts)


def execute_api_build(dir='.'):
    build = load_build_script(dir=dir)
    execute_build(build)
