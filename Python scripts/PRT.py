from collections import deque
from random import choice, randrange


class Auto:
    """Esta clase modela los autos que llegan a la revision."""

    # Un staticmethod es un método propio de la clase, que no se aplica a una instancia particular
    # Su primer argumento NO es una instancia de la clase (al que solemos llamar self)
    @staticmethod
    def tiempo_revision(tipo):
        if tipo == 'auto':
            return 10
        elif tipo == 'moto':
            return 25
        return 30

    def __init__(self):
        self.tipo_vehiculo = choice(['moto', 'camioneta', 'auto'])
        self.tiempo_revision = self.tiempo_revision(self.tipo_vehiculo)

    def __str__(self):
        return self.tipo_vehiculo


class Taller:
    """
    Esta clase modela la línea de revision en el taller.
    """

    def __init__(self):
        self.auto_actual = None
        self.tiempo_actual = 0

    def ocupado(self):
        """
        Verifica si el taller está ocupado. 
        Retorna False cuando está vacío.
        """
        return self.auto_actual != None

    def ingresar_auto(self, auto):
        self.auto_actual = auto
        self.tiempo_actual = 0
        print("Atendiendo: {}".format(self.auto_actual))

    def tick(self):
        """
        Realiza el incremento del contador de tiempo 
        en la simulación.
        """
        if self.auto_actual != None:
            self.tiempo_actual += 1
            if self.auto_actual.tiempo_revision == self.tiempo_actual:
                self.auto_actual = None
                self.tiempo_actual = 0


def llega_nuevo_auto():
    """
    La llegada de los vehículos a la línea de 
    revisión está modelada como un proceso aleatorio.
    Por cada intervalo de tiempo, hay un 1% de 
    probabilidad de que llegue un auto
    """
    return 0 == randrange(0, 50)


def revision_tecnica():
    """Esta función maneja el proceso de revisión."""

    planta_revision = Taller()  # Crea una planta de revisión
    cola_revision = deque()  # Cola de revision vacia
    tiempo_espera = []  # Lista con los tiempos de espera

    # Simulación por 500 intervalos de tiempo
    for _ in range(500):

        if llega_nuevo_auto():
            auto = Auto()
            cola_revision.append(auto)

        if (not planta_revision.ocupado()) and (len(cola_revision) > 0):
            # Extrae el próximo auto en la cola de atención y
            # lo pasa a la planta de revisión.
            proximo_auto = cola_revision.popleft()
            tiempo_espera.append(proximo_auto.tiempo_revision)
            planta_revision.ingresar_auto(proximo_auto)

        planta_revision.tick()  # Incrementa el tiempo que el auto ha sido atendido

    tiempo_promedio = sum(tiempo_espera) / len(tiempo_espera)
    print(f"""Tiempo promedio de atención: {tiempo_promedio:6.2f} minutos """
          f"""y {len(cola_revision)} vehiculos aún esperando.""")


revision_tecnica()
