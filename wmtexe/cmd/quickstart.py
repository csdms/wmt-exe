import os
from distutils.spawn import find_executable

from .. import formatting
from ..config import default_paths


class Prompter(object):
    def __init__(self, prefix='> ', defaults=None, interactive=True):
        self._prefix = prefix.strip() + ' '
        self._vals = defaults or dict()
        self._interactive = interactive

    @property
    def vals(self):
        return self._vals

    def get(self, key, text, default=None):
        try:
            default = default or self._vals[key]
        except KeyError:
            pass

        self._vals[key] = self._get_non_empty_input(text, default=default)

    def _get_non_empty_input(self, text, default=None):
        if self._interactive:
            while True:
                val = raw_input(self.render_prompt(text, default=default))
                if default and not val:
                    val = default
                break
        else:
            val = default or '?'
        return val


    def list(self, key, text, default=None):
        vals = []
        while True:
            val = raw_input(self.render_prompt(text, default=default))
            if default and not val:
                val = default
            if len(val.strip()) > 0:
                vals.append(val)
            else:
                break
        self._vals[key] = vals

    def render_prompt(self, text, default=None):
        prompt = self._prefix + '%s' % text
        if default:
            prompt += ' [%s]' % default
        prompt += ': '
        return formatting.dim(formatting.lightgreen(prompt))


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


def prompt_for_paths(**kwds):
    prompt = Prompter('>>>', defaults=default_paths(),
                      interactive=kwds.get('interactive', False))

    prompt.get('bash', 'path to bash')
    prompt.get('tail', 'path to tail')
    prompt.get('curl', 'path to curl')
    prompt.get('python', 'path to python')
    prompt.get('babel_config', 'path to babel-config')
    prompt.get('cca_spec_babel_config', 'path to cca-spec-babel-config')

    return prompt.vals


def prompt_for_launcher(**kwds):
    prompt = Prompter('>>>', **kwds)
    prompt.get('launcher', 'wmt-exe launcher', default='bash-launcher')

    if prompt.vals['launcher'] not in ['bash-launcher', 'qsub-launcher']:
        raise RuntimeError('%s: unknown launcher' % prompt.vals['launcher'])

    return prompt.vals


def prompt_for_bash_launcher(**kwds):
    prompt = Prompter('>>>', **kwds)
    prompt.get('bash', 'path to bash',
               default=find_executable('bash') or 'bash')
    return prompt.vals


def prompt_for_qsub_launcher(**kwds):
    prompt = Prompter('>>>', **kwds)
    prompt.get('qsub', 'path to qsub',
               default=find_executable('qsub') or 'qsub')
    return prompt.vals


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--batch', action='store_true', default=False,
                       help='run in batch mode')

    args = parser.parse_args()
    kwds = dict(interactive=not args.batch)

    sections = []

    paths = prompt_for_paths(**kwds)
    launcher = prompt_for_launcher(**kwds)

    sections.append(dict_to_ini(paths, 'paths'))
    sections.append(dict_to_ini(launcher, 'launcher'))

    if launcher['launcher'] == 'bash-launcher':
        bash_launcher = prompt_for_bash_launcher(**kwds)
        sections.append(dict_to_ini(bash_launcher, 'bash-launcher'))
    elif launcher['launcher'] == 'qsub-launcher':
        qsub_launcher = prompt_for_qsub_launcher(**kwds)
        sections.append(dict_to_ini(qsub_launcher, 'qsub-launcher'))

    print (os.linesep * 2).join(sections)
