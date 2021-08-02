""" Edificios """
from collections import namedtuple


Atributos = namedtuple(
    'Atributos',
    'nombre tiempo c_trabajadores c_oro c_madera c_piedra hp p_oro p_madera p_piedra'
)


class Edificio:
    def __init__(self, codigo_edificio):
        datos_edificio = DATOS[codigo_edificio]
        self.nombre = datos_edificio.nombre
        self.tiempo = datos_edificio.tiempo
        self.c_trabajadores = datos_edificio.c_trabajadores
        self.c_oro = datos_edificio.c_oro
        self.c_madera = datos_edificio.c_madera
        self.c_piedra = datos_edificio.c_piedra
        self.hp = datos_edificio.hp
        self.p_oro = datos_edificio.p_oro
        self.p_madera = datos_edificio.p_madera
        self.p_piedra = datos_edificio.p_piedra


class CentroUrbano(Edificio):
    def __init__(self):
        super().__init__('centro_urbano')

    def crear_trabajador(self):
        pass


class Cuartel(Edificio):
    def __init__(self):
        super().__init__('cuartel')

    def crear_soldado(self):
        pass


class DCCowork(Edificio):
    def __init__(self):
        super().__init__('DCCowork')

    def crear_ayudante(self):
        pass


class Muralla(Edificio):
    def __init__(self):
        super().__init__('muralla')


DATOS = {}
with open('data/edificios.csv', 'r') as file:
    LINEAS = map(lambda linea: linea.strip().split(','), file.readlines())
    next(LINEAS)
    for linea in LINEAS:
        DATOS[linea[0]] = Atributos(*linea)
