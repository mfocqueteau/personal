""" module_doctsring """
import tkinter
from tkinter import ttk
import backend as back

VENTANA = tkinter.Tk()
VENTANA.iconify()

NB = ttk.Notebook(VENTANA)
NB.pack(fill='both', expand='yes')

# PESTAÑAS
P1 = ttk.Frame(NB)
P2 = ttk.Frame(NB)
P3 = ttk.Frame(NB)
NB.add(P1, text="Jugador 1")
NB.add(P2, text="Jugador 2")
NB.add(P3, text="Resultados")

GEN_FIBO1 = back.gen_fibonacci()
GEN_FIBO2 = back.gen_fibonacci()
for _ in range(2):
    next(GEN_FIBO1)
    next(GEN_FIBO2)
VENTANA.geometry('400x300')

# Pestaña 1
ETIQUETA1 = tkinter.Label(P1, text=next(GEN_FIBO1), font='"fira mono" 64 bold', bg='#007fff')
ETIQUETA1.pack(fill=tkinter.BOTH, expand=True)
FIBO1 = tkinter.Button(
    P1,
    text='Next',
    padx=8,
    pady=4,
    command=lambda: back.fibonacci(ETIQUETA1, GEN_FIBO1)
)
FIBO1.pack()

# Pestaña 2
ETIQUETA2 = tkinter.Label(P2, text=next(GEN_FIBO2), font='"fira mono" 64 bold', bg='#ef9f00')
ETIQUETA2.pack(fill=tkinter.BOTH, expand=True)
FIBO2 = tkinter.Button(
    P2,
    text='Next',
    padx=8,
    pady=4,
    command=lambda: back.fibonacci(ETIQUETA2, GEN_FIBO2)
)
FIBO2.pack()


# Pestaña 3
ETIQUETA3 = tkinter.Label(P3, text='', font='"fira mono" 64 bold', bg='#00cf3f')
ETIQUETA3.pack(fill=tkinter.BOTH, expand=True)
COLOR = tkinter.Button(
    P3,
    text='Cambiar color',
    padx=8,
    pady=4,
    command=lambda: back.random_color(ETIQUETA3, back.CHARS)
)
COLOR.pack()

RESULTS = tkinter.Button(
    P3,
    text='Calcular',
    padx=8,
    pady=4,
    command=lambda: back.calculate(ETIQUETA1, ETIQUETA2, ETIQUETA3)
)
RESULTS.pack()


VENTANA.mainloop()
