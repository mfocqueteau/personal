import os
import pickle
from random import shuffle


with open("amigo.secreto", "rb") as file:
    DICT = pickle.load(file)


NOMBRES = list(DICT.keys())
shuffle(NOMBRES)
try:
    while True:
        for nom in NOMBRES:
            print(nom)
        input_ = input("Ingresa tu nombre como aparece en la lista: ")
        print()
        if receptor := DICT.get(input_):
            os.system("clear")
            print("Memoriza este nombre:", receptor)
            input_ = input("\nCuando estés listo/a apreta Enter")
            os.system("clear")
            exit()

except KeyboardInterrupt:
    print()
finally:
    exit()
