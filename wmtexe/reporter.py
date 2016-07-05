"""Logging and reporting tools for a wmt-exe environment."""

import os
import sys
import threading
import time
import logging
import subprocess

import yaml
import requests


logger = logging.getLogger(__name__)
"""Logger : Instance of Logging class."""


class TaskCompleted(Exception):
    """Exception thrown when a wmt-exe task completes."""
    pass


class redirect_output(object):
    """Manager for output and error logs.

    Parameters
    ----------
    name : str
        Log file name.
    log_dir : str, optional
        Path to logging directory (default is current directory).
    join : bool, optional
        Set to True to combine logs (default is False).

    """
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


class open_reporter(object):
    """Manager for a reporter in a wmt-exe environment.

    Parameters
    ----------
    id : str
        A unique UUID for a job.
    server : str
        URL of API server.
    fname : str
        Name of status file.

    """
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
            reporter.report('error', reporter.status_with_line_nos(n=40))


def add_line_numbers(lines, start=0, fn=None):
    """Prefix lines with numbers.

    Parameters
    ----------
    lines : list or list-like of str
        Lines to be prefixed with a number.
    start : int, optional
        The index at which line numbers start (default is 0).
    fn : str, optional
        File name to prepend to line number (default is None).

    Returns
    -------
    list
        Lines prefixed with numbers.

    """
    if fn:
        fmt_string = '[{fn}-{{ln}}] {{line}}'.format(fn=fn)
    else:
        fmt_string = '[{ln}] {line}'

    with_prefix = []
    for line_no, line in enumerate(lines, start):
        with_prefix.append(fmt_string.format(ln=line_no, line=line))

    return with_prefix


def wc_l(fname, with_wc='wc'):
    """Count the lines in a file.

    Parameters
    ----------
    fname : str
        File name.
    with_wc : str, optional
        The 'wc' command to use (default is `wc`).

    Returns
    -------
    int
        Number of lines in file, or None on error.

    """
    try:
        n_lines = subprocess.check_output(
            [with_wc, '-l', fname])
    except Exception:
        raise
    else:
        return int(n_lines.split()[0])


def tail(fname, n=10, with_tail='tail'):
    """Get the last lines in a file.

    Parameters
    ----------
    fname : str
        File name.
    n : int, optional
        Number of lines to get (default is 10).
    with_tail : str, optional
        The 'tail' command to use (default is `tail`).

    Returns
    -------
    str
        The last lines in file, or None on error.

    """
    fname = os.path.abspath(fname)
    try:
        lines = subprocess.check_output(
            [with_tail, '-n{n}'.format(n=n), fname])
    except subprocess.CalledProcessError:
        raise RuntimeError('Unable to get status. Please try again.')
    except Exception:
        raise
    else:
        return lines.strip()


def tail_with_line_numbers(fname, n=10, with_tail='tail', with_wc='wc'):
    """Get the last lines in a file, with line numbers.

    Parameters
    ----------
    fname : str
        File name.
    n : int, optional
        Number of lines to get (default is 10).
    with_tail : str, optional
        The 'tail' command to use (default is `tail`).
    with_wc : str, optional
        The 'wc' command to use (default is `wc`).

    Returns
    -------
    list
        The last lines in file, prefixed with numbers.

    """
    total_lines = wc_l(fname, with_wc=with_wc)

    if total_lines > 0:
        last_lines = tail(fname, n=n, with_tail=with_tail).split(os.linesep)

        start_line_no = total_lines - len(last_lines)

        return add_line_numbers(last_lines, start_line_no)
    else:
        return [fname]


class Reporter(threading.Thread):
    """Event reporter for wmt-exe tasks.

    Parameters
    ----------
    id : str
        A unique UUID for a job.
    server : str
        URL of API server.
    fname : str
        Name of status file.
    **kwds
        Arbitrary keyowrd arguments.

    """
    def __init__(self, id, server, filename, **kwds):
        super(Reporter, self).__init__(**kwds)
        self._stop = threading.Event()
        self._args = (id, server, filename)

    def stop(self):
        """Stop reporting on a task."""
        self._stop.set()

    def stopped(self):
        """Check whether reporting has stopped.

        Returns
        -------
        bool
            True if reporting has stopped.

        """
        return self._stop.is_set()

    def run(self):
        """Start reporting on a task."""
        import time

        reporter = TaskStatus(*self._args)
        while 1:
            try:
                status = reporter.get_status()
            except TaskCompleted:
                break
            except Exception as error:
                import traceback
                reporter.report(
                    'running',
                    '(2) Error getting status ({err})\n{tb}'.format(
                        err=error, tb=traceback.format_exc()))
            else:
                reporter.report('running', '{message}'.format(message=status))
            time.sleep(2)

            if self.stopped():
                break

        reporter.report('success', 'completed')


