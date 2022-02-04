from numpy import sin, cos, pi
import numpy as np


def build_W(N: int):
    def base(n, k):
        return cos(pi/2*n*k) - 1j * sin(pi/2*n*k)
    return np.array([[clean(base(n, k)) for n in range(N)] for k in range(N)])


def clean(num: complex):
    real, imag = np.real(num), np.imag(num)
    real = 0 if real < 0.001 else real
    imag = 0 if imag < 0.001 else imag
    return real + 1j * imag


fn = np.array([1, -1, 1])
W = build_W(len(fn))

# print(W)
print(W@fn)
print(W**3)
