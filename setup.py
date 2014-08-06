from setuptools import setup, find_packages
from codecs import open
from os import path


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
    raise RuntimeError("Unable to find vresion string.")


setup(
    name='wmtexe',
    version=find_version("wmtexe/__init__.py"),
    description='WMT execution server.',
    long_description=read('README.md'),
    url='https://github.com/csdms/wmt-exe',

    author='Eric Hutton',
    author_email='hutton.eric@gmail.com',

    license='MIT',

    packages=find_packages(),

    entry_points={
        'console_scripts': [
            'wmt-slave=wmtexe.slave:main',
        ],
    },
)
