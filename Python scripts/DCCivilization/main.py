""" Correr el juego """
import menu
import civilizaciones as civ

NEW = menu.inicial()

menu.cargar_partida()

RUTA = 'data/civilizaciones.csv' if NEW else 'saved/default/civilizaciones.csv'
DATOS = civ.cargar(RUTA)

DCC = civ.DCC(DATOS['0'])
LA_COMARCA = civ.LaComarca(DATOS['1'])
COBRELOA = civ.Cobreloa(DATOS['2'])
CIVILIZACIONES = [DCC, LA_COMARCA, COBRELOA]

if NEW:
    menu.elegir_civilizacion(CIVILIZACIONES)

while True:

    break
