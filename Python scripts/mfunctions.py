""" mFunctions """
from math import ceil


def rdivision(numerator: int, denominator: int) -> tuple:
    """ División con resto """
    quotient = numerator // denominator
    return quotient, numerator - quotient * denominator


def leap_year(year: int) -> bool:
    """ Determina si el año es bisiesto """
    if not year % 400:
        return True
    if not year % 100:
        return False
    if not year % 4:
        return True
    return False


def is_prime(num):
    """ Determina si el número es primo """
    for i in range(2, ceil(num**0.5 + 1)):
        if num % i == 0:
            return False
    return True


class Olist(list):
    """ Lista que se mantiene ordenada eficientemente """

    def insert_num(self, num):
        """ Inserción ordenada de números """
        self.append(num)
        index = -1
        while abs(index) < len(self) and num < self[index - 1]:
            self[index] = self[index - 1]
            self[index - 1] = num
            index -= 1


def gen_fibonacci():
    """ Retorna un generador de secuencia de Fibonacci """
    pen, last = 0, 1
    while True:
        yield pen
        temp = pen
        pen = last
        last += temp


def factorial(num):
    """ Calcula el factorial de num """
    if num <= 0:
        return 1
    return factorial(num-1) * num


def sobre(num1, num2):
    """ Calcula 'num1 sobre num2' (binomio de Newton) """
    if num1 >= num2:
        return int(factorial(num1) / (factorial(num2) * factorial(num1 - num2)))
    return 1


def looper(array_like_object):
    """ Retorna generador ciclico de los elementos de un objeto tipo array """
    while True:
        for item in array_like_object:
            yield item


def binomial(tries, succs, prob):
    """ Retorna la probabilidad de ocurrencia de 'succs' eventos en 'tries' intentos """
    return sobre(tries, succs) * prob**succs * (1 - prob)**(tries - succs)


def cumulative_binomial(tries, start, finish, prob):
    """ Probabilidad acumulada de una distribución binomial """
    return sum(binomial(tries, i, prob) for i in range(start, finish+1))


def std(data):
    """ Desviación estándar de los datos """
    sums = sum(data)
    length = len(data)
    average = sums / length
    var = 0
    for num in data:
        var += (num - average)**2
    var /= length
    res = var**0.5
    return res, sums, sums / res
