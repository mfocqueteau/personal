import pickle
import itertools as it

from random import choice
from typing import Container, NamedTuple


def rp_enc(k, m):
    return k, m


def pair_with_next(gen_func):
    def wrapper(*args, **kwrds):
        gen1 = gen_func(*args, **kwrds)
        gen2 = gen_func(*args, **kwrds)
        last = next(gen2)
        for e2, e1 in zip(gen2, gen1):
            yield e1, e2
        yield next(gen1), last

    return wrapper


class Persona(NamedTuple):
    nombre: str
    anterior: str


class Familia(tuple):
    @staticmethod
    def no_repetir(container: Container[Persona]):
        for p1, p2 in pair_with_next(container.__iter__)():
            p1: Persona
            p2: Persona
            if p1.anterior == p2.nombre:
                return False
        return True

    def asignar_as(self):
        return choice(tuple(filter(self.no_repetir, it.permutations(self, len(self)))))


DATOS = (
    ("Madre", "Marto"),
    ("Marto", "Padre"),
    ("Padre", "Madre"),
    ("Sebas", "Vicente"),
    ("Vicente", "Meno"),
    ("Meno", "Sebas"),
)


def generate(datos):
    familia = Familia(map(lambda d: Persona(*d), datos))
    SANTAS = {}
    for emisor, receptor in pair_with_next(familia.asignar_as().__iter__)():
        SANTAS[emisor.nombre] = receptor.nombre

    with open("amigo.secreto", "wb") as file:
        pickle.dump(SANTAS, file)


generate(DATOS)
