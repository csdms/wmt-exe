"""Classes to configure and launch jobs from a wmt-exe environment."""

import os
import sys
import stat
import subprocess
from types import StringTypes


class Launcher(object):
    """Job launcher for a wmt-exe environment.

    Parameters
    ----------
    sim_id : str
        A unique UUID for the job.
    server_url : str or None, optional
        The URL of the WMT API server from which the job was submitted.

    Attributes
    ----------
    launch_dir : str
        The working directory from which the job is started.
    script_path : str
        Path to launch script.
    sim_id : str
        A unique UUID for the job.
    server_url : str or None
        The URL of the WMT API server from which the job was submitted.

    """
    launch_dir = '~/.wmt'
    _script = "{slave_command}"
    _extra_args = []

    def __init__(self, sim_id, server_url=None):
        self.sim_id = sim_id
        self.server_url = server_url
        self.script_path = os.path.expanduser(
            os.path.join(self.launch_dir,
                         '%s.sh' % self.sim_id))

    def before_launch(self, **kwds):
        """Perform actions before launching job.

        Parameters
        ----------
        **kwds
            Arbitrary keyword arguments.

        """
        with open(self.script_path, 'w') as f:
            f.write(self.script(**kwds))
        os.chmod(self.script_path, stat.S_IXUSR|stat.S_IWUSR|stat.S_IRUSR)

    def after_launch(self, **kwds):
        """Perform actions after launching job.

        Parameters
        ----------
        **kwds
            Arbitrary keyword arguments.

        """
        pass

    def after_success(self, **kwds):
        """Perform actions after job completes.

        Parameters
        ----------
        **kwds
            Arbitrary keyword arguments.

        """
        pass

    def run(self, **kwds):
        """Perform job setup, launch, and teardown actions.

        Parameters
        ----------
        **kwds
            Arbitrary keyword arguments.

        """
        self.before_launch(**kwds)

        try:
            self.launch(**kwds)
        except subprocess.CalledProcessError:
            raise
        else:
            self.after_success(**kwds)
        finally:
            self.after_launch(**kwds)

    def launch(self, **kwds):
        """Launch job with launch command.

        Parameters
        ----------
        **kwds
            Arbitrary keyword arguments.

        """
        subprocess.check_output(self.launch_command(**kwds), env={})

    def launch_command(self, **kwds):
        """Path to launch script.

        Parameters
        ----------
        **kwds
            Arbitrary keyword arguments.

        Returns
        -------
        str
            The launch command to execute.

        """
        return self.script_path

    def slave_command(self, extra_args=None):
        """Create the `wmt-slave` command.

        Parameters
        ----------
        extra_args : str, optional
            Additional arguments.

        Returns
        -------
        str
            The slave command to execute.

        """
        import shlex
        from pipes import quote

        wmt_slave = os.path.join(sys.prefix, 'bin', 'wmt-slave')
        command = [wmt_slave, quote(self.sim_id)] + self._extra_args

        if self.server_url:
            command += ['--server-url={}'.format(self.server_url)]

        if extra_args:
            if isinstance(extra_args, StringTypes):
                extra_args = shlex.split(extra_args)
            command += [quote(arg) for arg in extra_args]

        return ' '.join(command)

    def script(self, **kwds):
        """Generate the launch script.

        Parameters
        ----------
        *kwds
            Arbitrary keyword arguments.

        Returns
        -------
        str
            The launch script to be written to a file.

        """
        return self._script.format(slave_command=self.slave_command(**kwds))


class QsubLauncher(Launcher):
    """WMT job launcher for a PBS scheduler."""
    _script = """
#! /bin/bash
#PBS -q debug
#PBS -l mem=10gb
#PBS -j oe
#PBS -k oe

cd $TMPDIR

{slave_command}
""".lstrip()
    _extra_args = ['--exec-dir=$TMPDIR']

    def launch_command(self, **kwds):
        """Path to launch script.

        Parameters
        ----------
        **kwds
            Arbitrary keyword arguments.

        Returns
        -------
        str
            The launch command to execute.

        """
        return ['/opt/torque/bin/qsub', '-o', self.launch_dir,
                self.script_path]


class BashLauncher(Launcher):
    """WMT job launcher for a bash environment."""
    _script = """
#! /bin/bash

export PATH={wmt_path}

{slave_command}
""".lstrip()

    def prepend_path(self):
        """Places the `bin` directory of executor at the front of the path."""
        return os.pathsep.join([os.path.join(sys.prefix, 'bin'),
                                os.environ['PATH']])

    def script(self, **kwds):
        """Generate the launch script.

        Parameters
        ----------
        *kwds
            Arbitrary keyword arguments.

        Returns
        -------
        str
            The launch script to be written to a file.

        """
        return self._script.format(wmt_path=self.prepend_path(),
                                   slave_command=self.slave_command(**kwds))
