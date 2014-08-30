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

    parser = argparse.ArgumentParser()

    parser.add_argument('uuid', type=str,
                        help='Unique identifier for simulation')
    parser.add_argument('--extra-args', default='',
                        help='Extra arguments for wmt-slave command')
    parser.add_argument('--launcher', choices=_LAUNCHERS.keys(),
                        default='bash', help='Launch method')

    args = parser.parse_args()

    launcher = _LAUNCHERS[args.launcher](args.uuid)
    print(launcher.script())

