#! /usr/bin/env python
import os

from .utils import which, check_output, system, cd


def git_repo_name(url):
    (base, _) = os.path.splitext(os.path.basename(url))
    return base


def git_repo_sha(url, git=None, branch='HEAD'):
    git = git or which('git')

    lines = check_output([git, 'ls-remote', url]).strip().split(os.linesep)
    shas = dict()
    for line in lines:
        (sha, name) = line.split()
        shas[name] = sha

    return shas[branch][:10]


def git_clone(url, git=None, dir='.'):
    git = git or which('git')

    with cd(dir):
        system([git, 'init', '-q'])
        system([git, 'config', 'remote.origin.url', url])
        system([git, 'config', 'remote.origin.fetch',
                '+refs/head/*:refs/remotes/origin/*'])
        system([git, 'fetch', 'origin',
                'master:refs/remotes/origin/master', '-n', '--depth=1'])
        system([git, 'reset', '--hard', 'origin/master'])


def git_pull(url, dir='.'):
    with cd(dir):
        system(['git', 'checkout', '-q', 'master'])
        system(['git', 'pull', 'origin', '-q',
                'refs/heads/master:refs/remotes/origin/master'])


def git_clone_or_update(url, dir='.'):
    if os.path.isdir(os.path.join(dir, '.git')):
        status('Updating %s' % url)
        git_pull(url, dir=dir)
    else:
        status('Cloning %s' % url)
        git_clone(url, dir=dir)
