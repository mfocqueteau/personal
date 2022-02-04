""" La lógica para todos los menús de juego """
import os
import json

with open("menu.json", "r") as file:
    MENU_OPTIONS = json.load(file)


def valid_input(menu):
    options = MENU_OPTIONS[menu]
    _input = display(options)
    valid_options = range(1, len(options) + 1)
    while _input not in valid_options:
        print("La opción no es válida, intenta de nuevo\n")
        _input = display(options)
    return _input


def display(options):
    for i, opt in enumerate(options):
        print(f"[{i}] {opt}")
    return int(input("Ingresa una opción: "))


def inicial():
    _input = valid_input("inicial")
    return _input == "1"


def pick_civ(civilizations):
    print("Escoje tu civilización:")
    _input = int(valid_input("civilizations"))
    print(f"Has escogido {civilizations[_input-1]}")
    civilizations[_input - 1].usuario = True
    civilizations.sort(key=lambda civ: civ.usuario)


def cargar_partida(ruta="data/"):
    print(os.listdir(ruta))


def principal():
    _input_ = valid_input("principal")


principal()
