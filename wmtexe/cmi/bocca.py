#! /usr/bin/env python
import os
import subprocess
import types
import re
import fileinput
import shutil
import glob
from string import Template

import yaml
from distutils.dir_util import mkpath

from .utils import cd, mktemp, which, system, check_output


class Error(Exception):
    pass


class ProjectExistsError(Error):
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


def is_bocca_project(name):
    return os.path.isdir(os.path.join(name, 'BOCCA'))


def create_project(name, bocca=None, language=None, ifexists='pass'):
    if ifexists not in ['pass', 'raise']:
        raise ValueError('ifexists value not understood')

    bocca = bocca or which('bocca')
    options = []
    if language is not None:
        options += ['--language=%s' % language]

    if is_bocca_project(name):
        if ifexists == 'raise':
            raise ValueError('project exists')
    else:
        system([bocca, 'create', 'project', name] + options)


def create_interface(name, bocca=None, sidl=None):
    bocca = bocca or which('bocca')
    options = []
    if sidl is not None:
        options += ['--import-sidl=%s@%s' % (name, sidl)]

    system([bocca, 'create', 'interface', name] + options)


def create_class(name, bocca=None, implements=None, language=None, sidl=None,
                 impl=None, includes='', libs=''):
    bocca = bocca or which('bocca')
    options = []
    if sidl is not None:
        options += ['--import-sidl=%s@%s' % (name, sidl)]
    if impl is not None:
        options += ['--import-impl=%s@%s' % (name, impl)]
    if language is not None:
        options += ['--language=%s' % language]
    if implements is not None:
        options += ['--implements=%s' % implements]

    system([bocca, 'create', 'class', name] + options)

    if impl:
        for fname in ['make.vars.user', 'make.rules.user']:
            shutil.copy(os.path.join(impl, fname),
                        os.path.join('components', name))

    #make_vars_user = 'components/%s/make.vars.user' % name

    #f = fileinput.input(make_vars_user, inplace=True)
    #for line in f:
    #    if line.startswith('INCLUDES ='):
    #        print ' '.join([line.rstrip(), includes])
    #    elif line.startswith('LIBS ='):
    #        print ' '.join([line.rstrip(), libs])
    #    else:
    #        print line.rstrip()
    #f.close ()


def class_language(name, bocca=None):
    bocca = bocca or which('bocca')

    import re

    lines = check_output([bocca, 'display', 'class', name]).split(os.linesep)
    m = re.search('\((?P<lang>\w+)\)', lines[0])
    return m.group('lang')


def class_files(name, bocca=None, pattern=None):
    from fnmatch import fnmatch

    bocca = bocca or which('bocca')

    files = check_output([bocca, 'display', 'class', '-f', name]).split()
    if pattern:
        return [f for f in files if fnmatch(f, pattern)]
    else:
        return files


def replace_class_name(src, dest, include=None, prefix=None, cflags=None,
                       libs=None):
    import re

    cflags = cflags or ''
    libs = libs or ''

    subs = ((re.sub('\.', '_', src), re.sub('\.', '_', dest)),
            (src, dest),
            ('BMI_HEAT', prefix),
            ('bmi_heat.h', include),
            ('Heat', dest.split('.')[-1]),
           )

    for path in class_files(dest):
        f = fileinput.input(path, inplace=True)
        for line in f:
            for sub in subs:
                line = re.sub(sub[0], sub[1], line)
            if line.startswith('INCLUDES ='):
                line = ' '.join([line.rstrip(), cflags])
            elif line.startswith('LIBS ='):
                line = ' '.join([line.rstrip(), libs])

            print line.rstrip()
        f.close()


def substitute_in_file(file_like, pattern, repl):
    if isinstance(file_like, types.StringTypes):
        with open(file_like, 'r') as fp:
            contents = fp.read()
    else:
        contents = file_like.read()

    return re.sub(pattern, repl, contents)

    if inplace:
        with open(path, 'w') as fp:
            fp.write(contents)


def substitute_patterns(subs, string):
    for pattern, repl in subs:
        string = re.sub(pattern, repl, string)
    return string


def substitute_patterns_in_file(subs, file_like):
    if isinstance(file_like, types.StringTypes):
        with open(file_like, 'r') as fp:
            contents = fp.read()
    else:
        contents = file_like.read()
    return substitute_patterns(subs, contents)


def replace_c_class_names(paths, src, dest, inplace=True):
    src_with_underscores = re.sub('\.', '_', src)
    dest_with_underscores = re.sub('\.', '_', dest)
    subs = (
        (src_with_underscores, dest_with_underscores),
        (src, dest),
    )

    for path in paths:
        contents = substitute_patterns_in_file(subs, path)
        if not inplace:
            path = re.sub(src_with_underscores, dest_with_underscores,
                          os.path.basename(path))
        with open(path, 'w') as fp:
            fp.write(contents)


def replace_cxx_class_names(paths, src, dest, inplace=True):
    src_with_underscores = re.sub('\.', '_', src)
    dest_with_underscores = re.sub('\.', '_', dest)
    src_with_colons = re.sub('\.', '::', src)
    dest_with_colons = re.sub('\.', '::', dest)
    subs = (
        (src_with_underscores, dest_with_underscores),
        (src_with_colons, dest_with_colons),
        (src, dest),
    )

    for path in paths:
        contents = substitute_patterns_in_file(subs, path)
        if not inplace:
            path = re.sub(src_with_underscores, dest_with_underscores,
                          os.path.basename(path))
        with open(path, 'w') as fp:
            fp.write(contents)


