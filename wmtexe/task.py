"""Classes for running components in a wmt-exe environment."""

import os
import sys
import subprocess
import tarfile
import shutil
import json
import threading
import logging

from cmt.component.model import Model
from cmt.framework.services import register_component_classes


logger = logging.getLogger(__name__)
"""Logger : Instance of Logging class."""


def register_all_csdms_components():
    """Import all available CSDMS components."""
    try:
        from cmt.components import __all__ as names
    except ImportError:
        pass
    else:
        register_component_classes(
            ['cmt.components.{name}'.format(name=name) for name in names])


register_all_csdms_components()


class TaskError(Exception):
    """Base exception for an error thrown in a task."""
    pass


class TaskCompleted(Exception):
    """Base exception for a completed task."""
    pass


class UploadError(TaskError):
    """Exception raised on a failed file upload.

    Parameters
    ----------
    code : int
        Error code.
    filename : str
        File to be uploaded or downloaded.

    """
    def __init__(self, code, filename):
        self._code = code
        self._file = filename

    def __str__(self):
        return '%s: unable to upload (error %d)' % (self._file, self._code)


class DownloadError(UploadError):
    """Exception raised on a failed file download."""
    def __str__(self):
        return '%s: unable to download (error %d)' % (self._file, self._code)


class ComponentRunError(TaskError):
    """Runtime exception raised by a component.

    Parameters
    ----------
    msg : str
        Error message.

    """
    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return self._msg


def create_user_execution_dir(run_id, prefix='~/.wmt'):
    """Create the user execution directory.

    Parameters
    ----------
    run_id : str
        A unique UUID for a job.
    prefix : str, optional
        Path to the launch directory (default is "~/.wmt").

    Returns
    -------
    str
        Path to the user execution directory.

    """
    path = os.path.join(prefix, run_id)

    try:
        os.makedirs(path)
    except os.error:
        if os.path.isdir(path):
            pass
        else:
            raise

    return path


def components_to_run(path):
    """Define components to run.

    Parameters
    ----------
    path : str
        Path to a directory containing components.

    Returns
    -------
    dict
        Dict of components.

    """
    components = {}

    for item in os.listdir(path):
        if dir_contains_run_script(os.path.join(path, item)):
            components[item] = os.path.abspath(os.path.join(path, item))

    return components


def dir_contains_run_script(path):
    """Check whether a directory contains a run script.

    Parameters
    ----------
    path : str
        Path to a directory containing a component.

    Returns
    -------
    bool
        True if the directory contains a run script.

    """
    return os.path.isfile(os.path.join(path, 'run.sh'))


def run_component(name, **kwds):
    """Run a component.

    Parameters
    ----------
    name : str
        The name of a component.
    **kwds
        Optional keyword arguments.

    """
    try:
        subprocess.check_call(['/bin/bash', 'run.sh'], **kwds)
    except subprocess.CalledProcessError as error:
        raise ComponentRunError(generate_error_message(name, error, **kwds))


def generate_error_message(name, error, **kwds):
    """Generate an error message.

    Parameters
    ----------
    name : str
        The name of a component.
    error : str
        Error message.
    **kwds
        Optional keyword arguments.

    Returns
    -------
    str
        The error message.

    """
    cwd = kwds.get('cwd', '.')

    try:
        path_to_error_log = os.path.join(cwd, '_%s.err' % name)
        with open(path_to_error_log, 'r') as err:
            stderr = err.read()
    except IOError:
        stderr = """
(There should be an error log here but I had trouble reading it.)
"""

    return '\n'.join([str(error), stderr, ])


class open_logs(object):
    """Manager for logfile state.

    Parameters
    ----------
    name : str
        Base name of log file.
    log_dir : str, optional
        Path to logging directory (default is current directory).

    """
    def __init__(self, name, log_dir='.'):
        prefix = os.path.abspath(log_dir)
        self._out_log = os.path.join(prefix, '_%s.out' % name)
        self._err_log = os.path.join(prefix, '_%s.err' % name)

    def __enter__(self):
        (self._out, self._err) = (open(self._out_log, 'w'),
                                  open(self._err_log, 'w'))
        return self._out, self._err

    def __exit__(self, type, value, traceback):
        self._out.close()
        self._err.close()


