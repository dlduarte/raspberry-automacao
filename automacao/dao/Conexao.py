import sqlite3


class Conexao:

    def __init__(self, caminho):
        conn = sqlite3.connect(caminho + '.db')
        self.conexao = conn

    def getType(self, atributo):
        tipo = type(atributo)
        print(tipo)
        if tipo == str:
            return 'text'
        if tipo == int:
            return 'integer'
        if tipo == float:
            return 'real'
        if tipo == bool:
            return 'integer'

    def create_table(self, entidade):
        try:
            tabela = str(type(entidade).__name__).lower()
            colunas = entidade.__dict__.keys()

            sql = 'CREATE TABLE ' + tabela + '('

            for index, coluna in enumerate(colunas):
                atributo = getattr(entidade, coluna)

                sql += coluna + ' ' + self.getType(atributo)

                if index + 1 < len(colunas):
                    sql += ', '

            sql += ')'

            print(f'EXECUTANDO: {sql}')

            cursor = self.conexao.cursor()
            cursor.execute(sql)

            print('SUCESSO.')
        except Exception as e:
            print(e)

    def inset(self, entidade):
        try:
            tabela = str(type(entidade).__name__).lower()
            valores = entidade.__dict__.values()

            sql = 'INSERT INTO ' + tabela + ' VALUES('

            for index, valor in enumerate(valores):
                if type(valor) == str:
                    sql += '"' + valor + '"'
                else:
                    sql += str(valor)

                if index + 1 < len(valores):
                    sql += ', '

            sql += ')'

            print(f'EXECUTANDO: {sql}')

            cursor = self.conexao.cursor()
            cursor.execute(sql)
            self.conexao.commit()

            print('SUCESSO.')
        except Exception as e:
            print(e)

    def delete(self, entidade, id=None):
        try:
            tabela = str(type(entidade).__name__).lower()
            sql = 'DELETE FROM ' + tabela + ' WHERE '
            colunas = entidade.__dict__.keys()

            if id is None:
                for index, coluna in enumerate(colunas):
                    atributo = getattr(entidade, coluna)

                    if type(atributo) == str:
                        sql += coluna + ' = ' + '"' + atributo + '"'
                    else:
                        sql += coluna + ' = ' + str(atributo)

                    if index + 1 < len(colunas):
                        sql += ' and '
            else:
                sql += 'id = ' + str(id)

            print(f'EXECUTANDO: {sql}')

            cursor = self.conexao.cursor()
            cursor.execute(sql)
            self.conexao.commit()
            print('SUCESSO')
        except Exception as e:
            print(e)

    def update(self):
        pass

    def select(self, entidade, condicoes=None):
        tabela = str(type(entidade).__name__).lower()
        sql = 'SELECT * FROM ' + tabela

        if condicoes is not None:
            sql += ' WHERE '
            for index, condicao in enumerate(condicoes):
                sql += condicao[0] + ' = ' + condicao[1]

                if index + 1 < len(condicoes):
                    sql += ' and '

        print(sql)
        cursor = self.conexao.cursor()
        dados = cursor.execute(sql)
        retorno = []
        for row in dados:
            print(row)
            retorno.append(row)

        return retorno

    def executar(self, sql):
        try:
            cursor = self.conexao.cursor()
            cursor.execute(sql)
            self.conexao.commit()
        except Exception as e:
            print(e)

# conexao = Conexao('automacao')

# conexao.create_table(Usuarios())
# conexao.inset(Usuarios(1, 'david', '123456'))
# conexao.inset(Usuarios(2, 'dduarte', '159753'))
# conexao.inset(Usuarios(3, 'dld2019', '2019'))
