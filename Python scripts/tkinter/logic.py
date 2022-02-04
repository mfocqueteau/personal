""" Lógica de project_felmer """
from random import choice

CHARS = tuple(str(i) for i in range(10)) + ('a', 'b', 'c', 'd', 'e', 'f')


def add_one(label):
    """ Suma 1 al valor actual del label """
    num = int(label['text'])
    num += 1
    label['text'] = num


def gen_fibonacci():
    """ Retorna un generador de secuencia de Fibonacci """
    pen, last = 0, 1
    while True:
        yield pen
        temp = pen
        pen = last
        last += temp


def fibonacci(label, generator):
    """ Genera secuencia de fibonacci en el label """
    label['text'] = str(next(generator))


def random_color(label, chars=CHARS):
    """ Cambia color de label aleatoriamente """
    color = ''
    for _ in range(6):
        color += choice(chars)
    label['bg'] = '#' + color
    # label.master['bg'] = '#' + color


def calculate(label1, label2, results_label):
    """ Muestra el resultado """
    results_label['text'] = f'{(int(label1["text"]) + int(label2["text"])) / 2}'
