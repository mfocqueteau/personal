'''Estructura de datos propia: lista ligada'''


class Nodo:
    def __init__(self, valor):
        self.anterior = None
        self.siguiente = None
        self.valor = valor


class Ligada:
    def __init__(self, inicial):
        self.pointer = Nodo(inicial)
        self.final = self.pointer
        self.largo = 1 if self.pointer else 0

    def insert(self, obj):
        new_node = Nodo(obj)
        if self.final:
            self.final.siguiente = new_node
        else:
            self.pointer = new_node
        new_node.anterior = self.final
        self.final = new_node
        self.largo += 1

    def extract(self):
        popped = self.final
        del self.final
        self.final = popped.anterior
        self.final.siguiente = None
        self.largo -= 1
        return popped.valor

    def extractleft(self):
        popped = self.pointer
        del self.pointer
        self.pointer = popped.siguiente
        self.pointer.anterior = None
        self.largo -= 1
        return popped.valor

    def __repr__(self):
        cursor = self.pointer
        if not cursor:
            return '[]'
        myPrint = f'[{cursor.valor}'
        while cursor.siguiente:
            cursor = cursor.siguiente
            myPrint += f'→{cursor.valor}'
        return myPrint + ']'

    def __getitem__(self, index):
        cursor = self.pointer
        if cursor:
            for _ in range(index % self.largo):
                cursor = cursor.siguiente
            return cursor.valor


def gen_fibonacci():
    pen, last = 0, 1
    while True:
        yield pen
        temp = pen
        pen = last
        last += temp


FIBO = gen_fibonacci()


LIST = Ligada(next(FIBO))

for _ in range(10):
    LIST.insert(next(FIBO))

print(LIST)
print(LIST.extract())
print(LIST)
print(LIST.extractleft())
print(LIST)
print(LIST[-2])
