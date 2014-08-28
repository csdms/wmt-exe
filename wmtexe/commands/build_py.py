from setuptools.command.build_py import build_py


class Build(build_py):
    #def build_module(self, module, module_file, package):
    #    build_py.build_module(module, module_file, package)
    #    with open('wmt-exe-default.py', 'w') as f:
    #        f.write('DEFAULTS = {}')
    description = 'Build WMT py files'
    user_options = [
        ('option', None, 'Option'),
    ] + build_py.user_options

    def initialize_options(self):
        raise RuntimeError('error')
        print '*****************'
        self.option = None
        build_py.initialize_options(self)

    def run(self):
        raise RuntimeError('error')
        print '*****************'
        build_py.run(self)
        #self.build_module('wmt-exe-default.py', 'wmtexe/defaults.py', 'wmtexe')
        print '*****************'
