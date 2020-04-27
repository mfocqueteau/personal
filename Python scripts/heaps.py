from random import randint

A = set()


class Heap(list):
    def __init__(self):
        super().__init__()

    def insert(self, integer, i=0):
        if integer < self[i]:
            self.insert(integer, i + 1)
        else:
            pass



def siftdown(arreglo, i):
    i += 1
    try:
        maximo_hijo = max(arreglo[2*i-1], arreglo[2*i])
        indice = arreglo.index(maximo_hijo)
        if maximo_hijo > arreglo[i-1]:
            placeholder = arreglo[i-1]
            arreglo[i-1] = maximo_hijo
            maximo_hijo = placeholder

            siftdown(arreglo, indice)

    except Exception:
        pass


def preparar(arreglo):
    for i in range(0, int(len(arreglo)/2))[::-1]:
        siftdown(arreglo, i)


while len(A) < 12:
    A.add(randint(5, 25))
A = list(A)
print(A)
preparar(A)
print(A)
