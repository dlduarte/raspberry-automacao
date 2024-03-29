from flask import Flask, request, abort, jsonify, render_template, Response, json, redirect, url_for
from flask_restful import Resource, Api
from flask_cors import CORS
import traceback

from auth.Autenticar import Autenticar
from devices.Serialize import Serialize
#from devices.Gpio import Gpio

app = Flask(__name__)
api = Api(app)
CORS(app, support_credentials=True)


class Index(Resource):
    def get(self):
        try:
            return Response(
                render_template(
                    "index.html",
                    mimetype='text/html'
                )
            )
        except Exception as e:
            traceback.print_exc(e)
            return f'Erro: {e}'


class Painel(Resource):
    def get(self):
        try:
            return redirect(url_for('index'))
        except Exception as e:
            traceback.print_exc(e)
            return f'Erro: {e}'

    def post(self):
        try:
            if 'user' in request.form and 'psw' in request.form:
                user = request.form['user']
                psw = request.form['psw']

                print(f'LOGIN: {user} SENHA: {psw} IP: {request.environ["REMOTE_ADDR"]}')

                auth = Autenticar(user, psw)

                if auth.isValido():
                    return Response(
                        render_template(
                            "painel.html",
                            mimetype='text/html',
                            Grupos=Serialize.desserializar()
                        )
                    )
                else:
                    return redirect(url_for('index', erro='Usuário ou senha inválidos!'))

            return redirect(url_for('index'))

        except Exception as e:
            traceback.print_exc(e)
            return f'Erro: {e}'


class Status(Resource):
    def get(self):
        try:
            return Serialize.desserializar(True)
        except Exception as e:
            traceback.print_exc(e)
            return f'Erro: {e}'


class Comando(Resource):
    def post(self):
        try:
            if not request.json or 'device' not in request.json:
                abort(400)

            dados = json.loads(request.json)

            pino = dados['device']
            saida = dados['saida']
            grupo_ = None
            sigla = ''
            status = 'off'

            # Chamada classe manipuladora GPIO
            #Gpio(pino, saida)

            grupos = Serialize.desserializar()

            for grupo in grupos:
                for device in grupo.devices:
                    if device.pino == pino:
                        grupo_ = grupo
                        device.saida = saida
                        sigla = grupo.sigla
                        break

                if grupo == grupo_:
                    grupo.status = 'off'
                    for device in grupo.devices:
                        if device.saida:
                            status = 'on'
                            grupo.status = 'on'
                            break

            # Serializo a mudança de estado
            Serialize.serializar(grupos)

            return jsonify({'sigla': sigla,'status': status})
        except Exception as e:
            traceback.print_exc(e)
            return f'Erro: {e}'


api.add_resource(Index, '/', '/index')
api.add_resource(Painel, '/painel')
api.add_resource(Status, '/status')
api.add_resource(Comando, '/comando')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

