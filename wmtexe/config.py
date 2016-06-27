"""Tools for configuring a wmt-exe environment."""

from __future__ import absolute_import
import os
import sys
import types


def _find_executable(executable, **kwds):
    from distutils.spawn import find_executable

    return find_executable(executable, **kwds) or executable


_DEFAULTS = [
    ('paths', [
        ('curl', _find_executable('curl')),
        ('bash', _find_executable('bash')),
        ('tail', _find_executable('tail')),
        ('babel_config', _find_executable('babel-config')),
        ('cca_spec_babel_config', _find_executable(
            'cca-spec-babel-config')),
        ('python', _find_executable('python')),
        ('wmt_prefix', '/usr/local'),
        ('components_prefix', '/usr/local'),
    ]),
    ('launcher', [
        ('name', 'bash-launcher'),
    ]),
    ('bash-launcher', [
        ('bash', 'bash'),
    ]),
]


class SiteConfiguration(object):

    """Configure a wmt-exe environment."""

    def __init__(self):
        from ConfigParser import ConfigParser

        config = ConfigParser()
        for section, values in _DEFAULTS:
            config.add_section(section)
            for option, value in values:
                config.set(section, option, value)
        self._config = config

    def section(self, section):
        """Get the all the values of a section in the configuration.

        Parameters
        ----------
        section : str
            Name of section in configuration.

        Returns
        -------
        list of tuples
            Configuration values of section.

        """
        return self._config.items(section)

    def set(self, section, option, value):
        """Set a configuration value.

        Parameters
        ----------
        section : str
            Name of section in configuration.
        option : str
            Name of configuration option.
        value
            Value to be set.

        """
        if value is not None:
            if section == 'paths':
                value = os.path.normpath(value)
            self._config.set(section, option, value)

    def write(self, file):
        """Write a configuration file.

        Parameters
        ----------
        file : str
            Name of configuration file.

        """
        if isinstance(file, types.StringTypes):
            with open(file, 'w') as fp:
                self.write(fp)
        else:
            self._config.write(file)

    @classmethod
    def from_path(clazz, filenames):
        """Create a SiteConfiguration instance from a file or files.

        Parameters
        ----------
        filename : str or array-like of str
            Configuration file(s).

        Returns
        -------
        SiteConfiguration
            A SiteConfiguration object.

        """
        conf = clazz()
        conf._config.read(filenames)
        return conf

    def __str__(self):
        from StringIO import StringIO
        output = StringIO()
        self._config.write(output)

        contents = output.getvalue()
        output.close()

        return contents.strip()


DEFAULT = SiteConfiguration()
INSTALL_ETC = os.path.join(sys.exec_prefix, 'etc')
USER_CONFIG_PATH = os.path.expanduser('~/.wmt')


def load_configuration(filenames=None):
    """Load a wmt-exe configuration.

    Parameters
    ----------
    filenames : dict, optional
        Configuration files.

    Returns
    -------
    SiteConfiguration
        The configuration.

    """
    paths = filenames or ['wmt.cfg',
                          os.path.join(USER_CONFIG_PATH, 'wmt.cfg'),
                          os.path.join(INSTALL_ETC, 'wmt.cfg'),
                         ]
    return SiteConfiguration.from_path(paths)
