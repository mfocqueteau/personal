""" Create uninstatiated variables """


class Variable:
    def __init__(self, name):
        self.name = name
        self.pond = 1
        self.pow = 1

    def __add__(self, other):
        return Polinome((self, other), ops=['+'])


class Polinome(list):
    def __init__(self, *args, ops=[]):
        super().__init__(*args)
        self.ops = ops


a = Variable('a')
b = Variable('b')

print(a + b)
