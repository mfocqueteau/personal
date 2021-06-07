from array import array
import sys


class Board(tuple):

    def __init__(self, init):
        super().__init__()
        self.initial_values = init

    def check_in_row(self, row, num):
        assert 0 < row < 10
        assert 0 < num < 10
        return num in self[row-1]

    def check_in_column(self, col, num):
        assert 0 < col < 10
        assert 0 < num < 10
        for row in self:
            if row[col-1] == num:
                return True
        return False

    def check_in_square(self, row, col, num):
        assert 0 < row < 10
        assert 0 < col < 10
        assert 0 < num < 10
        first_row = 3*((row-1) // 3)
        first_col = 3*((col-1) // 3)
        for row in self[first_row:first_row+3]:
            if num in row[first_col:first_col+3]:
                return True
        return False

    def check_all(row, col, num):
        return (

        )

    def insert(self, num, row, col):
        assert 0 < num < 10
        assert 0 < row < 10
        assert 0 < col < 10
        if not (
            self.initial_values[row-1][col-1] or
            self.check_in_row(row, num) or
            self.check_in_column(col, num) or
            self.check_in_square(row, col, num)
        ):
            self[row-1][col-1] = num
            return True
        else:
            return False

    def __repr__(self):
        def rep_row(row):
            return ' '.join((str(num) if num else ' ' for num in row))
        # top, bottom = '─' * 17 + '¬' + '\n', '\n' + '─' * 18
        return '\n'.join('|' + rep_row(row) + '|' for row in self)


INITIAL = (
    array('B', (0, 0, 7, 9, 4, 0, 0, 0, 1)),
    array('B', (8, 0, 0, 0, 0, 5, 6, 0, 9)),
    array('B', (0, 9, 0, 0, 3, 0, 8, 0, 0)),
    array('B', (0, 0, 1, 3, 0, 7, 0, 6, 2)),
    array('B', (0, 3, 0, 0, 0, 0, 1, 0, 0)),
    array('B', (0, 8, 2, 0, 1, 6, 0, 0, 0)),
    array('B', (0, 0, 0, 0, 0, 9, 0, 5, 0)),
    array('B', (1, 7, 5, 8, 0, 0, 0, 0, 6)),
    array('B', (3, 0, 0, 0, 5, 0, 0, 0, 0))
)

BOARD = Board(INITIAL)
BOARD.insert(8, 7, 3)
BOARD.insert(8, 9, 3)
print(BOARD)
