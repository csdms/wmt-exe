from __future__ import print_function
import sys
import os

from ..env import WmtEnvironment


_ACTIVATE_SCRIPT = """
# This file must be used with "source wmt-activate" *from bash*
# you cannot run it directly

if [ -n "$BASH" -o -n "$ZSH_VERSION" ] ; then
    hash -r
fi

{ENVIRONMENT}
""".strip()


def main():
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument('file', nargs='?', type=str,
                        default=None, help='WMT config file')
    args = parser.parse_args()

    env = WmtEnvironment.from_config(args.file)
    #print(_ACTIVATE_SCRIPT.format(ENVIRONMENT=str(env)))
    print(str(env))
