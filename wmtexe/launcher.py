import os
import subprocess
from types import StringTypes


class Launcher(object):
    launch_dir = '~/.wmt'
    _script = "{slave_command}"
    _extra_args = []

    def __init__(self, sim_id):
        self.sim_id = sim_id
        self.script_path = os.path.join(self.launch_dir,
                                        '%s.sh' % self.sim_id)

    def before_launch(self, **kwds):
        with open(self.script_path, 'w') as f:
            f.write(self.script(**kwds))

    def after_launch(self, **kwds):
        pass

    def after_success(self, **kwds):
        pass

    def run(self, **kwds):
        self.before_launch(**kwds)

        try:
            self.launch(**kwds)
        except subprocess.SubprocessError:
            raise
        else:
            self.after_success(**kwds)
        finally:
            self.after_launch(**kwds)

    def launch(self, **kwds):
        subprocess.check_output(self.launch_command(**kwds), env={})

    def launch_command(self, **kwds):
        return self.script_path

    def slave_command(self, extra_args=None):
        import shlex
        from pipes import quote

        command = ['wmt-slave', quote(self.sim_id)] + self._extra_args

        if extra_args:
            if isinstance(extra_args, StringTypes):
                extra_args = shlex.split(extra_args)
            command += [quote(arg) for arg in extra_args]

        return ' '.join(command)

    def script(self, **kwds):
        return self._script.format(slave_command=self.slave_command(**kwds))


class QsubLauncher(Launcher):
    _script = """
#! /bin/bash
#PBS -q debug
#PBS -l mem=10gb
#PBS -j oe

cd $TMPDIR
source $(wmt-activate)

{slave_command}
""".strip()
    _extra_args = ['--exec-dir=$TMPDIR', ]
    
    def launch_command(self, **kwds):
        return ['qsub', '-o', self.launch_dir, self.script_path]


class BashLauncher(Launcher):
    _script = """
#! /bin/bash

source $(wmt-activate)

{slave_command}
""".strip()
