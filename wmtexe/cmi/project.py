import os


_THIS_DIR = os.path.dirname(__file__)


def empty_bmi_project():
    return {
        'name': 'csdms',
        'language': 'c',
        'interfaces': [{
            'name': 'csdms.core.Bmi',
            'sidl': os.path.join(_THIS_DIR, 'data', 'csdms.core.Bmi.sidl')
        }],
        'bmi': []
    }


def add_bmi_component(project, api):
    project['bmi'].append(api)