class __redirect_output(object):
    def __init__(self, name, log_dir='.', join=False):
        self._stdout = sys.stdout
        self._stderr = sys.stderr

        prefix = os.path.abspath(log_dir)
        self._out_log = os.path.join(prefix, name)
        if join:
            self._err_log = self._out_log
        else:
            self._err_log = os.path.join(prefix, '%s.err' % name)

    def __enter__(self):
        self._out = open(self._out_log, 'w')
        if self._out_log == self._err_log:
            self._err = self._out
        else:
            self._err = open(self._err_log, 'w')
        sys.stdout = self._out
        sys.stderr = self._err

        return self._out, self._err

    def __exit__(self, type, value, traceback):
        self._out.close()
        if self._out_log != self._err_log:
            self._err.close()

        sys.stdout = self._stdout
        sys.stderr = self._stderr


class __open_reporter(object):
    def __init__(self, id, server, fname):
        self._args = (id, server, fname)

    def __enter__(self):
        self._reporter = Reporter(*self._args)
        self._reporter.start()

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self._reporter.stop()
        self._reporter.join()

        if exc_type is not None:
            reporter = TaskStatus(*self._args)
            # reporter.report('error', reporter.status_with_line_nos(n=40))
            reporter.report('error', 'THERE WAS AN ERROR!!!')


def download_run_tarball(server, uuid, dest_dir='.'):
    """Download tarball of simulation output.

    Parameters
    ----------
    server : str
        URL of API server.
    uuid : str
        The unique UUID for the job.
    dest_dir : str, optional
        Path to download directory (default is current directory).

    Returns
    -------
    str
        Full path to downloaded tarball.

    """
    import requests

    url = os.path.join(server, 'run/download')
    resp = requests.post(url, stream=True,
                         data={
                             'uuid': uuid,
                             'filename': '',
                         })

    if resp.status_code == 200:
        dest_name = os.path.join(dest_dir, uuid + '.tar.gz')
        with open(dest_name, 'wb') as fp:
            for chunk in resp.iter_content(chunk_size=8192):
                if chunk:  # filter out keep-alive new chunks
                    fp.write(chunk)
                    fp.flush()
    else:
        raise DownloadError(resp.status_code, url + ':' + uuid + '.tar.gz')

    return dest_name


def upload_run_tarball(server, tarball):
    """Upload tarball of simulation output.

    Parameters
    ----------
    server : str
        URL of API server.
    tarball : str
        Path to tarball of simulation output.

    Returns
    -------
    str
        Output from `curl`, or None on error.

    """
    # /usr/bin/curl -i -F file=@cb2eb29b-12a8-4979-a961-e283e4f1619d.tar.gz \
    #  http://csdms.colorado.edu/wmt/api-dev/run/upload/
    #  cb2eb29b-12a8-4979-a961-e283e4f1619d

    cmd = [
        '/usr/bin/curl', '-i', '-F',
        'file=@%s' % tarball,
        '%s/run/upload/%s' % (server, 'cb2eb29b-12a8-4979-a961-e283e4f1619d')
    ]

    # resp = subprocess.call(cmd)
    # return '{"checksum":0, "url":"http://csdms.colorado.edu/pub/users/wmt"}'
    try:
        return subprocess.check_output(cmd)
    except Exception as error:
        logger.error(error)
        raise


def report_status(id, url, status, message):
    """Report task status using `requests`.

    Parameters
    ----------
    id : str
        The unique UUID for the job.
    url : str
        URL of API server.
    status : str
        Type of message.
    message : str
        Status message.

    Returns
    -------
    Reponse
        Response from server.

    """
    import requests

    url = os.path.join(server, 'run/update')
    resp = requests.post(url, data={
        'uuid': id,
        'status': status,
        'message': message,
    })
    return resp


class __WmtReporter(object):
    def __init__(self, id, server):
        self._id = id
        self._server = server
        self._curl = os.environ.get('CURL', 'curl')
        log_file = os.path.expanduser('~/.wmt/%s.log' % self.id)
        logging.basicConfig(filename=log_file, filemode='w',
                            level=logging.DEBUG)

    @property
    def id(self):
        return self._id

    @property
    def server(self):
        return self._server

    def report_error(self, message):
        return self.report('error', message)

    def report_success(self, message):
        return self.report('success', message)

    def report(self, status, message):
        import requests

        logger.info('%s: %s' % (status, message))

        url = os.path.join(self.server, 'run/update')
        resp = requests.post(url, data={
            'uuid': self.id,
            'status': status,
            'message': message,
        })

        return resp

    def report_with_curl(self, status, message):
        logger.info('%s: %s' % (status, message))
        cmd = [
            self._curl, '-i', '-F',
            'uuid=%s' % self.id,
            'status=%s' % status,
            'message=\'%s\'' % message,
            '%s/run/update' % self.server,
        ]
        return subprocess.check_output(cmd)


