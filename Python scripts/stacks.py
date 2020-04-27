import sys


class stack(list):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        items = ', '.join(str(item) for item in self)
        return f'|{items} ←'

    def pop(self):
        return super().pop()

    def add(self, *obj):
        for e in obj:
            self.append(e)

    def insert(self, *args):
        raise AttributeError


s1 = stack()
for i in range(20):
    s1.add((2*i**2 - 3*i) % 21)
s1.add(0, 2)
l1 = list(s1)
print(sys.getsizeof(s1))
print(sys.getsizeof(l1))

print(s1)
print(l1)
