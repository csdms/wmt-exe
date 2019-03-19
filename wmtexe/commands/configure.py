"""Configures a wmt-exe environment with setuptools."""

from __future__ import absolute_import, print_function

from setuptools import Command
from distutils.spawn import find_executable
import subprocess
from os import path, pathsep
import sys


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
        ('launch-dir=', None, 'directory from which job is started'),
        ('exec-dir=', None, 'directory where job is run'),
        ('clobber', None, 'clobber existing configuration'),
    ]

    def initialize_options(self):
        self.with_curl = None
        self.with_bash = None
        self.with_tail = None
        self.with_babel_config = None
        self.with_cca_spec_babel_config = None
        self.wmt_prefix = None
        self.components_prefix = None
        self.launch_dir = None
        self.exec_dir = None
        self.clobber = False

    def finalize_options(self):
        pass

    def run(self):
        import configparser

        from ..config import SiteConfiguration

        config = SiteConfiguration()
        config.set('paths', 'curl', self.with_curl)
        config.set('paths', 'bash', self.with_bash)
        config.set('paths', 'tail', self.with_tail)
        config.set('paths', 'babel_config', self.with_babel_config)
        config.set('paths', 'cca_spec_babel_config',
                   self.with_cca_spec_babel_config)
        config.set('paths', 'wmt_prefix', self.wmt_prefix)
        config.set('paths', 'components_prefix', self.components_prefix)
        config.set('paths', 'launch_dir', self.launch_dir)
        config.set('paths', 'exec_dir', self.exec_dir)

        if path.isfile('wmt.cfg') and not self.clobber:
            print('wmt.cfg: file exists (use --clobber to overwrite)')
        else:
            config.write('wmt.cfg')
            print('configuration written to wmt.cfg')