class __TaskStatus(__WmtReporter):
    def __init__(self, id, server, filename, pid=None):
        super(TaskStatus, self).__init__(id, server)

        self._status_file = filename
        self._tail = os.environ.get('TAIL', 'tail')
        self._pid = pid

    @property
    def status_file(self):
        return self._status_file

    def running(self):
        if self._pid:
            try:
                os.kill(self._pid, 0)
            except OSError:
                return False
            else:
                return True
        else:
            return True

    def tail(self, n=10):
        try:
            status = subprocess.check_output(
                [self._tail, '-n{n}'.format(n=n), self.status_file])
        except Exception:
            raise
        else:
            return status

    def wc_l(self):
        try:
            n_lines = subprocess.check_output(
                ['wc', '-l', self.status_file])
        except Exception:
            raise
        else:
            return int(n_lines.split()[0])

    def prepend_to_lines(self, lines, prefix):
        new_lines = []
        for (prefix, line) in zip(lines, prefix):
            new_lines.append(prefix + suffix)
        return new_lines

    def status_with_line_nos(self, n=10):
        last_lines = self.tail(n=n).split(os.linesep)
        n_lines = self.wc_l()

        start_line_no = n_lines - len(last_lines)

        if start_line_no < 0:
            lines = ['Waiting for stdout...']
        else:
            lines = [
                'Last {n} lines from stdout...'.format(n=len(last_lines)),
                '']
            for line_no, line in enumerate(last_lines, start_line_no):
                lines.append('[stdout-{no}] {line}'.format(
                    no=line_no, line=line))

        return os.linesep.join(lines)

    def get_status(self):
        if not self.running():
            raise TaskCompleted()

        status = self.status_with_line_nos()

        # if 'done' in status:
        #     raise TaskCompleted()

        return status

    def report_status(self):
        import time

        while 1:
            time.sleep(10)
            try:
                status = self.get_status()
            except TaskCompleted:
                break
            except Exception as error:
                self.report('running', 'Error getting status (%s)' % error)
                #return
            else:
                # self.report('running', 'Time: %s days' % status)
                self.report('running', '{message}'.format(message=status))

        self.report('success', 'completed')

    def __call__(self):
        self.report_status()


class __Reporter(threading.Thread):
    def __init__(self, id, server, filename, **kwds):
        super(Reporter, self).__init__(**kwds)
        self._stop = threading.Event()
        self._args = (id, server, filename)

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.is_set()

    def run(self):
        import time

        reporter = TaskStatus(*self._args)
        while 1:
            try:
                status = reporter.get_status()
            except TaskCompleted:
                break
            except Exception as error:
                reporter.report('running', 'Error getting status (%s)' % error)
            else:
                reporter.report('running', '{message}'.format(message=status))
            time.sleep(10)

            if self.stopped():
                beak

        reporter.report('success', 'completed')


from .reporter import WmtTaskReporter


