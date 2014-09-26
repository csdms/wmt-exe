from os import path, pathsep
import subprocess

from . import formatting


def audit(environ):
    """Check a wmt-exe environment.

    Parameters
    ----------
    environ : dict
        Environment variables.

    Returns
    -------
    string :
        Warnings/errors.
    """
    from os import linesep

    messages = []

    for command in ['TAIL', 'CURL', 'BASH']:
        messages.append(check_is_executable(environ[command]))

    for path_var in ['PYTHONPATH', 'LD_LIBRARY_PATH', 'PATH', 'CLASSPATH']:
        for item in environ[path_var].split(pathsep):
            messages.append(check_is_dir(item))

    for path_var in ['SIDL_DLL_PATH']:
        for item in environ[path_var].split(';'):
            messages.append(check_is_dir(item))

    for module in ['csdms', 'csdms.model']:
        messages.append(check_is_module(module, env=environ))

    for component in find_components(env=environ):
        module = '.'.join(['csdms.model', component])
        messages.append(check_is_module(module, env=environ))

    for component in find_components(env=environ):
        module = '.'.join(['csdms.model', component])
        messages.append(check_is_component(module, component,
                                           env=environ))

    return linesep.join(messages)


def _is_executable(program):
    from os import access, X_OK, path
    return path.isfile(program) and access(program, X_OK)


def result_message(assertion, checking):
    if assertion:
        return ' '.join([formatting.green(u'\u2713'), checking, 'yes'])
    else:
        return ' '.join([formatting.red(u'\u2717'), checking, 'no'])


def check_is_executable(program):
    check_message = '%s is executable...' % program
    return result_message(_is_executable(program), check_message)


def check_is_dir(path_to_dir):
    check_message = '%s is a directory...' % path_to_dir
    return result_message(path.isdir(path_to_dir), check_message)


def check_is_module(module_name, python='python', env=None):
    check_message = 'import %s...' % module_name
    try:
        subprocess.check_output(
            [python, '-c', 'import %s' % module_name], env=env)
    except subprocess.CalledProcessError:
        result = False
    else:
        result = True
    return result_message(result, check_message)


def check_is_component(module_name, component, python='python', env=None):
    check_message = 'instantiate %s...' % component
    try:
        subprocess.check_output(
            [python, '-c', 'from %s import %s; %s()' %
             (module_name, component, component)], env=env).strip()
    except subprocess.CalledProcessError:
        result = False
    else:
        result = True
    return result_message(result, check_message)


def path_to_python_module(module_name, python='python', env=None):
    try:
        path_to_module = subprocess.check_output(
            [python, '-c', 'import %s; print(%s.__path__)[0]' %
             (module_name, module_name)], env=env).strip()
    except subprocess.CalledProcessError:
        return None
    else:
        return path_to_module


def find_components(python='python', env=None):
    from glob import glob

    path_to_mod = path_to_python_module('csdms.model', python=python,
                                        env=env)
    if path_to_mod is not None:
        shared_libs = glob(path.join(path_to_mod, '*.so'))
        return [path.basename(lib[:-3]) for lib in shared_libs]
    else:
        return []
