import os
import platform

from setuptools.sandbox import _execfile

dependencias_faltantes = []
pip = 'pip'


if platform.system() == 'Linux':
    pip = 'pip3'

try:
    import flask
except ImportError as e:
    print(e)
    dependencias_faltantes.append('flask')

try:
    import flask_restful
except ImportError as e:
    print(e)
    dependencias_faltantes.append('flask-restful')

try:
    import flask_cors
except ImportError as e:
    print(e)
    dependencias_faltantes.append('flask_cors')

print('Dependencias faltantes: ')
print(dependencias_faltantes)

for dep in dependencias_faltantes:
    comando = pip + ' install ' + dep
    print(comando)

    try:
        os.system(comando)
    except Exception or BaseException:
        pass

os.system('python Server.py')

