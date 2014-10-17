import os
import argparse

from ..slave import Slave
from ..env import WmtEnvironment
from cmt.component.model import Model


def run(path):
    os.chdir(path)

    import yaml
    with open('model.yaml', 'r') as opened:
        model = yaml.load(opened.read())

    status_file = os.path.abspath(os.path.join(
        model['driver'], '_time.txt'))

    #status = TaskStatus(self.id, self.server, status_file)
    #timer = threading.Thread(target=status)
    #timer.start()

    with open('components.yaml', 'r') as opened:
        model = Model.load(opened.read())

    #report('running', 'running model')
    #model.go(file='model.yaml')
    #report('running', 'finished')


def main():
    import argparse
    import traceback

    parser = argparse.ArgumentParser(
        description="Run a WMT simulation")
    parser.add_argument('path', help='Path to simulation directory')

    parser.add_argument('--config', default=None,
                        help='WMT site configuration file')
    parser.add_argument('--show-env', action='store_true',
                        help='print execution environment and exit')
    parser.add_argument('--verbose', action='store_true',
                        help='Be verbose')

    args = parser.parse_args()

    env = WmtEnvironment.from_config(args.config)

    if args.show_env:
        print str(env)
        return

    run(args.path)
