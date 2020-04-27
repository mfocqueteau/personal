from collections import namedtuple


CURSO = dict()

with open('IIC2413 - Notas 2020-1 - Público - GLOBAL.csv', 'r') as file:
    for i, line in enumerate(file):
        if i:
            alumno = line.strip().split(',')
            alumno = alumno[0] +
            print(alumno)
            CURSO[alumno[0]] = Alumno(*alumno)
        else:
            print(line)
            head = list(str(a) for a in
                        line.strip().replace(' ', '_').replace('.', '').split(','))
            print(head)
            Alumno = namedtuple('Alumno', head)
