from dao.entidades.Usuarios import Usuarios
from dao.Conexao import Conexao


class Autenticar:

    def __init__(self, login, senha):
        self.login = '"' + login + '"'
        self.senha = '"' + senha + '"'

    def isValido(self):
        conexao = Conexao('automacao')
        usuarios = conexao.select(Usuarios(), [['login', self.login],['senha', self.senha]])

        if len(usuarios) == 1:
            print('AUTENTICAÇÃO ACEITA')
            return True
        print('AUTENTICAÇÃO RECUSADA')
        return False
