"""Audit the setup for a WMT simulation."""

from .. import formatting
from ..env import WmtEnvironment
from ..audit import audit


def main():
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument('file', nargs='?', type=str, default=None,
                        help='WMT config file')
    args = parser.parse_args()

    env = WmtEnvironment.from_config(args.file)

    print formatting.red('Auditing the following environment')
    print str(env)

    print '\n\n'
    print formatting.red('This is what I found...')
    print audit(env.env)
