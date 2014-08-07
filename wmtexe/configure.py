from setuptools import Command
from distutils.spawn import find_executable
import subprocess
from os import path, pathsep
import sys


def find_cca_tools(var):
    try:
        return subprocess.check_output(['babel-config',
                                        '--query-var=%s' % var]).strip()
    except (OSError, subprocess.CalledProcessError):
        return None


class Configure(Command):
    """Create local configuration file.
    """
    description = 'create WMT-exe configuration file'

    user_options = [
        ('with-curl=', None, 'path to curl command'),
        ('with-bash=', None, 'path to bash command'),
        ('with-tail=', None, 'path to tail command'),
        ('cca-prefix=', None, 'prefix of cca installation'),
        ('python-prefix=', None, 'prefix of python installation'),
        ('wmt-prefix=', None, 'prefix of WMT installation'),
        ('components-prefix=', None, 'prefix of components installation'),
        ('clobber', None, 'clobber existing configuration'),
    ]

    def initialize_options(self):
        self.with_curl = find_executable('curl') or '<path-to-curl>'
        self.with_bash = find_executable('bash') or '<path-to-bash>'
        self.with_tail = find_executable('tail') or '<path-to-tail>'

        self.cca_prefix = find_cca_tools('prefix') or '<path-to-cca-tools>'
        self.python_prefix = path.normpath(sys.exec_prefix)

        self.wmt_prefix = '<path-to-wmt>'
        self.components_prefix = '<path-to-components>'

        self.clobber = False

    def finalize_options(self):
        for opt in ['with_curl', 'with_bash', 'with_tail', 'cca_prefix']:
            setattr(self, opt, path.normpath(getattr(self, opt)))

    def run(self):
        import ConfigParser

        config = ConfigParser.RawConfigParser()
        config.add_section('wmt')
        config.set('wmt', 'curl', self.with_curl)
        config.set('wmt', 'tail', self.with_tail)
        config.set('wmt', 'bash', self.with_bash)
        config.set('wmt', 'cca_prefix', self.cca_prefix)
        config.set('wmt', 'wmt_prefix', self.wmt_prefix)
        config.set('wmt', 'python_prefix', self.python_prefix)
        config.set('wmt', 'components_prefix', self.components_prefix)

        if path.isfile('wmt.cfg') and not self.clobber:
            print 'wmt.cfg: file exists (use --clobber to overwrite)'
        else:
            with open('wmt.cfg', 'w') as opened:
                config.write(opened)
            print 'configuration written to wmt.cfg'
