#! /usr/bin/env python
import os

from .utils import which, check_output, system, cd, status


def git_repo_name(url):
    (base, _) = os.path.splitext(os.path.basename(url))
    return base


def git_repo_sha(url, git=None, branch='master'):
    git = git or which('git')

    lines = check_output([git, 'ls-remote', url]).strip().split(os.linesep)
    shas = dict()
    for line in lines:
        (sha, name) = line.split()
        shas[name] = sha

    return shas['refs/heads/{branch}'.format(branch=branch)][:10]


def git_clone(url, git=None, dir='.', branch='master'):
    git = git or which('git')

    with cd(dir):
        system([git, 'init', '-q'])
        system([git, 'config', 'remote.origin.url', url])
        system([git, 'config', 'remote.origin.fetch',
                '+refs/heads/*:refs/remotes/origin/*'])
        system([git, 'fetch', 'origin',
                '{branch}:refs/remotes/origin/{branch}'.format(branch=branch),
                '-n', '--depth=1'])
        system([git, 'reset', '--hard',
                'origin/{branch}'.format(branch=branch)])


def git_pull(url, dir='.', branch='master'):
    with cd(dir):
        system(['git', 'checkout', '-q', branch])
        system(['git', 'pull', 'origin', '-q',
                'refs/heads/{branch}:refs/remotes/origin/{branch}'.format(branch=branch)])


def git_clone_or_update(url, dir='.', branch='master'):
    if os.path.isdir(os.path.join(dir, '.git')):
        status('Updating %s' % url)
        git_pull(url, dir=dir, branch=branch)
    else:
        status('Cloning %s' % url)
        git_clone(url, dir=dir, branch=branch)
