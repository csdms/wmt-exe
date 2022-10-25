"""Get a WMT simulation.

Connect to a WMT server and download a staged simulation using a universal
unique identifier.
"""

from __future__ import print_function

import os
import sys
import argparse
import tarfile

from ..task import download_run_tarball, DownloadError
from ..env import WmtEnvironment


def download_or_exit(url, id, dest):
    try:
        tarball = download_run_tarball(url, id,
                                       dest_dir=dest)
    except DownloadError as error:
        print('==> Error: %s' % error)
        sys.exit(1)

    return os.path.normpath(tarball)


def unpack_or_exit(name, dest):
    try:
        with tarfile.open(name, 'r') as tar:
            def is_within_directory(directory, target):
                
                abs_directory = os.path.abspath(directory)
                abs_target = os.path.abspath(target)
            
                prefix = os.path.commonprefix([abs_directory, abs_target])
                
                return prefix == abs_directory
            
            def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
            
                for member in tar.getmembers():
                    member_path = os.path.join(path, member.name)
                    if not is_within_directory(path, member_path):
                        raise Exception("Attempted Path Traversal in Tar File")
            
                tar.extractall(path, members, numeric_owner=numeric_owner) 
                
            
            safe_extract(tar, path=dest)
    except tarfile.TarError as error:
        print('==> Error: %s' % error)
        sys.exit(1)
    try:
        base = name[:- len('.tar.gz')]
        for r, _, _ in os.walk(base):
            os.chmod(r, 0o777 - get_umask())
    except OSError:
        raise


def get_umask():
    current_umask = os.umask(0)
    os.umask(current_umask)
    return current_umask


def main():
    import argparse
    import traceback

    parser = argparse.ArgumentParser(
        description="Download and unpack a WMT simulation")
    parser.add_argument('id', help='Run ID')
    parser.add_argument('dest', nargs='?', default='.',
                        help='Destination directory')

    parser.add_argument('--url',
                        default='https://csdms.colorado.edu/wmt/api-dev',
                        help='URL of WMT server')
    parser.add_argument('--config', default=None,
                        help='WMT site configuration file')
    parser.add_argument('--clean', action='store_true',
                        help='Remove tarball after extracting')
    parser.add_argument('--show-env', action='store_true',
                        help='print execution environment and exit')
    parser.add_argument('--verbose', action='store_true',
                        help='Be verbose')
    parser.add_argument('--unpack', choices=('yes', 'no'),
                        default='yes',
                        help='Unpack the simulation tarball')

    args = parser.parse_args()

    env = WmtEnvironment.from_config(args.config)

    if args.show_env:
        print(str(env))
        return

    if args.verbose:
        print('==> connecting %s' % args.url)
        print('==> downloading %s' % args.id)

    tarball = download_or_exit(args.url, args.id, args.dest)

    if args.unpack == 'yes':
        if args.verbose:
            print('==> unpacking %s' % tarball)

        unpack_or_exit(tarball, args.dest)

        if args.clean:
            print('==> removing %s' % tarball)
            os.remove(tarball)

    if args.verbose:
        print('==> success')
