""" To work with complex functions """
from typing import Callable
import numpy as np
import matplotlib.pyplot as plt


FloatToFloat = Callable[[float], float]


def signal(space: np.ndarray, func: FloatToFloat):
    return np.array([[t, func(t)] for t in space])


def plot_signal(sgn: np.ndarray, *args, imag=False, **kwargs) -> None:
    plt.plot(sgn[:, 0].real, sgn[:, 1].real, *args, **kwargs)
    if imag or np.any(sgn.imag != np.zeros_like(sgn)):
        plt.plot(sgn[:, 0].real, sgn[:, 1].imag, '--')


def rect(t: float) -> int:
    return 1 if -0.5 < t < 0.5 else 0


def exp(t):
    return np.cos(t) + 1j * np.sin(t)


def exp_n(n):
    return lambda t: np.cos(n*t) + 1j * np.sin(n*t)


time = np.linspace(0, 4, 100)
SIG = signal(time, exp_n(10))

plot_signal(SIG)
plt.show()
