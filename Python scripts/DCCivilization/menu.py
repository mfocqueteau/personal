""" La lógica para todos los menús de juego """
import os


def input_valido(message, opciones_validas):
    print(message)
    _input = input('Ingresa una opción: ')
    while int(_input) not in opciones_validas:
        print('La opción no es válida, intenta de nuevo')
        _input = input(message + '\nIngresa una opción: ')
    return _input


def inicial():
    message = (
        '[1] Nueva Partida\n'
        '[2] Cargar Partida\n'
    )
    _input = input_valido(message, range(1, 3))
    return _input == '1'


def elegir_civilizacion(civilizaciones):
    print('Escoje tu civilización:')
    message = ''
    for index, civ in enumerate(civilizaciones):
        message += f'[{index+1}] {civ}\n'
    _input = int(input_valido(message, range(1, len(civilizaciones)+1)))
    print(f'Has escogido {civilizaciones[_input-1]}')
    civilizaciones[_input-1].usuario = True
    civilizaciones.sort(key=lambda civ: civ.usuario)


def cargar_partida(ruta='data/'):
    print(os.listdir(ruta))


def principal():
    message = (
        '[1] Recolectar recursos\n'
        '[2] Crear persona\n'
        '[3] Crear edificio\n'
        '[4] Atacar\n'
        '[5] Terminar turno\n'
        '[6] Ver estadísticas\n'
        '[7] Guardar\n'
        '[8] Salir\n'
    )
    _input = input_valido(message, range(1, 9))
