import os
import sys
import argparse
import urlparse
import urllib2
import tarfile
import subprocess
import shutil
import json


from cmt.component.model import Model
from cmt.framework.services import register_component_classes

register_component_classes([
    'csdms.model.Sedflux2d.Sedflux2d',
    'csdms.model.Sedflux3d.Sedflux3d',
    'csdms.model.Child.Child',
    'csdms.model.Hydrotrend.Hydrotrend',
    'csdms.model.Plume.Plume',
    'csdms.model.Avulsion.Avulsion',
    'csdms.model.Cem.Cem',
    'csdms.model.Waves.Waves',
    'cmt.services.constant.constant.River',
])


_WMT_PREFIX = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
_WMT_ETC = os.path.join(_WMT_PREFIX, 'etc', 'wmt')
_WMT_SHARE = os.path.join(_WMT_PREFIX, 'share', 'wmt')

class Error(Exception):
    pass


class UploadError(Error):
    def __init__(self, code, file):
        self._code = code
        self._file = file

    def __str__(self):
        return '%s: unable to upload (error %d)' % (self._file, self._code)


class DownloadError(UploadError):
    def __str__(self):
        return '%s: unable to download (error %d)' % (self._file, self._code)


class ComponentRunError(Error):
    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return self._msg


def load_environment(yaml_file):
    import yaml
    import types
    from collections import defaultdict

    env = defaultdict(list)

    modules = yaml.load_all(open(yaml_file, 'r').read())

    for module in modules:
        if 'paths' in module:
            for (name, paths) in module['paths'].items():
                env[name] = paths + env[name]
        if 'vars' in module:
            for (name, value) in module['vars'].items():
                env[name] = value

    for (name, value) in env.items():
        if isinstance(value, types.ListType):
            env[name] = os.pathsep.join(value)
        else:
            env[name] = str(value)

    return env


def download_run_tarball(server, uuid, dir='.'):
    import requests

    url = os.path.join(server, 'run/download')
    resp = requests.post(url, stream=True,
                         data={
                             'uuid': uuid,
                             'filename': '',
                         })

    if resp.status_code == 200:
        dest_name = os.path.join(dir, uuid + '.tar.gz')
        with open(dest_name, 'wb') as fp:
            for chunk in resp.iter_content():
                if chunk: # filter out keep-alive new chunks
                    fp.write(chunk)
                    fp.flush()
    else:
        raise DownloadError(resp.status_code, url + ':' + uuid + '.tar.gz')

    return dest_name


def update_run_status(server, uuid, status, message):
    import requests

    url = os.path.join(server, 'run/update')
    resp = requests.post(url, data={
        'uuid': uuid,
        'status': status,
        'message': message,
    })

    return resp


def update_run_status_with_curl(server, uuid, status, message):
    cmd = [
        '/usr/bin/curl', '-i', '-F',
        'uuid=%s' % uuid,
        'status=%s' % status,
        'message=\'%s\'' % message,
        '%s/run/update' % server,
    ]
    return subprocess.check_output(cmd)


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


def upload_run_tarball(server, tarball):
    #/usr/bin/curl -i -F file=@cb2eb29b-12a8-4979-a961-e283e4f1619d.tar.gz http://csdms.colorado.edu/wmt/api-dev/run/upload/cb2eb29b-12a8-4979-a961-e283e4f1619d

    cmd = [
        '/usr/bin/curl', '-i', '-F',
        'file=@%s' % tarball,
        '%s/run/upload/%s' % (server, 'cb2eb29b-12a8-4979-a961-e283e4f1619d')
    ]

    #resp = subprocess.call(cmd)
    #return '{"checksum":0, "url":"http://csdms.colorado.edu/pub/users/wmt"}'
    return subprocess.check_output(cmd)


def generate_error_message(name, error, **kwds):
    cwd = kwds.get('cwd', '.')

    try:
        path_to_error_log = os.path.join(cwd, '_%s.err' % name)
        #with open('_%s.err' % name, 'r') as err:
        with open(path_to_error_log, 'r') as err:
            stderr = err.read()
    except IOError:
        stderr = """
(There should be an error log here but I had trouble reading it.)
"""

    return '\n'.join([str(error), stderr, ])


def create_user_execution_dir(id, prefix='~/.wmt'):
    path = os.path.join(prefix, id)

    try:
        os.makedirs(path)
    except os.error:
        if os.path.isdir(path):
            pass
        else:
            raise

    return path


def dir_contains_run_script(path):
    return os.path.isfile(os.path.join(path, 'run.sh'))


def components_to_run(path):
    components = {}

    for item in os.listdir(path):
        if dir_contains_run_script(os.path.join(path, item)):
            components[item] = os.path.abspath(os.path.join(path, item))

    return components


def run_component(name, **kwds):
    try:
        subprocess.check_call(['/bin/bash', 'run.sh'], **kwds)
    except subprocess.CalledProcessError as error:
        raise ComponentRunError(generate_error_message(name, error, **kwds))


class open_logs(object):
    def __init__(self, name, dir='.'):
        prefix = os.path.abspath(dir)
        self._out_log = os.path.join(prefix, '_%s.out' % name)
        self._err_log = os.path.join(prefix, '_%s.err' % name)

    def __enter__(self):
        (self._out, self._err) = (open(self._out_log, 'w'),
                                  open(self._err_log, 'w'))
        return (self._out, self._err)

    def __exit__(self, type, value, traceback):
        self._out.close()
        self._err.close()


import threading