class WmtTaskReporter(object):
    """Reporter for wmt-exe tasks.

    Parameters
    ----------
    id : str
        A unique UUID for a job.
    server : str
        URL of API server.

    """
    def __init__(self, id, server):
        self._id = id
        self._server = server
        self._curl = os.environ.get('CURL', 'curl')
        log_file = os.path.expanduser('~/.wmt/%s.log' % self.id)
        logging.basicConfig(filename=log_file, filemode='w',
                            level=logging.DEBUG)

    @property
    def id(self):
        """Get id of task.

        Returns
        -------
        str
            The task id.

        """
        return self._id

    @property
    def server(self):
        """Get server URL.

        Returns
        -------
        str
            The server URL.

        """
        return self._server

    def report_error(self, message):
        """Report an error.

        Parameters
        ----------
        message : str
            Error message.

        Returns
        -------
        Reponse
            Response from server.

        """
        return self.report('error', message)

    def report_success(self, message):
        """Report successful task completion.

        Parameters
        ----------
        message : str
            Success message.

        Returns
        -------
        Reponse
            Response from server.

        """
        return self.report('success', message)

    def report(self, status, message):
        """Report task status using `requests`.

        Parameters
        ----------
        status : str
            Type of report.
        message : str
            Message for report.

        Returns
        -------
        Reponse
            Response from server.

        """
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
        """Report task status using `curl`.

        Parameters
        ----------
        status : str
            Type of report.
        message : str
            Message for report.

        Returns
        -------
        str
            Response from server.

        """
        logger.info('%s: %s' % (status, message))
        cmd = [
            self._curl, '-i', '-F',
            'uuid=%s' % self.id,
            'status=%s' % status,
            'message=\'%s\'' % message,
            '%s/run/update' % self.server,
        ]
        return subprocess.check_output(cmd)


from datetime import datetime


def load_status_from_lines(lines):
    """Load task status from strings.

    Parameters
    ----------
    lines : list or list-like of str
        List of lines containing task status information.

    Returns
    -------
    dict
        The task status, or an empty dict on error.

    """
    status = {}
    for line in lines[::-1]:
        try:
            status = yaml.load(line)
        except yaml.YAMLError:
            pass
        else:
            if isinstance(status, dict):
                break

    if not isinstance(status, dict):
        return {}
    else:
        return status


def read_wmt_status(fname):
    """Read the WMT status from a file.

    Parameters
    ----------
    fname : str
        WMT status file.

    Returns
    -------
    dict
        The task status, or an empty dict on error.

    """
    status = {}

    try:
        status_lines = tail(fname, n=2).split(os.linesep)
    except RuntimeError:
        status = {}
    else:
        status = load_status_from_lines(status_lines)

    return status


class TaskStatus(WmtTaskReporter):
    """Task status manager for a wmt-exe environment.

    Parameters
    ----------
    id : str
        A unique UUID for a job.
    server : str
        URL of API server.
    filename : str
        Name of status file.
    pid : str, optional
        Process id (default is None).
    prefix : str, optional
        Path to base directory (default is current directory).

    """
    def __init__(self, id, server, filename, pid=None, prefix='.'):
        super(TaskStatus, self).__init__(id, server)

        self._status_file = filename
        self._prefix = os.path.abspath(prefix)
        self._tail = os.environ.get('TAIL', 'tail')
        self._pid = pid
        self._start_time = datetime.now()

    @property
    def status_file(self):
        """Get the status file.

        Returns
        -------
        str
            Name of status file.

        """
        return self._status_file

    @property
    def elapsed(self):
        """Get the elapsed time in the simulation.

        Returns
        -------
        float
            The elapsed time, in seconds.

        """
        return (datetime.now() - self._start_time).total_seconds()

    def running(self):
        """Test whether the simulation is running.

        Returns
        -------
        bool
            True if simulation is running.

        """
        if self._pid:
            try:
                os.kill(self._pid, 0)
            except OSError:
                return False
            else:
                return True
        else:
            return True

    def status_with_line_nos(self, n=10):
        """Get status prepended with line numbers.

        Parameters
        ----------
        n : int, optional
            Number of lines to display.

        Returns
        -------
        str
            The status as a YAML stream.

        """
        lines = tail_with_line_numbers(self.status_file, n=n)
        if len(lines) == 0:
            dots = '.' * (int(self.elapsed  / 10) % 10)
            lines = ['Waiting for stdout{dots}'.format(dots=dots)]
        else:
            lines = [
                'Last {n} lines from stdout:'.format(n=len(lines)),
                ''] + lines

        status = dict(stdout=os.linesep.join(lines),
                      time_elapsed=self.elapsed)
        status.update(read_wmt_status(os.path.join(self._prefix, '_time.txt')))

        return yaml.dump(status)
        # return os.linesep.join(lines)

    def get_status(self):
        """Get task status.

        Returns
        -------
        str
            The status as a YAML stream.

        """
        # if not self.running():
        #     raise TaskCompleted()
        return self.status_with_line_nos()

    def report_status(self):
        """Report task status at regular intervals until task completes.

        Returns
        -------
        Reponse
            Response from server.

        """
        import time

        while 1:
            time.sleep(2)
            try:
                status = self.get_status()
            except TaskCompleted:
                break
            except Exception as error:
                self.report('running', '(1) Error getting status (%s)' % error)
                #return
            else:
                # self.report('running', 'Time: %s days' % status)
                self.report('running', '{message}'.format(message=status))

        self.report('success', 'completed')

    def __call__(self):
        self.report_status()
