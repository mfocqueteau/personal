""" Scientific Numbers """


def new_unit(name):
    """
    Returns a new UnitArray
    """
    return _UnitArray(_Unit(name))


class _Unit:
    """
    Basic structure for dimension units
    """

    def __init__(self, value='', exponent=1):
        self._value = value
        self.exponent = exponent

    def __mul__(self, other):
        if isinstance(other, _UnitArray):
            return other * self
        if not isinstance(other, _Unit):
            return SciNum(other, self)
        if self._value == other._value:
            return _UnitArray(_Unit(self._value, self.exponent + other.exponent))
        return _UnitArray(self, other)

    def __truediv__(self, other):
        other.exponent *= -1
        return self * other

    def __repr__(self):
        exp = f'^{self.exponent}' if self.exponent != 1 else ''
        return f'{self._value}{exp}'

    def __pow__(self, other):
        result = _Unit(self._value, self.exponent)
        result.exponent *= other
        return result

    def __eq__(self, other):
        if isinstance(other, _Unit):
            return (self._value, self.exponent) == (other._value, other.exponent)
        return False

    __rmul__ = __mul__
    __floordiv__ = __truediv__


class _UnitArray(list):
    """
    Keeps all the dimensions in a single place and manages operations
    """

    def __init__(self, *args):
        super().__init__(args)

    def __add__(self, other):
        if not isinstance(other, _UnitArray):
            raise ValueError
        if not self == other:
            self.sort()
            other.sort()
            raise ValueError(f'Dimensional error when trying to add: {self} + {other}')
        return self

    def __mul__(self, other):
        new = _UnitArray(*self)
        if not isinstance(other, _UnitArray):
            return SciNum(other, self)
        temp = _UnitArray(*other)
        if not new:
            return temp
        while temp:
            shared_unit = False
            cur = temp.pop()
            for i, unit in enumerate(new):
                if cur._value == unit._value:
                    new[i] = (new[i] * cur)[0]
                    shared_unit = True
                    break
            if not shared_unit:
                new.append(cur)
        new.clean()
        return new

    def __truediv__(self, other):
        if isinstance(other, _Unit):
            other = _UnitArray(other)
        return self * other**-1

    def __rtruediv__(self, other):
        return other * self**-1

    def __pow__(self, other):
        return _UnitArray(*tuple(unit**other for unit in self))

    def __eq__(self, other):
        if isinstance(other, _UnitArray):
            self.clean()
            other.clean()
            self_set = set((d._value, d.exponent) for d in self)
            other_set = set((d._value, d.exponent) for d in other)
            return self_set == other_set
        return False

    def __call__(self, power=1):
        return self ** power

    def __repr__(self):
        self.sort()
        return '[' + ' '.join(str(u) for u in self) + ']'

    def sort(self, reverse=False, key=lambda x: (x.exponent < 0, x._value)):
        """
        Sort the units in the _UnitArray object
        """
        super().sort(reverse=reverse, key=key)

    def clean(self):
        """
        Removes invalid or exponent 0 units from the array
        """
        for unit in self[::-1]:
            if unit.exponent == 0:
                self.remove(unit)

    __rmul__ = __mul__


class SciNum:
    """
    Scientific Numbers (magntiude and dimension)
    """

    def __init__(self, magnitude, units):
        self.magnitude = magnitude
        if isinstance(units, _Unit):
            units = _UnitArray(units)
        elif not isinstance(units, _UnitArray):
            raise ValueError('Units parameter must be of type _Unit or _UnitArray')
        self.units = units

    def __add__(self, other):
        if other == 0:
            return self
        if not isinstance(other, SciNum):
            raise TypeError
        return SciNum(self.magnitude + other.magnitude, self.units + other.units)

    def __sub__(self, other):
        if isinstance(other, SciNum):
            return self + SciNum(other.magnitude * -1, other.units)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return SciNum(self.magnitude * other, self.units)
        elif isinstance(other, _UnitArray):
            return SciNum(self.magnitude, self.units * other)
        return SciNum(self.magnitude * other.magnitude, self.units * other.units)

    def __truediv__(self, other):
        new = self * (other ** -1)
        new.units.clean()
        return new

    def __rtruediv__(self, other):
        return other * SciNum(self.magnitude ** -1, self.units ** -1)

    def __floordiv__(self, other):
        if not isinstance(other, SciNum):
            return SciNum(self.magnitude // other, self.units)
        return SciNum(self.magnitude // other.magnitude, self.units / other.units)

    def __rfloordiv__(self, other):
        if not isinstance(other, SciNum):
            return SciNum(other // self.magnitude, self.units ** -1)
        return SciNum(other.magnitude // self.magnitude, other.units / self.units)

    def __pow__(self, power):
        return SciNum(self.magnitude ** power, self.units ** power)

    def __eq__(self, other):
        if isinstance(other, SciNum):
            return (self.magnitude, self.units) == (other.magnitude, other.units)
        return False

    def __call__(self, exponent=1):
        return self ** exponent

    def __repr__(self):
        return f'{self.magnitude} {self.units}'

    __radd__ = __add__
    __rmul__ = __mul__


###########
#  Units  #
###########

# Time
s = new_unit('s')
h = new_unit('h')
d = new_unit('d')

# Length
m = new_unit('m')
mi = new_unit('mi')
ft = new_unit('ft')

# Mass
kg = new_unit('kg')
lb = new_unit('lb')

# Electric current
A = new_unit('A')

# Temperature
K = new_unit('K')
C = new_unit('C°')
F = new_unit('F°')

# Amount of substance
mol = new_unit('mol')

# Luminous intensity
cd = new_unit('cd')

# Compound units
N = kg * m / s**2
J = kg * m**2 / s**2
Pa = N / m**2
