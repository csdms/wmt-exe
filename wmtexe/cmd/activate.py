from __future__ import print_function
import sys
import os

from ..env import WmtEnvironment


_ACTIVATE_SCRIPT = """
# This file must be used with "source wmt-activate" *from bash*
# you cannot run it directly

if [ -n "$BASH" -o -n "$ZSH_VERSION" ] ; then
    hash -r
fi

{ENVIRONMENT}
""".strip()

_PATH_NAMES = ['PATH', 'LD_LIBRARY_PATH', 'PYTHONPATH', 'LD_RUN_PATH',
               'CLASSPATH', 'SIDL_DLL_PATH']
_VAR_NAMES = ['TAIL', 'CURL', 'BASH']


def prepend_path(var, path, out=None):
    path = os.path.normpath(path)

    env = out or os.environ
    try:
        paths = env[var].split(os.pathsep)
    except KeyError:
        paths = []
    else:
        paths = [os.path.normpath(p) for p in paths]

    try:
        paths.remove(path)
    except ValueError:
        pass

    env[var] = os.pathsep.join([path] + paths)


def prepend_paths(var, paths, out=None):
    for path in paths.split(os.pathsep)[::-1]:
        prepend_path(var, path)


def saved_var_name(name):
    return '_WMT_OLD_%s' % name


def save_vars(names):
    saved = {}
    for name in names:
        if name in os.environ:
            saved[saved_var_name(name)] = os.environ[name]

    return saved


def restore_vars(names):
    env = {}
    for name in names:
        saved_name = saved_var_name(name)
        if saved_name in os.environ:
            env[name] = os.environ.pop(saved_name)
        else:
            env[name] = None
        env[saved_name] = None
    return env


def environ_update(env):
    updated = save_vars(_PATH_NAMES + _VAR_NAMES)

    for name in _PATH_NAMES:
        prepend_paths(name, env[name])

    for name in _VAR_NAMES:
        os.environ[name] = env[name]

    for name in _PATH_NAMES + _VAR_NAMES:
        updated[name] = os.environ[name]

    return updated


def environ_as_bash_commands(env):
    commands = []
    names = env.keys()
    names.sort()
    for name in names:
        if env[name] is None:
            commands.append('unset %s;' % name)
        else:
            commands.append('export %s="%s";' % (name, env[name]))
    return commands


def activate(path, extra_bases=[]):
    env = WmtEnvironment.from_config(path)

    env = environ_update(env)
    for base in extra_bases:
        prepend_path('PATH', os.path.join(base, 'bin'), out=env)
        prepend_path('LD_LIBRARY_PATH', os.path.join(base, 'lib'), out=env)
        prepend_path('PYTHONPATH',
                     os.path.join(base, 'lib', 'python2.7', 'site-packages'),
                     out=env)

    print(os.linesep.join(environ_as_bash_commands(env)))


def deactivate():
    env = restore_vars(_PATH_NAMES + _VAR_NAMES)

    print(os.linesep.join(environ_as_bash_commands(env)))



def deactivate_main():
    import argparse

    parser = argparse.ArgumentParser(
        description='Deactivate a WMT environment')
    args = parser.parse_args()

    deactivate()


def activate_main():
    import argparse

    parser = argparse.ArgumentParser(
        description='Activate a WMT environment')

    parser.add_argument('file', nargs='?', type=str,
                        default=None, help='WMT config file')
    parser.add_argument('--prepend-base', action='append', default=[],
                        help='Extra bases to include in environment')
    args = parser.parse_args()

    activate(args.file, extra_bases=args.prepend_base)
