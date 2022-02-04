""" To work with complex functions """
# from collections import namedtuple
from math import sin, cos, pi
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# __Signal = namedtuple("Signal", "space values")

show = plt.show


def complex_plot(signal, *args, scalex=True, scaley=True, data=None, **kwargs):
    """Plot real and imaginary parts of a vector"""
    space, values = signal["space"], signal["values"]
    plt.plot(space, np.real(values), *args, **kwargs)
    plt.plot(space, np.imag(values), *args, **kwargs)


def real_plot(signal, *args, scalex=True, scaley=True, data=None, **kwargs):
    """Plot a real signal"""
    space, values = signal["space"], signal["values"]
    plt.plot(space, np.real(values), *args, **kwargs)


def signal(space, function):
    return pd.DataFrame(data={"space": space, "values": [function(x) for x in space]})
    # return __Signal(space, [function(x) for x in space])


def dft(signal):
    space, values = signal["space"], signal["values"]
    return pd.DataFrame(data={"space": space, "values": np.fft.fftshift(np.fft.fft(values))})
    # return __Signal(signal.space, np.fft.fftshift(np.fft.fft(signal.values)))


def main():
    SPACE = np.linspace(-3, 7, 100)

    def foo(x):
        return cos(2 * x) - 1j * sin(0.67 * x)

    def rect(x):
        return 1 if -0.5 < x < 0.5 else 0

    # def sinc(x):
    #     return 1 if not x else np.sin(np.pi * x) / (np.pi * x)

    S1 = signal(SPACE, foo)
    S2 = signal(SPACE, rect)
    S3 = dft(S2)
    complex_plot(S1)
    real_plot(S2)
    real_plot(S3)
    plt.show()


if __name__ == "__main__":
    main()
