import tkinter as tk

from matplotlib.pyplot import margins, title
import registry as reg
import plot


class Field:
    def __init__(self, master, text, grid):
        self.label = tk.Label(master, text=text)
        self.entry = tk.Entry(master)
        self.grid(*grid)

    def get(self):
        return self.entry.get()

    def grid(self, row, column):
        self.label.grid(row=row, column=column, sticky=tk.W)
        self.entry.grid(row=row, column=column+1)


WINDOW = tk.Tk()
WINDOW.title('Marto\'s GYM')
WINDOW.resizable(False, False)
WINDOW.config(padx='0.5ch', pady='0.5ch', )

PULLUPS = Field(WINDOW, text='Pullups:', grid=(0, 0))
SQUATS = Field(WINDOW, text='Squats:', grid=(1, 0))
DIPS = Field(WINDOW, text='Dips:', grid=(2, 0))
DEADLIFTS = Field(WINDOW, text='Deadlifts:', grid=(3, 0))
ROWS = Field(WINDOW, text='Rows:', grid=(4, 0))
PUSH_UPS = Field(WINDOW, text='Pushups:', grid=(5, 0))
COMMENTS = Field(WINDOW, text='Comentario:', grid=(6, 0))

EXERCICES = map(
    lambda field: field.get(),
    [PULLUPS, SQUATS, DIPS, DEADLIFTS, ROWS, PUSH_UPS, COMMENTS]
)

SUBMIT = tk.Button(text='Submit', command=lambda: reg.add_session(EXERCICES))
SUBMIT.grid(row=7, column=0)

PLOT = tk.Button(text='Gráfico', command=plot.plot_progress)
PLOT.grid(row=7, column=1)

WINDOW.mainloop()
