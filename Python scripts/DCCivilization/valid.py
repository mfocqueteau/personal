from menu import MENU_OPTIONS


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
