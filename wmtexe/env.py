"""Classes for configuring a wmt-exe environment."""

import sys
from os import path, pathsep, linesep
from collections import OrderedDict
import subprocess

from . import formatting
from .config import load_configuration


class Babel(object):
    """CCA Babel configuration.

    Parameters
    ----------
    **kwds
        Arbitrary keyword arguments.

    """
    def __init__(self, **kwds):
        prefix = kwds.get('prefix', '')
        babel_config = kwds.get('babel_config', 'babel-config')
        cca_spec_babel_config = kwds.get('cca_spec_babel_config',
                                         'cca-spec-babel-config')

        self._babel_config = path.join(prefix, babel_config)
        self._cca_spec_babel_config = path.join(prefix,
                                                cca_spec_babel_config)
        self._prefix = self.query_var('prefix')
        self._libs = self.query_cca_spec_var('CCASPEC_BABEL_LIBS')

    @property
    def babel_config(self):
        """Babel configuration values."""
        return self._babel_config

    @property
    def cca_spec_babel_config(self):
        """cca-spec-babel configuration values."""
        return self._cca_spec_babel_config

    @property
    def prefix(self):
        """Prefix used for Babel installation."""
        return self._prefix

    @property
    def libs(self):
        """Libraries used with cca-spec-babel."""
        return self._libs

    def query_var(self, var):
        """Query a Babel configuration variable.

        Parameters
        ----------
        var : str
            Variable name.

        Returns
        -------
        str
            Variable information, or None on error.

        """
        try:
            return subprocess.check_output(
                [self.babel_config, '--query-var=%s' % var]).strip()
        except (OSError, subprocess.CalledProcessError):
            return None

    def query_cca_spec_var(self, var):
        """Query a cca-spec-babel configuration variable.

        Parameters
        ----------
        var : str
            Variable name.

        Returns
        -------
        str
            Variable information, or None on error.

        """
        try:
            return subprocess.check_output(
                [self.cca_spec_babel_config, '--var', var]).strip()
        except (OSError, subprocess.CalledProcessError):
            print [self.cca_spec_babel_config, '--var', var]
            raise
            return None


class Python(object):
    """Python configuration.

    Parameters
    ----------
    python : str, optional
        Python executable (default is 'python').

    """
    def __init__(self, python='python'):
        self._python = python
        self._version = self.query_version()
        self._prefix = self.query_exec_prefix()

    @property
    def executable(self):
        """Python executable."""
        return self._python

    @property
    def prefix(self):
        """Prefix for Python installation."""
        return self._prefix

    @property
    def version(self):
        """Python version."""
        return self._version

    def site_packages(self, prefix=None):
        """Path to Python `site-packages` directory.

        Parameters
        ----------
        prefix : str, optional
            Prefix for Python distribution.

        Returns
        -------
        str
            Path to `site-packages` directory.

        """
        return path.join(prefix or self.prefix, 'lib', self.version,
                         'site-packages')
    
    @property
    def lib(self):
        """Path to Python `lib` directory."""
        return path.join(self.prefix, 'lib')

    def query_version(self):
        """Get the version of Python.

        Get the version of a Python instance as *pythonX.Y*.

        Parameters
        ----------
        python : string
            Path to the Python program.

        Returns
        -------
        str
            The Python version as a string.

        """
        version = subprocess.check_output(
            [self.executable, '-c', 'import sys; print(sys.version[:3])'])
        return 'python%s' % version.strip()

    def query_exec_prefix(self):
        """Get the path to the Python executables directory.

        Returns
        -------
        str
            The Python exec path prefix.

        """
        prefix = subprocess.check_output(
            [self.executable, '-c', 'import sys; print(sys.exec_prefix)'])
        return path.normpath(prefix.strip())


class WmtEnvironment(object):
    """WMT executor configuration."""
    def __init__(self):
        self._env = {}

    @property
    def env(self):
        """WMT environment variables."""
        return OrderedDict(self._env)

    def to_dict(self):
        """Converts WMT environment variables to an OrderedDict.

        Returns
        -------
        OrderedDict
            WMT environment variables.

        """
        return OrderedDict(self._env)

    @classmethod
    def from_dict(clazz, *args, **kwds):
        """Loads WMT environment variables from arguments.

        Parameters
        ----------
        *args
            Variable length argument list.
        *kwds
            Arbitrary keyword arguments.

        Returns
        -------
        WmtEnvironment
            A WmtEnvironment instance.
        
        """
        env = clazz()

        d = dict(*args, **kwds)

        babel = Babel(babel_config=d['babel_config'],
                      cca_spec_babel_config=d['cca_spec_babel_config'])
        python = Python(python=d['python'])

        wmt_prefix = d['wmt_prefix']
        components_prefix = d['components_prefix']

        env._env.update({
            'CURL': d['curl'],
            'TAIL': d['tail'],
            'BASH': d['bash'],
            'PYTHONPATH': pathsep.join([
                python.site_packages(),
                path.join(python.prefix, 'lib', python.version),
                python.site_packages(components_prefix),
                python.site_packages(babel.prefix),
                path.join(babel.libs, python.version, 'site-packages'),
            ]),
            'LD_LIBRARY_PATH': pathsep.join([
                path.join(python.prefix, 'lib'),
                path.join(components_prefix, 'lib'),
                path.join(wmt_prefix, 'lib'),
                path.join(babel.prefix, 'lib'),
            ]),
            'PATH': pathsep.join([
                path.join(python.prefix, 'bin'),
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
        })
        env._env['LD_RUN_PATH'] = env['LD_LIBRARY_PATH']

        return env

    @classmethod
    def from_config(clazz, filenames):
        """Loads WMT environment variables from configuration files.

        Parameters
        ----------
        filenames : dict
            Configuration file(s).

        Returns
        -------
        WmtEnvironment
            A WmtEnvironment instance.
        
        """
        env = clazz()

        conf = load_configuration(filenames)
        return env.from_dict(conf.section('paths'))

    def __getitem__(self, key):
        return self._env[key]

    def __str__(self):
        lines = []
        for item in self._env.items():
            lines.append('export %s=%s' % item)
        return linesep.join(lines)
