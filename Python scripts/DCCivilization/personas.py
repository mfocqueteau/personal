""" Personas """
from random import randint
import data.constantes as ctes


class Persona:
    def __init__(self, hp):
        self.hp = hp


class Trabajador(Persona):
    def __init__(self, hp):
        super().__init__(hp)
        self.disponible = True


class Soldado(Persona):
    def __init__(self, hp):
        super().__init__(hp)
        self.fuerza = randint(ctes.MIN_ATAQUE_SOLDADO, ctes.MAX_ATAQUE_SOLDADO)
        self.en_guardia = True


class Ayudante(Persona):
    def __init__(self, hp):
        super().__init__(hp)
        self.iq = randint(ctes.MIN_IQ_AYUDANTE, ctes.MAX_IQ_AYUDANTE)
