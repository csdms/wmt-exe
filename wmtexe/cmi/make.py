import argparse

import yaml

from .bocca import make_project, ProjectExistsError


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=argparse.FileType('r'),
                        help='Project description file')
    parser.add_argument('--clobber', action='store_true',
                        help='Clobber an existing project')

    args = parser.parse_args()

    try:
        make_project(yaml.load(args.file), clobber=args.clobber)
    except ProjectExistsError as error:
        print 'The specified project (%s) already exists. Exiting.' % error


if __name__ == '__main__':
    main()
