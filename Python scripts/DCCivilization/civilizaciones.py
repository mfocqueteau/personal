""" Civilizaciones """
import edificios
from collections import deque, namedtuple


Atributos = namedtuple(
    'Atributos',
    (
        'id',
        'tipo',
        'centro_urbano',
        'cuartel',
        'dccowork',
        'muralla',
        'trabajador',
        'soldado',
        'ayudante',
        'oro',
        'madera',
        'piedra',
        'puntos_de_tecnologia',
        'usuario'
    )
)


class Civilizacion:
    def __init__(self, datos_civ):
        self.id = datos_civ.id
        self.tipo = datos_civ.tipo
        self.usuario = datos_civ.usuario
        self._tecnologia = datos_civ.puntos_de_tecnologia
        self._fuerza = 0
        self._defensa_base = 0
        self.p_ataque = 0
        self.p_defensa = 0

        self.trabajadores = deque()
        self.soldados = deque()
        self.ayudantes = deque()

        self.oro = 0
        self.madera = 0
        self.piedra = 0

        self.centro_urbano = edificios.CentroUrbano()
        self.cuartel = None
        self.dccowork = None
        self.murallas = deque()

    @property
    def defensa_base(self):
        return self._defensa_base

    @defensa_base.setter
    def defensa_base(self, _):
        hps = sum(soldado.hp for soldado in self.soldados if soldado.en_guardia)
        hpt = sum(trabajador.hp for trabajador in self.trabajadores)
        hpe = sum(edificio.hp for edificio in self.edificios)
        self._defensa_base = hps + hpt + hpe

    def ataque(self, otro):
        if self.p_ataque >= otro.p_defensa:
            print(f'¡{otro} ha sido eliminado directamente!')
        else:
            power = self.p_ataque
            power = self.ataque_en_serie(otro.murallas, power)
            power = self.ataque_en_serie(otro.soldados, power)
            power = self.ataque_en_serie([otro.cuartel], power)
            power = self.ataque_en_serie(otro.trabajadores, power)
            power = self.ataque_en_serie([otro.centro_urbano], power)
            if otro.centro_urbano.hp > 0:
                print(f'¡{otro} ha sobrevivido al ataque!')
            else:
                print(f'¡{otro} perdió su centro urbano!')

    def ataque_en_serie(self, entidades, power):
        if power <= 0:
            return 0
        while power > 0:
            if entidades[0].hp <= power:
                power -= entidades[0].hp
                entidades.popleft()
            else:
                entidades[0].hp -= power
                power = 0
        return power

    def __repr__(self):
        return self.tipo


class DCC(Civilizacion):
    @property
    def fuerza(self):
        return self._fuerza

    @property
    def tecnologia(self):
        return self._tecnologia

    @fuerza.setter
    def fuerza(self, valor):
        self._fuerza = valor
        self.p_ataque = self.fuerza + self.tecnologia

    @tecnologia.setter
    def tecnologia(self, valor):
        self._tecnologia = valor
        self.p_ataque = self.fuerza + self.tecnologia


class LaComarca(Civilizacion):
    @property
    def fuerza(self):
        return self._fuerza

    @property
    def piedra(self):
        return self._piedra

    @fuerza.setter
    def fuerza(self, valor):
        self._fuerza = valor
        self.p_ataque = self.fuerza + self.tecnologia

    @piedra.setter
    def piedra(self, valor):
        self._piedra = valor
        self.p_ataque = round(self.fuerza + self.piedra / 2)


class Cobreloa(Civilizacion):
    @property
    def fuerza(self):
        return self._fuerza

    @fuerza.setter
    def fuerza(self, valor):
        self._fuerza = valor
        self.p_ataque = self.fuerza * 1.15


def cargar(ruta):
    DATOS = {}
    with open(ruta, 'r') as file:
        LINEAS = map(lambda linea: linea.strip().split(','), file.readlines())
        next(LINEAS)
        for linea in LINEAS:
            DATOS[linea[0]] = Atributos(*linea)
    return DATOS
