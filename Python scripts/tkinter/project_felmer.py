""" Proyecto eléctrico de Felmer """
import tkinter
from tkinter import ttk
ROOT = tkinter.Tk()
ROOT.title("Proyecto Gestión Energética II")
TITULO = tkinter.Label(ROOT, text="Proyecto Semestral Gestión Enertgética II", bg="lightblue")
TITULO.pack(fill=tkinter.X)

PROFESOR = tkinter.Label(ROOT, text="Profesor: Felipe Escudero", bg="lightblue")
PROFESOR.pack(fill=tkinter.X)

INTEGRANTES = tkinter.Label(
    ROOT,
    text=(
        "Integrantes Grupo Nº24: \n"
        "Javier Felmer A. \n"
        "Tomás Leal G. \n"
        "Tomás Soublette P."
    ),
    bg="lightblue")
INTEGRANTES.pack(fill=tkinter.X)

PARALELO = tkinter.Label(ROOT, text="Paralelo 101", bg="lightblue")
PARALELO.pack(fill=tkinter.X)


def funcion():
    """ Ventana principal """
    otra_ventana = tkinter.Toplevel(ROOT)
    # otra_ventana.geometry('1024x600')
    ROOT.iconify()

    notebook = ttk.Notebook(otra_ventana, padding=8)
    notebook.pack(fill='both', expand='yes')

    # PESTAÑAS
    p1 = ttk.Frame(notebook)
    p2 = ttk.Frame(notebook)
    p3 = ttk.Frame(notebook)
    p4 = ttk.Frame(notebook)

    notebook.add(p1, text="Condiciones Iniciales del Proyecto")
    notebook.add(p2, text="Análisis Energético")
    notebook.add(p3, text="Emisiones gases de Efecto Invernadero")
    notebook.add(p4, text="Análisis Financiero y Costos")

    # PESTAÑA 1 #

    # TITULOS
    titulo1 = tkinter.Label(p1, text="Condiciones Iniciales", bg="light blue")
    # etiqueta1.pack(fill= tkinter.X)
    titulo1.grid(row=0, column=0)
    titulo2 = tkinter.Label(p1, text="Condiciones Colector Solar", bg="light blue")
    titulo2.grid(row=6, column=0)
    # etiqueta2.pack(fill= tkinter.X)
    titulo3 = tkinter.Label(p1, text="Condiciones Combustible", bg="light blue")
    titulo3.grid(row=6, column=3)
    titulo4 = tkinter.Label(p1, text="Materiales", bg="light blue")
    titulo4.grid(row=11, column=0)

    # ETIQUETAS
    # NOMBRES
    etiqueta1 = tkinter.Label(p1, text="Temperatura interior [ºC]:")
    etiqueta2 = tkinter.Label(p1, text="Temperatura ambiente [ºC]:")
    etiqueta3 = tkinter.Label(p1, text="Temperatura agua [ºC]:")
    etiqueta4 = tkinter.Label(p1, text="Temperatura agua caliente [ºC]:")
    etiqueta5 = tkinter.Label(p1, text="Consumo agua caliente [L/día]:")
    etiqueta6 = tkinter.Label(p1, text="Vida del proyecto [años]:")
    etiqueta7 = tkinter.Label(p1, text="Cantidad total de familias [Familias]:")
    etiqueta8 = tkinter.Label(p1, text="Fr (tau alpha):")
    etiqueta9 = tkinter.Label(p1, text="Fr (UL):")
    etiqueta10 = tkinter.Label(p1, text="Area colector solar:")
    etiqueta11 = tkinter.Label(p1, text="Poder calorifico combustible [kCal/m3]:")
    etiqueta12 = tkinter.Label(p1, text="Precio combustible [$/kg]:")
    etiqueta13 = tkinter.Label(p1, text="Densidad del combustible [kg/m3]:")
    etiqueta14 = tkinter.Label(p1, text="Detalles del material")

    # POSICIONES
    etiqueta1.grid(row=1, column=0)
    etiqueta2.grid(row=2, column=0)
    etiqueta3.grid(row=1, column=2)
    etiqueta4.grid(row=2, column=2)
    etiqueta5.grid(row=3, column=2)
    etiqueta6.grid(row=4, column=0)
    etiqueta7.grid(row=5, column=0)
    etiqueta8.grid(row=7, column=0)
    etiqueta9.grid(row=8, column=0)
    etiqueta10.grid(row=9, column=0)
    etiqueta11.grid(row=7, column=2)
    etiqueta12.grid(row=8, column=2)
    etiqueta13.grid(row=9, column=2)
    etiqueta14.grid(row=12, column=0)

    # CAJAS DE TEXTO COMO RANGO PARA INPUTS
    cajas_pestana_1 = [tkinter.Entry(p1) for _ in range(13)]

    # POSICIONES
    cajas_pestana_1[0].grid(row=1, column=1)
    cajas_pestana_1[1].grid(row=2, column=1)
    cajas_pestana_1[2].grid(row=1, column=3)
    cajas_pestana_1[3].grid(row=2, column=3)
    cajas_pestana_1[4].grid(row=3, column=3)
    cajas_pestana_1[5].grid(row=4, column=1)
    cajas_pestana_1[6].grid(row=5, column=1)
    cajas_pestana_1[7].grid(row=7, column=1)
    cajas_pestana_1[8].grid(row=8, column=1)
    cajas_pestana_1[9].grid(row=9, column=1)
    cajas_pestana_1[10].grid(row=7, column=3)
    cajas_pestana_1[11].grid(row=8, column=3)
    cajas_pestana_1[12].grid(row=9, column=3)

    my_listbox = tkinter.Listbox(p1)
    my_listbox.grid(row=12, column=1)
    my_list = ["Poliestireno Extruido", "Poliestireno Expandido", "Lana de Vidrio",
               "Lana de Roca", "Poliuterano", "Paneles Sandwich", "Corcho", "Celulosa"]

    for item in my_list:
        my_listbox.insert(0, item)

    def select():

        if my_listbox.get(tkinter.ANCHOR) == "Poliestireno Extruido":
            my_label.config(
                text=(
                    "Descripción: Espuma rígida de altos valores de resistencia térmica.\n"
                    "Este posee una conductividad térmica típica entre 0,025 [W/mK]\n"
                    "Dimensiones: 1,2 [m]x 0,6 [m] x 0,02[m]"
                ),
                bg="white"
            )
        elif my_listbox.get(tkinter.ANCHOR) == "Poliestireno Expandido":
            my_label.config(
                text=(
                    "Descripción: una espuma rígida de color blanco de gran trabajabilidad,\n"
                    "caracterizada por un termoplástico celular de baja densidad\n"
                    "y alta resistencia físico-mecánica en relación a su reducido peso aparente.\n"
                    "Conductividad térmica= 0,0384 [W/mK]\n"
                    "Dimensiones= 1,2 [m] x 0,6 [m] x 0,05[m]"
                ),
                bg="white")
        elif my_listbox.get(tkinter.ANCHOR) == "Lana de Vidrio":
            my_label.config(
                text=(
                    "Descripción: Esta posee un alto poder de aislación térmica, \n"
                    "una gran absorción acústica y durabilidad e inalterabilidad \n"
                    "Conductividad térmica=0, 0405 [W/m°C] \n"
                    "Dimensiones= 1,2[m] x 9,6 [m] 0,08[m]"
                ), bg="white")
        elif my_listbox.get(tkinter.ANCHOR) == "Poliuterano":
            my_label.config(
                text="Descripción: Estos son muy utilizados como aislantes térmicos. Sus principales aplicaciones son las aislación en frigoríficos. \n Conductividad térmica= 0,020 [W/mK] \n Dimensiones: 0,5 [m] x 1[m] x 0,02 [m].", bg="white")
        elif my_listbox.get(tkinter.ANCHOR) == "Lana de Roca":
            my_label.config(
                text="Descripción: Material fabricado a partir de la roca volcánica. \n Se utiliza principalmente como aislamiento térmico y \n como protección pasiva contra el fuego en la edificación, debido a su estructura fibrosa multidireccional,\n que le permite albergar aire relativamente inmóvil en su interior.\n Conductividad térmica = 0,025 [W/mK] \n Dimensiones= 0,61 [m] x 0,61 [m] x 0,02 [m]", bg="white")
        elif my_listbox.get(tkinter.ANCHOR) == "Paneles Sandwich":
            my_label.config(
                text=(
                    "Descripción: El Panel SIP, un moderno y completo sistema "
                    "estructural auto soportante usado para la construcción, \n"
                    "conformado por un alma de espuma rígida de Poliestireno de "
                    "alta densidad (EPS) \n Dimensiones= 6,10 [m] x 4,88 [m]."
                ),
                bg="white")

    my_label = tkinter.Label(p1, text="")
    my_label.grid(row=12, column=2, columnspan=2)

    my_button2 = tkinter.Button(p1, text="Seleccionar Material", command=select)
    my_button2.grid(row=14, column=1)
    my_button2.configure(bg="grey", fg="black")

    # BOTONES
    botonp1 = tkinter.Button(p1, text="Cerrar Programa", command=otra_ventana.destroy)
    botonp1.grid(row=13, column=3)
    botonp1.configure(bg="grey", fg="black")

    ###########################   PESTAÑA 2   ##############################

    # TITULOS
    titulo1 = tkinter.Label(p2, text="Paredes Paralelas", bg="light blue")
    # etiqueta1.pack(fill= tkinter.X)
    titulo1.grid(row=4, column=0)
    titulo2 = tkinter.Label(p2, text="Paredes Transversales", bg="light blue")
    titulo2.grid(row=4, column=2)
    # etiqueta2.pack(fill= tkinter.X)
    titulo3 = tkinter.Label(p2, text="Calefacción de Agua", bg="light blue")
    titulo3.grid(row=9, column=0)
    titulo4 = tkinter.Label(p2, text="Colectores Solares", bg="light blue")
    titulo4.grid(row=9, column=2)
    titulo5 = tkinter.Label(p2, text="Cálculos Energéticos Totales", bg="light blue")
    titulo5.grid(row=16, column=0)

    # ETIQUETAS
    # NOMBRES
    etiqueta1 = tkinter.Label(p2, text="Coeficiente convectivo exterior (h) [W/ºC*m^2]:")
    etiqueta2 = tkinter.Label(p2, text="Coeficiente convectivo interior (h) [W/ºC*m^2]:")
    etiqueta3 = tkinter.Label(p2, text="Resistencia a la conducción [ºC/W]:")
    etiqueta4 = tkinter.Label(p2, text="Resistencia a la convección exterior [ºC/W]:")
    etiqueta5 = tkinter.Label(p2, text="Resistencia a la convección interior [ºC/W]:")
    etiqueta6 = tkinter.Label(p2, text="Resistencia a la radiación [ºC/W]:")
    etiqueta7 = tkinter.Label(p2, text="Resistencia a la conducción [ºC/W]:")
    etiqueta8 = tkinter.Label(p2, text="Resistencia a la convección exterior [ºC/W]:")
    etiqueta9 = tkinter.Label(p2, text="Resistencia a la convección interior [ºC/W]:")
    etiqueta10 = tkinter.Label(p2, text="Resistencia a la radiación [ºC/W]:")
    etiqueta11 = tkinter.Label(p2, text="Flujo másico de agua caliente [kg/s]:")
    etiqueta12 = tkinter.Label(p2, text="Energía necesaria para calentar el agua en el día [kWh]:")
    etiqueta13 = tkinter.Label(p2, text="Energía suministrada por colector solar [kWh]:")
    etiqueta14 = tkinter.Label(p2, text="Energía a suministrar por combustible por familia [kWh]:")
    etiqueta15 = tkinter.Label(p2, text="Energía a suministrar por combustible en complejo [kWh]:")
    etiqueta16 = tkinter.Label(p2, text="Cantidad de colectores por familia:")
    etiqueta17 = tkinter.Label(p2, text="Cantidad de colectores por complejo habitacional:")

    # Pestañas
    etiqueta1.grid(row=0, column=0)
    etiqueta2.grid(row=1, column=0)
    etiqueta3.grid(row=5, column=0)
    etiqueta4.grid(row=6, column=0)
    etiqueta5.grid(row=7, column=0)
    etiqueta6.grid(row=8, column=0)
    etiqueta7.grid(row=5, column=2)
    etiqueta8.grid(row=6, column=2)
    etiqueta9.grid(row=7, column=2)
    etiqueta10.grid(row=8, column=2)
    etiqueta11.grid(row=10, column=0)
    etiqueta12.grid(row=11, column=0)
    etiqueta13.grid(row=12, column=0)
    etiqueta14.grid(row=13, column=0)
    etiqueta15.grid(row=14, column=0)
    etiqueta16.grid(row=10, column=2)
    etiqueta17.grid(row=11, column=2)

    # Cajas de texto como Rango para celdas de input
    cajas_pestana_2 = [tkinter.Entry(p2) for _ in range(2)]

    # POSICIONES
    cajas_pestana_2[0].grid(row=0, column=1)
    cajas_pestana_2[1].grid(row=1, column=1)

    # BOTONES
    botonp2 = tkinter.Button(p2, text="Cerrar Programa", command=otra_ventana.destroy)
    botonp2.grid(row=13, column=3)
    botonp2.configure(bg="grey", fg="black")

  # PARA DEFINIR LAS FUNCIONES EN UN LABEL
    resultado1 = tkinter.Label(p2, text="", bg="white", width=20, height=1)
    resultado2 = tkinter.Label(p2, text="", bg="white", width=20, height=1)
    resultado3 = tkinter.Label(p2, text="", bg="white", width=20, height=1)
    resultado4 = tkinter.Label(p2, text="", bg="white", width=20, height=1)
    resultado5 = tkinter.Label(p2, text="", bg="white", width=20, height=1)
    resultado6 = tkinter.Label(p2, text="", bg="white", width=20, height=1)
    resultado7 = tkinter.Label(p2, text="", bg="white", width=20, height=1)
    resultado8 = tkinter.Label(p2, text="", bg="white", width=20, height=1)
    resultado9 = tkinter.Label(p2, text="", bg="white", width=20, height=1)
    resultado10 = tkinter.Label(p2, text="", bg="white", width=20, height=1)
    resultado11 = tkinter.Label(p2, text="", bg="white", width=20, height=1)
    resultado12 = tkinter.Label(p2, text="", bg="white", width=20, height=1)
    resultado13 = tkinter.Label(p2, text="", bg="white", width=20, height=1)
    resultado14 = tkinter.Label(p2, text="", bg="white", width=20, height=1)
    resultado15 = tkinter.Label(p2, text="", bg="white", width=20, height=1)
    resultado16 = tkinter.Label(p2, text=(
        "La transferencia total por conducción es de:"
        "La transferencia total por convección es de:"
        "La transferencia total por radiación es de:"
        "La transferencia total por casa es de:"
        "La transferenacia total para el coplejo habitacional es de:"
    ),
        bg="white", width=65, height=5
    )

    resultado1.grid(row=5, column=1)
    resultado2.grid(row=6, column=1)
    resultado3.grid(row=7, column=1)
    resultado4.grid(row=8, column=1)
    resultado5.grid(row=10, column=1)
    resultado6.grid(row=11, column=1)
    resultado7.grid(row=12, column=1)
    resultado8.grid(row=13, column=1)
    resultado9.grid(row=14, column=1)
    resultado10.grid(row=5, column=3)
    resultado11.grid(row=6, column=3)
    resultado12.grid(row=7, column=3)
    resultado13.grid(row=8, column=3)
    resultado14.grid(row=10, column=3)
    resultado15.grid(row=11, column=3)
    resultado16.grid(row=24, column=0, columnspan=2)

    boton2 = tkinter.Button(p2, text="Iniciar Análisis", command=lambda: iniciar_analisis(
        cajas_pestana_2[0], cajas_pestana_2[1]))
    boton2.grid(row=2, column=0)

    def iniciar_analisis(exterior, interior):
        exterior = float(exterior.get())
        interior = float(interior.get())
        resultado1["text"] = exterior*interior
        resultado2["text"] = exterior+interior
        resultado3["text"] = exterior*interior
        resultado4["text"] = exterior+interior
        resultado5["text"] = exterior*interior
        resultado6["text"] = exterior+interior
        resultado7["text"] = exterior*interior
        resultado8["text"] = exterior+interior
        resultado9["text"] = exterior*interior
        resultado10["text"] = exterior+interior
        resultado11["text"] = exterior*interior
        resultado12["text"] = exterior+interior
        resultado13["text"] = exterior*interior
        resultado14["text"] = exterior+interior
        resultado15["text"] = exterior*interior
        resultado16["text"] = exterior*interior

    ###########################   PESTAÑA 3    ##############################

    # ETIQUETAS
    # NOMBRES
    etiqueta1 = tkinter.Label(p3, text="Factor de emisión [kg CO2/KWh]:")
    etiqueta1.grid(row=0, column=0)

    # CAJAS DE TEXTO

    cajadetexto1 = tkinter.Entry(p3)
    cajadetexto1.grid(row=0, column=1)

    # BOTONES
    botonp3 = tkinter.Button(p3, text="Cerrar Programa", command=otra_ventana.destroy)
    botonp3.grid(row=10, column=3)
    botonp3.configure(bg="grey", fg="black")
    #botonp3= tkinter.Button(p3,text = "Cerrar Programa",command =otra_ventana.destroy)
    # botonp3.pack(side=tkinter.BOTTOM)

    ###########################   PESTAÑA 4   ##############################

    # TITULOS
    titulo1 = tkinter.Label(p4, text="Parámetros Financieros", bg="light blue")
    titulo1.grid(row=0, column=0)
    titulo2 = tkinter.Label(p4, text="Costos Financieros", bg="light blue")
    titulo2.grid(row=6, column=0)
    titulo3 = tkinter.Label(p4, text="Costos Combustibles", bg="light blue")
    titulo3.grid(row=10, column=0)

    # ETIQUETAS
    # NOMBRES
    etiqueta1 = tkinter.Label(p4, text="Tasa de descuento social [%]:")
    etiqueta2 = tkinter.Label(p4, text="Vida útil del colector [%]:")
    etiqueta3 = tkinter.Label(p4, text="Salario ingeniería [$/día]:")
    etiqueta4 = tkinter.Label(p4, text="Precio electricidad [$/kWh]:")
    etiqueta5 = tkinter.Label(p4, text="Precio del colector [$]:")
    etiqueta6 = tkinter.Label(p4, text="VAC [$]:")
    etiqueta7 = tkinter.Label(p4, text="Costo energía [$/día]:")
    etiqueta8 = tkinter.Label(p4, text="Costo materiales [$]:")
    etiqueta9 = tkinter.Label(p4, text="Costo ingeniería [$]:")
    etiqueta10 = tkinter.Label(p4, text="Costo energía suministrada por colector solar [$/kWh]:")
    etiqueta11 = tkinter.Label(p4, text="Costo por combustible suministrado [$/kWh]:")

    # POSICIONES
    etiqueta1.grid(row=1, column=0)
    etiqueta2.grid(row=2, column=0)
    etiqueta3.grid(row=1, column=2)
    etiqueta4.grid(row=2, column=2)
    etiqueta5.grid(row=3, column=2)
    etiqueta6.grid(row=5, column=0)
    etiqueta7.grid(row=7, column=0)
    etiqueta8.grid(row=8, column=0)
    etiqueta9.grid(row=9, column=0)
    etiqueta10.grid(row=11, column=0)
    etiqueta11.grid(row=12, column=0)

    # CAJAS DE TEXTO COMO RANGO PARA INPUTS
    cajas_pestana_4 = [tkinter.Entry(p4) for _ in range(12)]

    # POSICIONES
    cajas_pestana_4[0].grid(row=1, column=1)
    cajas_pestana_4[1].grid(row=2, column=1)
    cajas_pestana_4[2].grid(row=1, column=3)
    cajas_pestana_4[3].grid(row=2, column=3)
    cajas_pestana_4[4].grid(row=3, column=3)
    cajas_pestana_4[5].grid(row=5, column=1)
    cajas_pestana_4[6].grid(row=7, column=1)
    cajas_pestana_4[7].grid(row=8, column=1)
    cajas_pestana_4[8].grid(row=9, column=1)
    cajas_pestana_4[9].grid(row=11, column=1)
    cajas_pestana_4[10].grid(row=12, column=1)

    # BOTONES
    boton1 = tkinter.Button(p4, text="Obtener indicadores", padx=30)
    boton1.grid(row=3, column=1)

    botonp4 = tkinter.Button(p4, text="Cerrar Programa", command=otra_ventana.destroy)
    botonp4.grid(row=15, column=3)
    botonp4.configure(bg="grey", fg="black")


boton = tkinter.Button(ROOT, text="Iniciar Programa", command=funcion)
boton.pack()
#boton_fin = tkinter.Button(ROOT, text="Cerrar Programa", command=funcion)
# boton.pack()
ROOT.mainloop()