def ping_server(server, uuid, status_file):
    import time
    while 1:
        time.sleep(10)
        try:
            time_str = subprocess.check_output(['/usr/bin/tail', '-n1', status_file])
            status = 'Time: %s days' % time_str
        except Exception as error:
            #status = 'no status...'
            return
        else:
            if 'done' in status:
                return
        
        try:
            update_run_status(server, uuid, 'running', status)
        except:
            pass


def ping(server, uuid):
    update_run_status(server, uuid, 'running', 'ping')


class WmtSlave(object):
    def __init__(self, id, server, env=None, dir='~/.wmt'):
        self._id = id
        self._wmt_dir = os.path.expanduser(dir)
        self._sim_dir = create_user_execution_dir(id, prefix=self._wmt_dir)
        self._server = server
        self._env = env
        self._result = {}

    @property
    def id(self):
        return self._id

    @property
    def sim_dir(self):
        return self._sim_dir

    @property
    def result(self):
        return self._result

    def setup(self):
        self.update_status('downloading', 'downloading simulation data')
        dest = self.download_tarball(dir=self._wmt_dir)

        self.update_status('unpacking', 'unpacking simulation data')
        self.unpack_tarball(dest)

    def run(self):
        for (component, path) in components_to_run(self.sim_dir).items():
            self.update_status('running', 'running component: %s' % component)
            self.run_component(component, dir=path)

    def teardown(self):
        self.update_status('packing', 'packing simulation output')
        tarball = self.pack_tarball()

        self.update_status('uploading', 'uploading simulation output')
        #import shutil
        #try:
        #    os.rmdir(os.path.expanduser(os.path.join('~/.wmt', self.id)))
        #except OSError:
        #    pass
        #shutil.move(self._sim_dir, '/home/huttone/.wmt/')
        try:
            self.upload_tarball(tarball)
        except:
            pass

        self.update_status('success', 'done')
        #self.update_status('cleaning', 'cleaning up')
        #self.cleanup()

    def execute(self):
        self.setup()
        self.run()
        self.teardown()

    def cleanup(self):
        shutil.rmtree(self._sim_dir, ignore_errors=True)
        tarball = os.path.join(self._wmt_dir, self.id + '.tar.gz')
        os.remove(tarball)

    def update_status(self, status, message):
        update_run_status(self._server, self.id, status, message)

    def run_component(self, name, dir='.'):
        with open_logs(name, dir=dir) as (stdout, stderr):
            run_component(name, stdout=stdout, stderr=stderr, env=self._env,
                          cwd=dir)

    def download_tarball(self, dir='.'):
        ans = download_run_tarball(self._server, self.id, dir=dir)
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


class RunComponentsSeparately(WmtSlave):
    def run(self):
        for (component, path) in components_to_run(self.sim_dir).items():
            self.update_status('running', 'running component: %s' % component)
            self.run_component(component, dir=path)

    def run_component(self, name, dir='.'):
        with open_logs(name, dir=dir) as (stdout, stderr):
            run_component(name, stdout=stdout, stderr=stderr, env=self._env,
                          cwd=dir)

class RunComponentCoupled(WmtSlave):
    def run(self):
        os.chdir(self.sim_dir)

        import yaml
        with open('model.yaml', 'r') as opened:
            model = yaml.load(opened.read())
        status_file = os.path.abspath(os.path.join(model['driver'], '_time.txt'))

        timer = threading.Thread(target=ping_server, args=[self._server, self.id, status_file])
        timer.start()

        with open('components.yaml', 'r') as opened:
            model = Model.load(opened.read())
        #with open('run.yaml', 'r') as opened:
        #    run = yaml.load(opened.read())Model.load(opened.read())
        self.update_status('running', 'running model')
        #with open(os.path.join(self.sim_dir, 'wmt.out'), 'w') as out:
        #    sys.stdout = out
        #    sys.stderr = out
        model.go(file='model.yaml')
        #model.go('plume', 2.)
        #timer.cancel()
        self.update_status('running', 'finished')


def launch(id, url, dir='~/.wmt', env={}):
    #env = {
    #    'PATH': os.pathsep.join([
    #        '/home/csdms/wmt/internal/Canopy_64bit/User',
    #        '/home/csdms/wmt/internal/bin',
    #        '/bin',
    #        '/usr/bin',
    #    ]),
    #    'LD_LIBRARY_PATH': '/home/csdms/wmt/internal/lib',
    #}

    task = RunComponentCoupled(id, url, env=env, dir=dir)
    task.execute()

    return task.result


class EnsureHttps(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        import urlparse
        o = urlparse.urlsplit(values)
        url = urlparse.urlunsplit(('https', o.netloc, o.path, '', ''))
        setattr(namespace, self.dest, url)


def main():
    import traceback

    parser = argparse.ArgumentParser()
    parser.add_argument('id', help='run ID')
    parser.add_argument('--server-url',
                        default='https://csdms.colorado.edu/wmt-server',
                        action=EnsureHttps, help='URL of WMT server')
    parser.add_argument('--exec-dir', default=os.path.expanduser('~/.wmt'),
                        help='path to execution directory')
    parser.add_argument('--env', default=os.path.join(_WMT_ETC, 'environ.yaml'),
                        help='path to environment file')

    args = parser.parse_args()

    env = load_environment(args.env)

    try:
        result = launch(args.id, args.server_url, dir=args.exec_dir,
                        env=env)
    except Error as error:
        update_run_status(args.server_url, args.id, 'error', str(error))
        print error
    except Exception as error:
        update_run_status(args.server_url, args.id, 'error',
                          traceback.format_exc())
        print error
    else:
        #message = '<a href=%s>pickup</a>' % result['url']
        message = 'pickup'
        update_run_status(args.server_url, args.id, 'success',
                          'simulation is complete and available for %s' % message)
        print 'success'


if __name__ == '__main__':
    main()
