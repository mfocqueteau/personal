from __future__ import annotations


class TestTube(list):

    @property
    def top_color(self):
        if self:
            return self[-1]
        return None

    def push(self, color: str) -> None:
        self.append(color)

    def extract(self) -> str:
        return self.pop()

    def pour(self, other: TestTube) -> None:
        if other.top_color not in (self.top_color, None):
            return
        top_color = self.top_color
        while self and len(other) < 4:
            color = self.extract()
            if top_color == color:
                other.push(color)
            else:
                self.push(color)
                break

    def __str__(self) -> str:
        return f'({super().__str__()[1:]:>23}'


class Stage(dict):
    def __init__(self, *args) -> None:
        for i, tube in enumerate(args):
            self[i+1] = TestTube(tube)
        self[i+2] = TestTube()
        self[i+3] = TestTube()

    def __str__(self):
        result = 'Stage = {\n'
        for i, tube in self.items():
            result += f'{i:>4}: {tube}\n'
        return result + '}'


STAGE = Stage(
    ('cy', 're', 'ye', 'or'),
    ('gy', 'gy', 'gr', 'pu'),
    ('gy', 'gy', 'gr', 'gy'),
    ('gy', 'gy', 'gr', 'pu'),
    ('gy', 'gy', 'gr', 'dg'),
    ('gy', 'gy', 'gr', 'pu'),
    ('gy', 'gy', 'gr', 'pu'),
    ('gy', 'gy', 'gr', 'pu'),
    ('gy', 'gy', 'gr', 'pu'),
)

print(STAGE)
