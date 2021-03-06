"""Classes to configure and launch jobs from a wmt-exe environment."""

import os
import sys
import subprocess


class Launcher(object):
    """Job launcher for a wmt-exe environment.

    Parameters
    ----------
    sim_id : str
        A unique UUID for the job.
    server_url : str or None, optional
        The URL of the WMT API server from which the job was submitted.
    launch_dir : str, optional
        The working directory from which the job is started.
    extra_args : list, optional
        Extra arguments to be passed to the wmt-slave command.

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
    _script = "{slave_command}"

    def __init__(self, sim_id, server_url=None, launch_dir='~/.wmt',
                 extra_args=[]):
        self.sim_id = sim_id
        self.server_url = server_url
        self.launch_dir = os.path.expandvars(os.path.expanduser(launch_dir))
        self.script_path = os.path.join(self.launch_dir,
                                        '%s.sh' % self.sim_id)
        self._extra_args = extra_args

    def before_launch(self, **kwds):
        """Perform actions before launching job.

        Parameters
        ----------
        **kwds
            Arbitrary keyword arguments.

        """
        try:
            os.makedirs(self.launch_dir)
        except OSError:
            if not os.path.isdir(self.launch_dir):
                raise
        with open(self.script_path, 'w') as f:
            f.write(self.script(**kwds))
        os.chmod(self.script_path, 0o755)

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
        """The command that runs a job.

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
            if isinstance(extra_args, str):
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


class SbatchLauncher(Launcher):
    """WMT job launcher for a Slurm scheduler.

    Parameters
    ----------
    sim_id : str
        A unique UUID for the job.
    server_url : str or None, optional
        The URL of the WMT API server from which the job was submitted.
    launch_dir : str, optional
        The working directory from which the job is started.
    extra_args : list, optional
        Extra arguments to be passed to the wmt-slave command.

    Attributes
    ----------
    launch_dir : str
        The working directory from which the job is started.
    script_path : str
        Path to launch script.
    run_script_path : str
        Path to run script, which submits launch script to scheduler.
    sim_id : str
        A unique UUID for the job.
    server_url : str or None
        The URL of the WMT API server from which the job was submitted.

    """
    _script = """
#!/usr/bin/env bash
#SBATCH --qos=blanca-csdms
#SBATCH --job-name=wmt
#SBATCH --mem=8000MB

export MPLBACKEND=Agg
{slave_command}
""".lstrip()
    _run_script = """
#!/usr/bin/env bash

source /etc/bashrc
module load slurm/blanca
sbatch --output={output_file} {script_path}
""".lstrip()

    def __init__(self, *args, **kwds):
        Launcher.__init__(self, *args, **kwds)
        self.run_script_path = os.path.expanduser(
            os.path.join(self.launch_dir,
                         '%s.run.sh' % self.sim_id))

    def before_launch(self, **kwds):
        """Perform actions before launching job.

        Parameters
        ----------
        **kwds
            Arbitrary keyword arguments.

        """
        Launcher.before_launch(self, **kwds)
        with open(self.run_script_path, 'w') as f:
            f.write(self.run_script(**kwds))
        os.chmod(self.run_script_path, 0o755)

    def run_script(self, **kwds):
        """Generate the run script that submits job to scheduler.

        Parameters
        ----------
        *kwds
            Arbitrary keyword arguments.

        Returns
        -------
        str
            The run script to be written to a file.

        """
        output_file = os.path.expanduser(
            os.path.join(self.launch_dir,
                         '%s.out' % self.sim_id))
        return self._run_script.format(output_file=output_file,
                                       script_path=self.script_path)

    def launch_command(self, **kwds):
        """The command that runs a job.

        Parameters
        ----------
        **kwds
            Arbitrary keyword arguments.

        Returns
        -------
        str
            The launch command to execute.

        """
        return self.run_script_path

    def launch(self, **kwds):
        """Launch job with launch command.

        Note that we override Launcher.launch because we want to
        inherit the environment from the current process.

        Parameters
        ----------
        **kwds
            Arbitrary keyword arguments.

        """
        subprocess.check_output(self.launch_command(**kwds))


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
