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


def gen_valuations(nprops=1):
    word = 0
    for _ in range(2 ** nprops):
        yield word
        word += 1


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


def main():
    OPCODES = True
    BITWISE = False

    if OPCODES:
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

    if BITWISE:
        NPROPS = 3
        VALUATIONS = gen_valuations(nprops=NPROPS)
        KEYS = range(1, NPROPS + 1)
        VALUES = map(lambda k: (2**(k-1) & val) // 2**(k-1), KEYS)
        for val in VALUATIONS:
            assigned = {
                key: value for key, value in
                zip(range(1, NPROPS+1), )
            }
            print(assigned)


if __name__ == '__main__':
    main()
