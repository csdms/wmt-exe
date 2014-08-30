from setuptools import setup, find_packages

from codecs import open
from os import path

from wmtexe.commands.configure import Configure
from wmtexe.commands.install import Install


_HERE = path.abspath(path.dirname(__file__))


def read(*names, **kwds):
    return open(
        path.join(_HERE, *names),
        encoding=kwds.get('encoding', 'utf-8')
    ).read()


def find_version(*file_paths):
    import re

    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='wmtexe',
    version=find_version("wmtexe/__init__.py"),
    description='WMT execution server.',
    long_description=read('README.md'),
    url='https://github.com/csdms/wmt-exe',

    author='Eric Hutton',
    author_email='hutton.eric@gmail.com',

    license='MIT',

    packages=['wmtexe', 'wmtexe.cmd', ],

    entry_points={
        'console_scripts': [
            'wmt-slave=wmtexe.cmd.slave:main',
            'wmt-exe=wmtexe.cmd.exe:main',
            'wmt-audit=wmtexe.cmd.audit:main',
            'wmt-activate=wmtexe.cmd.activate:main',
            'wmt-script=wmtexe.cmd.script:main',
            'wmt-quickstart=wmtexe.cmd.quickstart:main',
            'wmt-info=wmtexe.cmd.info:main',
        ],
    },

    cmdclass={
        'configure': Configure,
        'install': Install,
    },
)
