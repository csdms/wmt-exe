"""Launch a WMT simulation using `bash` or `qsub`."""

from __future__ import print_function
import sys
import os

from ..launcher import BashLauncher, QsubLauncher


_LAUNCHERS = {
    'bash': BashLauncher,
    'qsub': QsubLauncher,
}


def main():
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument('uuid', type=str,
                        help='Unique identifier for simulation')
    parser.add_argument('--extra-args', default='',
                        help='Extra arguments for wmt-slave command')
    parser.add_argument('--server-url', default='',
                        help='WMT API server URL')
    parser.add_argument('--launcher', choices=_LAUNCHERS.keys(),
                        default='bash', help='Launch method')
    parser.add_argument('--run', action='store_true',
                        help='Launch simulation')

    args = parser.parse_args()

    launcher = _LAUNCHERS[args.launcher](args.uuid,
                                         server_url=args.server_url)
    if args.run:
        launcher.run()
    else:
        print(launcher.script())

