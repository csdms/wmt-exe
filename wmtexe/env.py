from os import path, pathsep
import subprocess


def find_babel_libs():
    try:
        return subprocess.check_output(['cca-spec-babel-config',
                                        '--var', 'CCASPEC_BABEL_LIBS']).strip()
    except (OSError, subprocess.CalledProcessError):
        return None


def python_version(python):
    version = subprocess.check_output(
        [python, '-c', 'import sys; print(sys.version[:3])']).strip()
    return 'python%s' % version


def env_from_config_path(path_to_cfg):
    import ConfigParser

    config = ConfigParser.RawConfigParser()
    config.read(path_to_cfg)

    python_prefix = config.get('wmt', 'python_prefix')
    cca_prefix = config.get('wmt', 'cca_prefix')
    wmt_prefix = config.get('wmt', 'wmt_prefix')
    components_prefix = config.get('wmt', 'components_prefix')

    ver = python_version(path.join(python_prefix, 'bin', 'python'))

    environ = {
        'CURL': config.get('wmt', 'curl'),
        'TAIL': config.get('wmt', 'tail'),
        'BASH': config.get('wmt', 'bash'),
        'PYTHONPATH': pathsep.join([
            path.join(python_prefix, 'lib', ver, 'site-packages'),
            path.join(python_prefix, 'lib', ver),
            path.join(components_prefix, 'lib', ver, 'site-packages'),
            path.join(cca_prefix, 'lib', ver, 'site-packages'),
            path.join(find_babel_libs(), ver, 'site-packages'),
        ]),
        'LD_LIBRARY_PATH': pathsep.join([
            path.join(python_prefix, 'lib'),
            path.join(components_prefix, 'lib'),
            path.join(wmt_prefix, 'lib'),
            path.join(cca_prefix, 'lib'),
        ]),
        'PATH': pathsep.join([
            path.join(python_prefix, 'bin'),
            '/usr/local/bin',
            '/usr/bin',
            '/bin',
        ]),
        'CLASSPATH': pathsep.join([
            path.join(components_prefix, 'lib', 'java'),
        ]),
        'SIDL_DLL_PATH': ';'.join([
            path.join(components_prefix, 'share', 'cca'),
        ]),
    }
    environ['LD_RUN_PATH'] = environ['LD_LIBRARY_PATH']

    return environ


def _is_executable(program):
    from os import access, X_OK
    return path.isfile(program) and access(program, X_OK)


def audit(environ):
    from os import linesep

    messages = []

    for command in ['TAIL', 'CURL', 'BASH']:
        if not _is_executable(environ[command]):
            messages.append('%s: file is not executable' % command)

    for path_var in ['PYTHONPATH', 'LD_LIBRARY_PATH', 'PATH', 'CLASSPATH']:
        for item in environ[path_var].split(pathsep):
            if not path.isdir(item):
                messages.append('%s: not a directory' % item)

    for path_var in ['SIDL_DLL_PATH']:
        for item in environ[path_var].split(';'):
            if not path.isdir(item):
                messages.append('%s: not a directory' % item)

    return linesep.join(messages)


def main():
    environ = env_from_config_path('wmt.cfg')
    for item in environ.items():
        print 'export %s=%s' % item
    print audit(environ)


if __name__ == '__main__':
    main()
