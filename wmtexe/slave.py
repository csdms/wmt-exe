"""Tools to initiate and monitor tasks in a wmt-exe environment."""
import os
import argparse
import tarfile
import subprocess
import shutil


def _upload_run_tarball(server, tarball):
    import requests
    from requests_toolbelt import MultipartEncoder

    url = os.path.join(server, 'run/upload')
    with open(tarball, 'r') as fp:
        m = MultipartEncoder(fields={
            'file': (tarball, fp, 'application/x-gzip')})
        resp = requests.post(url, data=m,
                             headers={'Content-Type': m.content_type})

    if resp.status_code != 200:
        raise UploadError(resp.status_code, tarball)
    else:
        return resp


class Slave(object):
    """Task slave for a wmt-exe environment.

    Parameters
    ----------
    url : str
        URL of API server.
    env : dict, optional
        WMT environment variables (default is None).
    dir : str, optional
        The working directory for the job (default is current directory). 

    """
    def __init__(self, url, env=None, dir='.'):
        self._url = url
        self._tasks = {}

    @property
    def url(self):
        """Get the API server URL.

        Returns
        -------
        str
            The API server URL.

        """
        return self._url

    def start_task(self, id, env=None, dir='.'):
        """Start tasks for the given job id.

        Parameters
        ----------
        id : str
            The unique UUID for the job.
        env : dict, optional
            WMT environment variables (default is None).
        dir : str, optional
            The working directory for the job (default is current directory). 

        Returns
        -------
        Reponse
            Response from server.

        """
        from .task import RunComponentCoupled

        self._tasks[id] = RunComponentCoupled(id, self.url, exe_env=env,
                                              exe_dir=dir)
        return self._tasks[id].execute()

    def report_error(self, id, message):
        """Report errors from a job.

        Parameters
        ----------
        id : str
            The unique UUID for the job.
        message : str
            The error message.

        Returns
        -------
        Reponse
            Response from server.

        """
        return self.report(id, 'error', message)

    def report_success(self, id, message):
        """Report job success.

        Parameters
        ----------
        id : str
            The unique UUID for the job.
        message : str
            The success message.

        Returns
        -------
        Reponse
            Response from server.

        """
        return self.report(id, 'success', message)

    def report(self, id, status, message):
        """Report task status using `requests`.

        Parameters
        ----------
        id : str
            The unique UUID for the job.
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

        url = os.path.join(self.url, 'run/update')
        resp = requests.post(url, data={
            'uuid': id,
            'status': status,
            'message': message,
        })

        return resp
