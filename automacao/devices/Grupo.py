class Grupo:

    devices = []

    def __init__(self, devices, nome, sigla, status='off'):
        self.devices = devices
        self.nome = nome
        self.sigla = sigla
        self.status = status