def replace_bmi_names(paths, mapping):
    for path in paths:
        with open(path, 'r') as fp:
            contents = Template(fp.read()).safe_substitute(mapping)
        with open(path, 'w') as fp:
            fp.write(contents)


def copy_class(src, dest, bocca=None):
    bocca = bocca or which('bocca')

    system([bocca, 'copy', 'class', src, dest])

    if class_language(dest) == 'c':
        replace_c_class_names(class_files(dest, pattern='*.[ch]'), src, dest)


def dup_c_impl(path, new, destdir='.'):
    old = os.path.basename(path)

    impl_files = (glob.glob(os.path.join(path, '*.[ch]')) +
                  glob.glob(os.path.join(path, 'make.*.user')))

    with cd(os.path.join(destdir, new)) as _:
        replace_c_class_names(impl_files, old, new, inplace=False)

    return os.path.join(destdir, new)


def dup_cxx_impl(path, new, destdir='.'):
    old = os.path.basename(path)

    impl_files = (glob.glob(os.path.join(path, '*.cxx')) +
                  glob.glob(os.path.join(path, '*.hxx')) +
                  glob.glob(os.path.join(path, 'make.*.user')))

    with cd(os.path.join(destdir, new)) as _:
        replace_cxx_class_names(impl_files, old, new, inplace=False)

    return os.path.join(destdir, new)


def dup_impl_files(path, new, destdir='.', language=None):
    language = language or guess_language_from_files(path)

    if language == 'c':
        return dup_c_impl(path, new, destdir=destdir)
    elif language == 'cxx':
        return dup_cxx_impl(path, new, destdir=destdir)
    else:
        return None


def guess_language_from_files(path):
    from glob import glob

    with cd(path) as _:
        if len(glob('*.[ch]')) > 0:
            return 'c'
        elif len(glob('*.cxx') + glob('*.hxx')) > 0:
            return 'cxx'
        else:
            return None


_GRID_TYPE_FUNCTIONS = {
    'uniform_rectilinear': [
        'get_grid_shape', 'get_grid_spacing', 'get_grid_origin',
    ],
    'rectilinear': [
        'get_grid_shape', 'get_grid_x', 'get_grid_y',
    ],
    'structured': [
        'get_grid_shape', 'get_grid_x', 'get_grid_y',
    ],
    'unstructured': [
        'get_grid_offset', 'get_grid_connectivity',
    ],
}

def get_grid_type_defines(grid_types):
    if isinstance(grid_types, types.StringTypes):
        grid_types = [grid_types]

    defines = []
    for grid_type in grid_types:
        for func in _GRID_TYPE_FUNCTIONS[grid_type]:
            defines.append('#define BMI_HAS_%s' % func.upper())

    return os.linesep.join(defines)


def create_bmi_class(name, bocca=None, language='c', bmi_mapping=None,
                     pkg_config_package=None, impl=None):
    bocca = bocca or which('bocca')
    bmi_mapping = bmi_mapping or {}

    if pkg_config_package:
        bmi_mapping.setdefault('cflags', pkg_config(pkg_config_package, '--cflags'))
        bmi_mapping.setdefault('libs', pkg_config(pkg_config_package, '--libs'))

    bmi_mapping.setdefault('includes', '')
    if not isinstance(bmi_mapping['includes'], types.StringTypes):
        bmi_mapping['includes'] = os.linesep.join(bmi_mapping['includes'])

    bmi_mapping.setdefault('prefix', '')
    try:
        bmi_mapping['defines'] = get_grid_type_defines(bmi_mapping['grids'])
    except KeyError:
        bmi_mapping['defines'] = ''

    for key in bmi_mapping.keys():
        bmi_mapping['bmi_' + key] = bmi_mapping[key]

    with mktemp(prefix='csdms', suffix='.d') as destdir:
        #impl_dir = dup_c_impl(impl, name, destdir=destdir)
        if impl is not None:
            impl_dir = dup_impl_files(impl, name, destdir=destdir)
            replace_bmi_names(glob.glob(os.path.join(impl_dir, '*')),
                              bmi_mapping)
        else:
            impl_dir = None

        create_class(name, bocca=bocca, implements='csdms.core.Bmi',
                     language=language, impl=impl_dir)


_THIS_DIR = os.path.dirname(__file__)
_PATH_TO_IMPL = {
    'c': os.path.join(_THIS_DIR, 'data', 'csdms.examples.c.Heat'),
    'cxx': os.path.join(_THIS_DIR, 'data', 'csdms.examples.cxx.Heat'),
    'f90': os.path.join(_THIS_DIR, 'data', 'csdms.examples.f90.Heat'),
}


def make_project(proj):
    create_project(proj['name'], language=proj['language'])
    with cd(proj['name']) as path:
        for interface in proj.get('interfaces', []):
            name = interface.pop('name')
            create_interface(name, **interface)

        for clazz in proj.get('bmi', []):
            name = 'csdms.%s' % clazz.pop('name')
            #name = 'csdms.model.%s' % clazz.pop('name')
            clazz.setdefault('impl', _PATH_TO_IMPL[clazz['language']])
            create_bmi_class(name, bmi_mapping=clazz, impl=clazz['impl'],
                             language=clazz['language'])
