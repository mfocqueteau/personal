""" Interface objects handler """
import tkinter


class Field:
    """ A simple field object """

    def __init__(self, master, text, **kwargs):
        self.label = tkinter.Label(master, text=text)
        self.entry = tkinter.Entry(master)
        if kwargs:
            if 'label' in kwargs:
                self.label.config(**kwargs['label'])
            if 'entry' in kwargs:
                self.entry.config(**kwargs['entry'])

    def grid(self, row=0, column=0):
        """ Place the field in the window """
        self.label.grid(row=row, column=column, sticky=tkinter.W)
        self.entry.grid(row=row, column=column+1)

    def get(self):
        """ Get current entry value """
        return self.entry.get()


class Result:
    """ A simple result object """

    def __init__(self, master, text, unit, **kwargs):
        self.label = tkinter.Label(master, text=text)
        self.result = tkinter.Label(master)
        self.unit = tkinter.Label(master, text=f'{unit}')
        if kwargs:
            if 'label' in kwargs:
                self.label.config(**kwargs['label'])
                self.unit.config(**kwargs['label'])
                self.result.config(**kwargs['label'])

    def grid(self, row=0, column=0):
        """ Place the result in the window """
        self.label.grid(row=row, column=column, sticky=tkinter.W)
        self.result.grid(row=row, column=column+1, sticky=tkinter.E)
        self.unit.grid(row=row, column=column+2, sticky=tkinter.W)
