from flask import Flask, request, abort, jsonify, render_template, Response, json
from flask_restful import Resource, Api
from flask_cors import CORS
import traceback

from devices.Serialize import Serialize
from devices.Gpio import Gpio

app = Flask(__name__)
api = Api(app)
CORS(app, support_credentials=True)


class Index(Resource):
    def get(self):
        try:
            return Response(
                render_template(
                    "index.html",
                    mimetype='text/html',
                    Grupos=Serialize.desserializar()
                )
            )
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
            Gpio(pino, saida)

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


api.add_resource(Index, '/')
api.add_resource(Status, '/status')
api.add_resource(Comando, '/comando')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

