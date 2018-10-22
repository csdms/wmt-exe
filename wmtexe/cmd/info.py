"""Get information about the current wmt-exe environment."""

from __future__ import print_function

import sys


def dict_to_ini(d, section):
    from ConfigParser import ConfigParser
    from StringIO import StringIO

    config = ConfigParser()
    config.add_section(section)

    for (key, value) in d.items():
        config.set(section, key, value)

    output = StringIO()
    config.write(output)

    contents = output.getvalue()
    output.close()

    return contents.strip()


def hostname():
    import socket
    return socket.getfqdn()


def main():
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ssh-port', default=22, help='SSH port to use')
    parser.add_argument('--directory', default=sys.exec_prefix,
                        help='directory of WMT installation')
    parser.add_argument('--host', default=hostname(),
                        help='FQHN of wmt execution server')

    args = parser.parse_args()

    host_info = {
        'host': args.host,
        'host_nickname': args.host.split('.')[0],
        'ssh_port': args.ssh_port,
        'directory': args.directory,
    }

    print(dict_to_ini(host_info, args.host))
