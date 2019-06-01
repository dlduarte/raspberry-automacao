# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO


class Gpio:

    def __init__(self, pino, saida=False, mode='OUT'):
        GPIO.setmode(GPIO.BOARD)  # Utilizando o numero do pino
        GPIO.setwarnings(False)  # Desabilita mensagens

        print(f'Recebido o pino {pino} para definir como {saida} no setup {mode}')
        
        setup = getattr(GPIO, mode)
        
        GPIO.setup(pino, setup)
        GPIO.output(pino, saida)
        print('Definido.')

