""" Libreria del Marto """
import math
from collections import namedtuple
from functools import cache, reduce
from time import perf_counter
from typing import Container, Generator, Iterable, Union


Timed = namedtuple("Timed", "time value")
Empty = (_ for _ in [])


def pipe(*fns):
    return lambda x: reduce(lambda x, f: f(x), fns, x)


def take_the_time(foo):
    """Decorador para cronometrar el tiempo de una funcion. Retorna namedtuple Timed"""

    def wrapper(*args, **kwargs):
        t_0 = perf_counter()
        result = foo(*args, **kwargs)
        t_d = perf_counter() - t_0

        return Timed(t_d, result)

    return wrapper


def observe(foo):
    def wrapper(*args, **kwargs):
        _, _id = str(perf_counter()).split(".")
        print(f"begin {foo.__name__} @ {_id}")
        print(f"  args: {args}")
        print(f"  kwargs: {kwargs}")
        t_0 = perf_counter()
        result = foo(*args, **kwargs)
        t_d = perf_counter() - t_0
        print(f"  return: {result}")
        print(f"  time: {t_d}")
        print(f"end {foo.__name__} @ {_id}")
        return result

    return wrapper


def dprint(title: str, *args, **kwargs):
    print(title + "-" * abs(100 - len(title)), *args, "-" * 100, **kwargs, sep="\n")


@observe
def rdivision(numerator: int, denominator: int) -> "tuple[int, int]":
    """División con resto. Retorna tupla (cuociente, resto)"""
    quotient = numerator // denominator
    remainder = numerator - quotient * denominator
    return quotient, remainder


def anti_harmonic(nums: Iterable[Union[int, float]]) -> float:
    """Mi versión de una anti armónica"""
    numerator = 0
    denominator = 0
    for num in nums:
        numerator += num**2
        denominator += num
    return numerator / denominator


def geometric_mean(nums: Iterable[Union[int, float]]) -> float:
    product = 1
    root = 0
    for num in nums:
        product *= num
        root += 1
    root = max(1, root)
    return product ** (1 / root)


factorial = cache(math.factorial)


def sobre(num1: int, num2: int) -> int:
    """Calcula 'num1 sobre num2' (binomio de Newton)"""
    if num1 < num2:
        return 1
    return int(factorial(num1) / (factorial(num2) * factorial(num1 - num2)))


def looper(container: Container, *, frozen=True) -> Generator:
    """Retorna generador ciclico de los elementos de un contenedor"""
    if frozen:
        container = tuple(container)
    while True:
        for item in container:
            yield item


class Looper:
    def __init__(self, container: Container, *, frozen=True):
        self.container = container
        self.loop = looper(container, frozen=frozen)

    @property
    def length(self):
        return len(self.container)

    def __call__(self, limit: int = 1):
        for _, element in zip(range(limit), self.loop):
            yield element

    def __contains__(self, item):
        return item in self.container

    def __iter__(self):
        return self.loop

    def __next__(self):
        return next(self.loop)


def binomial(tries: int, succs: int, prob: float) -> float:
    """Retorna la probabilidad de ocurrencia de 'succs' eventos en 'tries' intentos"""
    return sobre(tries, succs) * prob**succs * (1 - prob) ** (tries - succs)


def cumulative_binomial(tries: int, start: int, finish: int, prob: float) -> float:
    """Probabilidad acumulada de una distribución binomial"""
    return sum(binomial(tries, i, prob) for i in range(start, finish + 1))


def std(data: "list[list]") -> tuple:
    """Desviación estándar de los datos"""
    sums = sum(data)
    length = len(data)
    average = sums / length
    var = sum((num - average) ** 2 for num in data) / length
    res = var**0.5
    return res, sums, sums / res
