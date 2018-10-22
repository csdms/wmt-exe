"""Launch a WMT simulation using `bash` or `qsub`."""

from __future__ import print_function

import sys
import os

from ..launcher import BashLauncher, QsubLauncher, SbatchLauncher
from ..config import load_configuration


_LAUNCHERS = {
    'bash': BashLauncher,
    'qsub': QsubLauncher,
    'sbatch': SbatchLauncher,
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
    parser.add_argument('--config', default='',
                        help='WMT site configuration file')
    parser.add_argument('--run', action='store_true',
                        help='Launch simulation')

    args = parser.parse_args()

    config = load_configuration(args.config)
    launch_dir = config.get('paths', 'launch_dir')
    exec_dir = config.get('paths', 'exec_dir')

    extra_args = []
    extra_args.append('--exec-dir={}'.format(os.path.expandvars(exec_dir)))
    if args.extra_args:
        extra_args.append(args.extra_args)

    launcher = _LAUNCHERS[args.launcher](args.uuid,
                                         server_url=args.server_url,
                                         launch_dir=launch_dir,
                                         extra_args=extra_args)

    if args.run:
        launcher.run()
    else:
        print(launcher.script().strip())

