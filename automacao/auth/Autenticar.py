from auth.Usuario import Usuario


class Autenticar:

    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

    def isValido(self):
        lista_usuarios = self._getAll()

        for usuario in lista_usuarios:
            if usuario.login == self.login:
                if usuario.senha == self.senha:
                    return True
        return False

    def _getAll(self):

        return [Usuario('dlduarte', '159753'), Usuario('dduarte', '123')]
