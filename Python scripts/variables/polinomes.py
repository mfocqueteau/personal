import itertools as it


class Variable(str):
    def __new__(cls, name, exp=1):
        obj = str.__new__(cls, name)
        obj.exp = exp
        return Monome(obj)

    def __str__(self):
        return self + ("" if self.exp == 1 else f"^{self.exp}")

    # def equals(self, other, name_only=True):
    #     if name_only:
    #         return self == other
    #     return self == other and self.exp == other.exp

    def __mul__(self, other: "Variable"):
        return Monome(self, other)

    def __pow__(self, other):
        return Variable(self, exp=other)


class Monome(tuple):
    def __new__(cls, *iterable, scale=1):
        obj = tuple.__new__(cls, sorted(iterable))
        obj.scale = scale
        return obj

    def __str__(self):
        str_scale = "" if self.scale == 1 else str(abs(self.scale))
        return str_scale + "".join(str(var) for var in self)

    def __eq__(self, other):
        if isinstance(other, Monome):
            for v1, v2 in it.zip_longest(sorted(self), sorted(other)):
                if v1 != v2 or v1.exp != v2.exp:
                    return False
            return True
        return False

    def __add__(self, other):
        return
        if self == other:
            return Polinome()

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        if isinstance(other, Monome):
            return Monome(self, other, scale=self.scale * other.scale)
        return Monome(self, scale=self.scale * other)

    def __pow__(self, other):
        return Monome(*(v**other for v in self), scale=self.scale**other)

    __radd__ = __add__
    __rmul__ = __mul__


class Polinome(tuple):
    def __str__(self):
        return " + ".join(str(mon) for mon in self)


x = Variable("x")
y = Variable("y")

print(x * y)
