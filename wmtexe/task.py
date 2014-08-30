import os
import subprocess
import tarfile
import shutil
import json
import threading

from cmt.component.model import Model
from cmt.framework.services import register_component_classes


register_component_classes([
    'csdms.model.Sedflux2d.Sedflux2d',
    'csdms.model.Sedflux3d.Sedflux3d',
    'csdms.model.Child.Child',
    'csdms.model.Hydrotrend.Hydrotrend',
    #'csdms.model.Plume.Plume',
    #'csdms.model.Avulsion.Avulsion',
    #'csdms.model.Cem.Cem',
    #'csdms.model.Waves.Waves',
    #'cmt.services.constant.constant.River',
])


class TaskError(Exception):
    pass


class TaskCompleted(Exception):
    pass


class UploadError(TaskError):
    def __init__(self, code, filename):
        self._code = code
        self._file = filename

    def __str__(self):
        return '%s: unable to upload (error %d)' % (self._file, self._code)


class DownloadError(UploadError):
    def __str__(self):
        return '%s: unable to download (error %d)' % (self._file, self._code)


class ComponentRunError(TaskError):
    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return self._msg


def create_user_execution_dir(run_id, prefix='~/.wmt'):
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
    components = {}

    for item in os.listdir(path):
        if dir_contains_run_script(os.path.join(path, item)):
            components[item] = os.path.abspath(os.path.join(path, item))

    return components


def dir_contains_run_script(path):
    return os.path.isfile(os.path.join(path, 'run.sh'))


def run_component(name, **kwds):
    try:
        subprocess.check_call(['/bin/bash', 'run.sh'], **kwds)
    except subprocess.CalledProcessError as error:
        raise ComponentRunError(generate_error_message(name, error, **kwds))


def generate_error_message(name, error, **kwds):
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


def download_run_tarball(server, uuid, dest_dir='.'):
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
            for chunk in resp.iter_content():
                if chunk:  # filter out keep-alive new chunks
                    fp.write(chunk)
                    fp.flush()
    else:
        raise DownloadError(resp.status_code, url + ':' + uuid + '.tar.gz')

    return dest_name


def upload_run_tarball(server, tarball):
    # /usr/bin/curl -i -F file=@cb2eb29b-12a8-4979-a961-e283e4f1619d.tar.gz \
    #  http://csdms.colorado.edu/wmt/api-dev/run/upload/
    #  cb2eb29b-12a8-4979-a961-e283e4f1619d

    cmd = [
        '/usr/bin/curl', '-i', '-F',
        'file=@%s' % tarball,
        '%s/run/upload/%s' % (server, 'cb2eb29b-12a8-4979-a961-e283e4f1619d')
    ]

    #resp = subprocess.call(cmd)
    #return '{"checksum":0, "url":"http://csdms.colorado.edu/pub/users/wmt"}'
    return subprocess.check_output(cmd)


def report_status(id, url, status, message):
    import requests

    url = os.path.join(server, 'run/update')
    resp = requests.post(url, data={
        'uuid': id,
        'status': status,
        'message': message,
    })
    return resp


class Task(object):
    def __init__(self, id, server):
        self._id = id
        self._server = server
        self._curl = os.environ.get('CURL', 'curl')

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

        url = os.path.join(self.server, 'run/update')
        resp = requests.post(url, data={
            'uuid': self.id,
            'status': status,
            'message': message,
        })
        return resp

    def report_with_curl(self, status, message):
        cmd = [
            self._curl, '-i', '-F',
            'uuid=%s' % self.id,
            'status=%s' % status,
            'message=\'%s\'' % message,
            '%s/run/update' % self.server,
        ]
        return subprocess.check_output(cmd)



class TaskStatus(Task):
    def __init__(self, id, server, filename):
        super(TaskStatus, self).__init__(id, server)

        self._status_file = filename
        self._tail = os.environ.get('TAIL', 'tail')

    @property
    def status_file(self):
        return self._status_file

    def get_status(self):
        try:
            time_str = subprocess.check_output(
                [self._tail, '-n1', self.status_file])
        except Exception:
            raise

        if 'done' in time_str:
            raise TaskCompleted()

        return time_str

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
                self.report('running', 'Time: %s days' % status)

        self.report('completed', 'completed')

    def __call__(self):
        self.report_status()


class RunTask(Task):
    def __init__(self, run_id, server, exe_env=None, exe_dir='~/.wmt'):
        super(RunTask, self).__init__(run_id, server)

        self._wmt_dir = os.path.expanduser(exe_dir)
        self._sim_dir = create_user_execution_dir(run_id,
                                                  prefix=self._wmt_dir)
        self._env = exe_env
        self._result = {}

    @property
    def sim_dir(self):
        return self._sim_dir

    @property
    def result(self):
        return self._result

    def setup(self):
        self.report('downloading', 'downloading simulation data')
        dest = self.download_tarball(dest_dir=self._wmt_dir)

        self.report('unpacking', 'unpacking simulation data')
        self.unpack_tarball(dest)

    def run(self):
        for (component, path) in components_to_run(self.sim_dir).items():
            self.report('running', 'running component: %s' % component)
            self.run_component(component, run_dir=path)

    def teardown(self):
        self.report('packing', 'packing simulation output')
        tarball = self.pack_tarball()

        self.report('uploading', 'uploading simulation output')
        try:
            self.upload_tarball(tarball)
        except:
            pass

        self.report_success('done')

    def execute(self):
        self.setup()
        self.run()
        self.teardown()

    def cleanup(self):
        shutil.rmtree(self._sim_dir, ignore_errors=True)
        tarball = os.path.join(self._wmt_dir, self.id + '.tar.gz')
        os.remove(tarball)

    def run_component(self, name, run_dir='.'):
        with open_logs(name, log_dir=run_dir) as (stdout, stderr):
            run_component(name, stdout=stdout, stderr=stderr, env=self._env,
                          cwd=run_dir)

    def download_tarball(self, dest_dir='.'):
        ans = download_run_tarball(self._server, self.id, dest_dir=dest_dir)
        return ans

    def unpack_tarball(self, path):
        with tarfile.open(path) as tar:
            tar.extractall(path=self._wmt_dir)

    def pack_tarball(self):
        os.chdir(self._wmt_dir)

        tarball = self.id + '.tar.gz'
        with tarfile.open(tarball, mode='w:gz') as tar:
            tar.add(self.id)

        return os.path.abspath(tarball)

    def upload_tarball(self, path):
        resp = upload_run_tarball(self._server, path)
        self._result = json.loads(resp.text)


class RunComponentsSeparately(RunTask):
    def run(self):
        for (component, path) in components_to_run(self.sim_dir).items():
            self.report('running', 'running component: %s' % component)
            self.run_component(component, run_dir=path)

    def run_component(self, name, run_dir='.'):
        with open_logs(name, log_dir=run_dir) as (stdout, stderr):
            run_component(name, stdout=stdout, stderr=stderr, env=self._env,
                          cwd=run_dir)


class RunComponentCoupled(RunTask):
    def run(self):
        os.chdir(self.sim_dir)

        import yaml
        with open('model.yaml', 'r') as opened:
            model = yaml.load(opened.read())
        status_file = os.path.abspath(os.path.join(model['driver'],
                                                   '_time.txt'))

        status = TaskStatus(self.id, self.server, status_file)
        timer = threading.Thread(target=status)
        timer.start()

        with open('components.yaml', 'r') as opened:
            model = Model.load(opened.read())
        self.report('running', 'running model')
        model.go(file='model.yaml')
        self.report('running', 'finished')
