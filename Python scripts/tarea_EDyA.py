from collections import deque


class Pasajero:
    def __init__(self, _id, prioridad):
        self.id = _id
        self.prioridad = prioridad


class Puerta:
    def __init__(self, _id):
        self.id = _id
        self.cola = deque()


class Terminal:
    def __init__(self, _id):
        self.id = _id
        self.pasajeros = list()


def simulate():
    file = open('/home/martin/Documents/2020-1/EDyA/Tarea 0/tests/unit/0_gate_enqueue.txt')
    terminal_count = int(file.read(2).strip())
    print(f'#terminales: {terminal_count}')

    for term in range(terminal_count):
        gate_count = int(file.read(2).strip())
    print(gate_count)

    # Cerramos
    file.close()


simulate()
