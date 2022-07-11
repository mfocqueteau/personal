from typing import Callable, Generator
from operator import add, sub
from itertools import cycle


Operation = Callable[[int, int], int]
Operation: Operation


def __textloop(text: str) -> Generator[str, None, None]:
    text = "".join(text.split(" "))
    return cycle(text)
    # while True:
    #     for char in text:
    #         yield char


def __normalize(charset, char1, char2, operation: Operation):
    return operation(charset.index(char1), charset.index(char2)) % len(charset)


def __common_subroutine(key: str, text: str, op: Operation) -> str:
    result = ""
    key_loop = __textloop(key)
    for char, k in zip(text, key_loop):
        if char in __ABC_MINUS:
            charset, case = __ABC_MINUS, str.lower
        elif char in __ABC_MAYUS:
            charset, case = __ABC_MAYUS, str.upper
        else:
            result += char
            continue
        result += charset[__normalize(charset, char, case(k), op)]
    return result


def encrypt(text: str, *, key: str) -> str:
    return __common_subroutine(key, text, add)


def decrypt(text: str, *, key: str) -> str:
    return __common_subroutine(key, text, sub)


__ABC_MINUS = "abcdefghijklmnopqrstuvwxyz"
__ABC_MAYUS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

c = encrypt("LEMMiNO watches Gravity Falls", key="dipper")
d = decrypt(c, key="dipper")

print(c)
print(d)
