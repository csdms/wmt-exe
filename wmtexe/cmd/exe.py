from os.path import expanduser
import subprocess

from ..env import WmtEnvironment


def main():
    import argparse
    import traceback

    parser = argparse.ArgumentParser()
    parser.add_argument('id', help='run ID')
    parser.add_argument('--server-url',
                        default='https://csdms.colorado.edu/wmt/api-dev',
                        help='URL of WMT server')
    parser.add_argument('--exec-dir', default=expanduser('~/.wmt'),
                        help='path to execution directory')
    parser.add_argument('--config', default=None,
                        help='WMT site configuration file')
    parser.add_argument('--show-env', action='store_true',
                        help='print execution environment and exit')
    parser.add_argument('--daemon', action='store_true', default=False,
                        help='run in daemon mode')
    args = parser.parse_args()

    env = WmtEnvironment.from_config(args.config)

    cmd = ['wmt-slave', args.id, '--server-url=%s' % args.server_url,
           '--exec-dir=%s' % args.exec_dir]

    if args.show_env:
        cmd.append('--show-env')

    if args.daemon:
        with open(args.id + '.o.txt', 'w') as stdout:
            with open(args.id + '.e.txt', 'w') as stderr:
                pipe = subprocess.Popen(cmd, env=env.env, stdout=stdout,
                                        stderr=stderr)
        print pipe.pid
    else:
        subprocess.call(cmd, env=env.env)
