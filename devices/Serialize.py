import json
import traceback

from devices.Default import Default
from devices.Device import Device
from devices.Grupo import Grupo


class Serialize:

    def __init__(self):
        pass

    @staticmethod
    def serializar(grupos, json_file=False):
        lista_grupos = []

        for g in grupos:
            lista_devices = []
            for d in g.devices:
                lista_devices.append([d.nome, d.pino, d.saida])
            lista_grupos.append([g.nome, g.sigla, g.status, lista_devices])

        data_json = json.dumps(lista_grupos, ensure_ascii=False)

        if json_file:
            return data_json
        else:
            file = open('grupos.json', 'w')
            file.write(data_json)
            file.close()

    @staticmethod
    def desserializar(json_file=False):
        try:
            file = open('grupos.json')
            data = json.load(file)

            if json_file:
                return data
            else:
                lista_grupos = []
                for i, g in enumerate(data):
                    lista_devices = []
                    for j, d in enumerate(g[3]):
                        lista_devices.append(Device(d[0], d[1], d[2]))
                    lista_grupos.append(Grupo(lista_devices, g[0], g[1], g[2]))

                return lista_grupos
        except FileNotFoundError as e:
            if not json_file:
                grupos = Default.build()
                Serialize.serializar(grupos)

                return grupos
            else:
                traceback.print_exc(e)


