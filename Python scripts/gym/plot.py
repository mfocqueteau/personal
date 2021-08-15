from os import removexattr
from tkinter import Label
import matplotlib.pyplot as plt
import registry as reg


def plot_progress(start=None, finish=None):
    data = reg.load_sessions()
    for col in data.columns[1:-1]:
        plt.plot(data['date'], data[col], '.-', label=beautify(col))
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def beautify(column: str) -> str: return column.replace('_', '').title()
