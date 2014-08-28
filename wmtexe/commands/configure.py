from __future__ import absolute_import

from setuptools import Command
from distutils.spawn import find_executable
import subprocess
from os import path, pathsep
import sys


_REQUIRED_PROGRAMS = ['curl', 'bash', 'tail', 'babel-config',
                      'cca-spec-babel-config', 'python']


def default_config():
    conf = {}

    for program in _REQUIRED_PROGRAMS:
        conf[program] = find_executable(program) or program
    conf['wmt-prefix'] = '/usr/local'
    conf['components-prefix'] = '/usr/local'

    return conf

_PATH_ATTRIBUTES = [
    ('curl', 'with_curl'), ('tail', 'with_tail'), ('bash', 'with_bash'),
    ('python', 'with_python'), ('babel_config', 'with_babel_config'),
    ('cca_spec_babel_config', 'with_cca_spec_babel_config'),
    ('wmt_prefix', 'wmt_prefix'),
    ('components_prefix', 'components_prefix')
]


class Configure(Command):
    """Create local configuration file.
    """
    description = 'create WMT-exe configuration file'

    user_options = [
        ('with-curl=', None, 'path to curl command'),
        ('with-bash=', None, 'path to bash command'),
        ('with-tail=', None, 'path to tail command'),
        ('with-babel-config=', None, 'path to babel-config command'),
        ('with-cca-spec-babel-config=', None, 'path to cca-spec-babel-config command'),
        ('with-python=', None, 'path to python command'),
        ('wmt-prefix=', None, 'prefix of WMT installation'),
        ('components-prefix=', None, 'prefix of components installation'),
        ('clobber', None, 'clobber existing configuration'),
    ]

    def initialize_options(self):
        default = default_config()

        for item in _PATH_ATTRIBUTES:
            setattr(self, item[1], default[item[0]])

        self.clobber = False

    def finalize_options(self):
        for (opt, _, _) in self.user_options:
            if opt.startswith('with_'):
                setattr(self, opt, path.normpath(getattr(self, opt)))

    def set_paths_section(self, config):
        section = 'paths'

        config.has_section(section) or config.add_section(section)
        for (path, attr) in _PATH_ATTRIBUTES:
            config.set(section, path, getattr(self, attr))

    def set_launcher_section(self, config):
        section = 'launcher'
        config.has_section(section) or config.add_section(section)
        config.set(section, 'launcher', self.launcher)

    def run(self):
        import ConfigParser

        config = ConfigParser.RawConfigParser()
        self.set_paths_section(config)
        self.set_launcher_section(config)

        if path.isfile('wmt.cfg') and not self.clobber:
            print 'wmt.cfg: file exists (use --clobber to overwrite)'
        else:
            with open('wmt.cfg', 'w') as opened:
                config.write(opened)
            print 'configuration written to wmt.cfg'
