
class vector(tuple):
    def __mul__(self, other):
        if isinstance(other, vector):
            assert len(self) == len(other)
            return vector(v * o for v, o in zip(self, other))
        if isinstance(other, (int, float)):
            return vector(v * other for v in self)
        raise TypeError

    def __add__(self, other):
        assert len(self) == len(other)
        return vector(v + o for v, o in zip(self, other))

    __rmul__ = __mul__
    __radd__ = __add__


def test():
    L = [2, 3, 5, 11, 13, 17, 19, 23]
    V = vector(L)
    print(V)
    print(L)


if __name__ == '__main__':
    test()
