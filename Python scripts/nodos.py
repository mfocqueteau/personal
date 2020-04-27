from math import sin


class Nodo:
    def __init__(self, valor=0, padre=None):
        self.valor = valor
        self.padre = padre
        self.hijo1 = None
        self.hijo2 = None
        self.nivel = 0

        if self.padre:
            self.nivel = self.padre.nivel + 1

    def agregar_hijo(self, valor=0):
        if not self.hijo1:
            self.hijo1 = Nodo(valor, self)
        elif not self.hijo2:
            self.hijo2 = Nodo(valor, self)
        else:
            raise NodeFull(valor)

    def quitar_hijo(self):
        if self.hijo2:
            self.hijo2 = None
        elif self.hijo1:
            self.hijo1 = None
        else:
            print("El nodo no tiene hijos")

    def __repr__(self):
        if not self.hijo1:
            return f"{' ' * self.nivel}{self.valor}"
        elif not self.hijo2:
            return f"{' ' * self.nivel}{self.valor}\n{self.hijo1}"
        else:
            return f"{' ' * self.nivel}{self.valor}\n{self.hijo1}\n{self.hijo2}"


class Heap:
    def __init__(self, raiz=None):
        self.raiz = raiz
        self.nodos = [self.raiz]

    def descendencia(self, nodo=None):
        if not nodo:
            nodo = self.raiz
        if nodo is self.raiz:
            print(nodo)
        # if nodo.hijo1:
        #     print(nodo.hijo1, nodo.hijo2)
        #     self.descendencia(nodo.hijo1)
        #     if nodo.hijo2:
        #         self.descendencia(nodo.hijo2)

    def agregar_nodo(self, valor=0):
        for nodo in self.nodos:
            if not nodo.hijo2:
                nodo.agregar_hijo(valor)
                if nodo.hijo2:
                    self.nodos.append(nodo.hijo2)
                else:
                    self.nodos.append(nodo.hijo1)
                return


class NodeFull(Exception):
    def __init__(self, valor):
        super().__init__()
        self.nodo = valor

    def __str__(self):
        return f"Nodo satisfecho: {self.nodo}"


if __name__ == '__main__':
    INICIAL = Nodo(42)
    HEAP = Heap(INICIAL)

    # INICIAL.agregar_hijo(29)
    # INICIAL.agregar_hijo(19)
    for i in range(21):
        HEAP.agregar_nodo(int(10 * abs(sin(i))))

    HEAP.descendencia()
