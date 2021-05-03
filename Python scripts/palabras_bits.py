""" Manejo de vectores lógicos """


def sucesor(palabra):
    """
    Retorna sucesor de una palabra en binario, con overflow
    """
    largo = len(palabra)
    for i, bit in enumerate(palabra[::-1]):
        if bit == '0':
            return palabra[:largo-i-1] + '1' + '0' * (largo - len(palabra[:largo-i-1]) - 1)
    return '1' + '0' * largo


def gen_sucesores(palabra):
    """
    Retorna un generador de números en binario a partir del ingresado
    """
    while True:
        yield palabra
        palabra = sucesor(palabra)


def bin_to_dec(palabra):
    """
    Transforma un literal binario en un número decimal
    """
    dec = 0
    for i, bit in enumerate(palabra[::-1]):
        dec += int(bit) * 2**i
    return dec


def dec_to_bin(num):
    """
    Transforma un número decimal a binario
    """
    return bin(num)[2:].zfill(16)


BITS = 5
SUCESORES = gen_sucesores('0' * BITS)


INSTRUCCIONES = (
    'NOP', 'MOV', 'ADD', 'SUB', 'AND', 'OR', 'NOT', 'XOR', 'SHL',
    'SHR', 'INC', 'DEC', 'CMP', 'JMP', 'JEQ', 'JNE', 'JGT', 'JGE',
    'JLT', 'JLE', 'JCR', 'PUSH', 'POP', 'CALL', 'RET', 'IN'
)

for j, (ins, opc) in enumerate(zip(INSTRUCCIONES, SUCESORES)):
    end = '\n' if j % 2 else ' '
    print(f"'{ins}': '{opc}',", end=end)
