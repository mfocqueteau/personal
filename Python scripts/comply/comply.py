""" To work with complex functions """
from math import sin, cos, pi
import numpy as np
import matplotlib.pyplot as plt


def complex_plot(signal, *args, scalex=True, scaley=True, data=None, **kwargs):
    """ Plot real and imaginary parts of a vector """
    space, values = np.real(signal[0]), signal[1]
    plt.plot(space, np.real(values), *args, **kwargs)
    plt.plot(space, np.imag(values), *args, **kwargs)


def real_plot(signal, *args, scalex=True, scaley=True, data=None, **kwargs):
    """ Plot a real signal """
    space, values = np.real(signal[0]), signal[1]
    plt.plot(space, np.real(values), *args, **kwargs)


def signal(space, function):
    return np.array((space, [function(x) for x in space]))


def DFT(signal):
    return np.array((signal[0], np.fft.fftshift(np.fft.fft(signal[1]))))


if __name__ == '__main__':
    SPACE = np.linspace(-3, 7, 100)
    def foo(x): return cos(2*x) - 1j * sin(0.67*x)
    def rect(x): return 1 if -0.5 < x < 0.5 else 0
    def sinc(x): return 1 if not x else np.sin(np.pi * x) / (np.pi * x)
    VECTOR1 = signal(SPACE, foo)
    VECTOR2 = signal(SPACE, rect)
    VECTOR3 = DFT(VECTOR2)
    complex_plot(VECTOR1)
    real_plot(VECTOR2)
    real_plot(VECTOR3)
    plt.show()
