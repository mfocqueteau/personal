from typing import Callable, Generator


def __wordloop(word: str) -> Generator:
    word = "".join(word.split(" "))
    while True:
        for char in word:
            yield char


def __cross(charset: str, char1: str, char2: str) -> str:
    return charset[(charset.index(char1) + charset.index(char2)) % 26]


def __rcross(charset: str, char1: str, char2: str) -> str:
    return charset[(charset.index(char1) - charset.index(char2)) % 26]


def __common_subroutine(key: str, word: str, cross_func: Callable) -> str:
    result = ""
    key_loop = __wordloop(key)
    for char in word:
        if char in __ABC_MINUS:
            charset, case = __ABC_MINUS, str.lower
        elif char in __ABC_MAYUS:
            charset, case = __ABC_MAYUS, str.upper
        else:
            result += char
            continue
        result += cross_func(charset, char, case(next(key_loop)))
    return result


def encrypt(word: str, *, key: str) -> str:
    return __common_subroutine(key, word, __cross)


def decrypt(word: str, *, key: str) -> str:
    return __common_subroutine(key, word, __rcross)


__ABC_MINUS = "abcdefghijklmnopqrstuvwxyz"
__ABC_MAYUS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
