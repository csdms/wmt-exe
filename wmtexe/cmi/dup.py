import argparse

import yaml

from .bocca import dup_c_impl


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='Path to impl files')
    parser.add_argument('name', help='Name of new class')

    args = parser.parse_args()

    dup_c_impl(args.path, args.name, destdir='.')


if __name__ == '__main__':
    main()
