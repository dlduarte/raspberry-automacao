import os
import platform

from dao.Conexao import Conexao
from dao.entidades.Usuarios import Usuarios

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

try:
    conexao = Conexao('automacao')

    # Crio a tabela de usuários e adiciono o usuário admin á ela.
    conexao.create_table(Usuarios())
    conexao.inset(Usuarios(1, 'admin', '@Admin'))
except Exception as e:
    print(e)