class RunTask(WmtTaskReporter):
    """Manager for wmt-exe tasks.

    Parameters
    ----------
    run_id : str
        A unique UUID for a job.
    server : str
        URL of API server.
    exe_env : WmtEnvironment, optional
        Environment variables (default is None).
    exe_dir : str, optional
        Launch directory (default is '~/.wmt').

    """
    def __init__(self, run_id, server, exe_env=None, exe_dir='~/.wmt'):
        super(RunTask, self).__init__(run_id, server)

        self._wmt_dir = os.path.expanduser(exe_dir)
        self._sim_dir = create_user_execution_dir(run_id,
                                                  prefix=self._wmt_dir)
        self._env = exe_env
        self._result = {}

    @property
    def sim_dir(self):
        """Get the simulation directory.

        Returns
        -------
        str
            Path to simulation directory.

        """
        return self._sim_dir

    @property
    def result(self):
        """Get result of simulation.

        Returns
        -------
        dict
            The simulation result.

        """
        return self._result

    def setup(self):
        """Perform pre-simulation tasks."""
        self.report('downloading', 'downloading simulation data')
        dest = self.download_tarball(dest_dir=self._wmt_dir)
        self.report('downloaded', 'downloaded simulation data')

        self.report('unpacking', 'unpacking simulation data')
        self.unpack_tarball(dest)
        self.report('unpacked', 'unpacked simulation data')

    def run(self):
        """Run all components in simulation."""
        for (component, path) in components_to_run(self.sim_dir).items():
            self.report('running', 'running component: %s' % component)
            self.run_component(component, run_dir=path)

    def teardown(self):
        """Perform post-simulation tasks."""
        self.report('packing', 'packing simulation output')
        tarball = self.pack_tarball()
        self.report('packed', 'packed simulation output')

        self.report('uploading', 'uploading simulation output')
        try:
            self.upload_tarball(tarball)
        except Exception as error:
            self.report('uploading', str(error))
        else:
            self.report('uploaded', 'uploaded simulation output')
            self.cleanup()

        self.report_success('done')

    def execute(self):
        """Set up, run, and tear down a simulation."""
        self.setup()
        self.run()
        self.teardown()

    def cleanup(self):
        """Clean up files from a simulation."""
        shutil.rmtree(self._sim_dir, ignore_errors=True)
        tarball = os.path.join(self._wmt_dir, self.id + '.tar.gz')
        os.remove(tarball)

    def run_component(self, name, run_dir='.'):
        """Run a component.

        Parameters
        ----------
        name : str
            Name of component.
        run_dir : str, optional
            Path to run directory (default is current directory).

        """
        with open_logs(name, log_dir=run_dir) as (stdout, stderr):
            run_component(name, stdout=stdout, stderr=stderr, env=self._env,
                          cwd=run_dir)

    def download_tarball(self, dest_dir='.'):
        """Download tarball of simulation output.

        Parameters
        ----------
        dest_dir : str, optional
            Path to destination directory (default is current directory).

        Returns
        -------
        str
            Path to downloaded tarball.

        """
        ans = download_run_tarball(self._server, self.id, dest_dir=dest_dir)
        return ans

    def unpack_tarball(self, path):
        """Extract contents of tarball of simulation output.

        Parameters
        ----------
        path : str
            Path to downloaded tarball.

        """
        with tarfile.open(path) as tar:
            tar.extractall(path=self._wmt_dir)

    def pack_tarball(self):
        """Create tarball of simulation output.

        Returns
        -------
        str
            Path to tarball.

        """
        os.chdir(self._wmt_dir)

        tarball = self.id + '.tar.gz'
        with tarfile.open(tarball, mode='w:gz') as tar:
            tar.add(self.id)

        return os.path.abspath(tarball)

    def upload_tarball(self, path):
        """Upload tarball of simulation output.

        Parameters
        ----------
        path : str
            Path to tarball to upload.

        """
        resp = upload_run_tarball(self._server, path)
        try:
            self._result = json.loads(resp.text)
        except AttributeError:
            self._result = {'resp': resp}


class RunComponentsSeparately(RunTask):
    """Task for running components individually."""
    def run(self):
        for (component, path) in components_to_run(self.sim_dir).items():
            self.report('running', 'running component: %s' % component)
            self.run_component(component, run_dir=path)

    def run_component(self, name, run_dir='.'):
        with open_logs(name, log_dir=run_dir) as (stdout, stderr):
            run_component(name, stdout=stdout, stderr=stderr, env=self._env,
                          cwd=run_dir)


from .reporter import open_reporter, redirect_output


class RunComponentCoupled(RunTask):
    """Task for running components concurrently, in coupled mode."""
    def run(self):
        os.chdir(self.sim_dir)

        import yaml
        from datetime import datetime

        with open(os.path.join(self.sim_dir, 'model.yaml'), 'r') as fp:
            model = yaml.load(fp.read())

        with open('.info.yaml', 'w') as fp:
            info = {
                'start_time': datetime.now().isoformat(),
                'server': self.server,
                'id': self.id,
                'prefix': self.sim_dir,
                'stdout': 'stdout',
                'driver': model['driver'],
            }
            yaml.dump(info, stream=fp, default_flow_style=True)

        # driver = os.path.join(self.sim_dir, model['driver'])
        status_file = os.path.abspath('stdout')
        with redirect_output(status_file, join=True):
            with open_reporter(self.id, self.server, status_file):
                # with open('model.yaml', 'r') as opened:
                #     model = yaml.load(opened.read())
                with open('components.yaml', 'r') as opened:
                    model = Model.load(opened.read())

                self.report('running', 'running model')
                model.go(filename='model.yaml')

        self.report('running', 'finished')
