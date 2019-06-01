from devices.Device import Device
from devices.Grupo import Grupo

class Default:

    def __init__(self):
        pass

    @staticmethod
    def build():
        default = [
                Grupo(nome='GARAGEM', sigla='gr', devices=[
                    Device('LUZ', 3),
                    Device('PORTÃO V.', 5),
                    Device('PORTÃO M.', 7)
                ]),
                Grupo(nome='SALA', sigla='sl', devices=[
                    Device('LUZ', 11),
                    Device('TELEVISÃO.', 13),
                    Device('COMPUTADOR', 15),
                    Device('VENTILADOR', 19)
                ]),
                Grupo(nome='COZINHA', sigla='cz', devices=[
                    Device('LUZ', 21),
                ]),
                Grupo(nome='BANHEIRO', sigla='bn', devices=[
                    Device('LUZ', 23),
                ]),
                Grupo(nome='QUARTO 1', sigla='q1', devices=[
                    Device('LUZ', 29),
                ]),
                Grupo(nome='QUARTO 2', sigla='q2', devices=[
                    Device('LUZ', 31),
                    Device('COMPUTADOR', 33),
                    Device('VENTILADOR', 35)
                ]),
                Grupo(nome='QUARTO 3', sigla='q3', devices=[
                    Device('LUZ', 36),
                    Device('COMPUTADOR', 38),
                    Device('VENTILADOR', 40)
                ])
            ]

        return default
