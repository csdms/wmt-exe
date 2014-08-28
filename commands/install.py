from setuptools.command.install import install
import os

from ..wmtexe.config import default_file


_HELP_MESSAGE = """
Missing configuration file wmt.cfg. Run 'setup.py configure' first. For help
on creating a WMT configuration file,

    setup.py configure --help

nothing installed.
""".strip()


def _mkdir_if_missing(path):
    try:
        os.mkdir(path)
    except OSError:
        pass


def _make_config_if_missing(filename):
    if not os.path.isfile(filename):
        with open(filename, 'w') as cfg:
            cfg.write(default_config())


class Install(install):
    """Install wmt-exe.
    """
    description = 'Install WMT-exe'

    user_options = [
        ('install-etc', None, 'path to local configuration files'),
    ] + install.user_options

    def initialize_options(self):
        self.install_etc = None
        install.initialize_options(self)

    def run(self):
        _make_config_if_missing('wmt.cfg')

        install.run(self)

        prefix = os.path.commonprefix([self.install_lib,
                                       self.install_scripts])

        install_etc = self.install_etc or os.path.join(prefix, 'etc')

        _mkdir_if_missing(install_etc)

        self.copy_file('wmt.cfg', os.path.join(install_etc, 'wmt.cfg'))
