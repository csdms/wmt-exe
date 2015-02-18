import argparse

import yaml

from .bocca import make_project, ProjectExistsError


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='Project description file')

    args = parser.parse_args()

    try:
        with open(args.file, 'r') as fp:
            make_project(yaml.load(fp))
    except ProjectExistsError as error:
        print 'The specified project (%s) already exists. Exiting.' % error


if __name__ == '__main__':
    main()
