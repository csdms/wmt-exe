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
    def __init__(self, url, env=None, dir='.'):
        self._url = url
        self._tasks = {}

    @property
    def url(self):
        return self._url

    def start_task(self, id, env=None, dir='.'):
        from .task import RunComponentCoupled

        self._tasks[id] = RunComponentCoupled(id, self.url, exe_env=env,
                                              exe_dir=dir)
        return self._tasks[id].execute()

    def report_error(self, id, message):
        return self.report(id, 'error', message)

    def report_success(self, id, message):
        return self.report(id, 'success', message)

    def report(self, id, status, message):
        import requests

        url = os.path.join(self.url, 'run/update')
        resp = requests.post(url, data={
            'uuid': id,
            'status': status,
            'message': message,
        })

        return resp
