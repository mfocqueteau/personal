# def paralelo(a, b):
#     return (a*b/(a+b))

_input = 32

llega_hasta = 2 ** (_input - 1) - 1

dia_tiene = 24 * 3600
anio_tiene = 365 * dia_tiene

anios = llega_hasta // anio_tiene
dias = llega_hasta % anio_tiene // dia_tiene
horas = llega_hasta % anio_tiene % dia_tiene // 3600
minutos = llega_hasta % anio_tiene % dia_tiene % 3600 // 60
segundos = llega_hasta % anio_tiene % dia_tiene % 3600 % 60


anios = str(anios)
while len(anios) < 4:
    anios = '0' + anios

dias = str(dias)
while len(anios) < 2:
    anios = '0' + anios

horas = str(horas)
while len(anios) < 2:
    anios = '0' + anios

minutos = str(minutos)
while len(anios) < 2:
    anios = '0' + anios


print(f"{anios}/{dias} 0{horas}:{minutos}:0{segundos}")
print(llega_hasta)
