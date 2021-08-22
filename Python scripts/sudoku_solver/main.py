from array import array
import sys


class Board(tuple):

    def __init__(self, init):
        super().__init__()
        self.initial_values = init

    def check_in_row(self, row, num) -> bool:
        return num in self[row]

    def check_in_column(self, col, num) -> bool:
        for row in self:
            if row[col] == num:
                return True
        return False

    def check_in_square(self, row, col, num) -> bool:
        first_row = 3 * (row // 3)
        first_col = 3 * (col // 3)
        for row in self[first_row:first_row+3]:
            if num in row[first_col:first_col+3]:
                return True
        return False

    def check_all(self, row, col, num) -> bool:
        return (
            self.check_in_row(row, num) or
            self.check_in_column(col, num) or
            self.check_in_square(row, col, num)
        )

    def insert(self, row, col, num) -> bool:
        if not self.check_all(row, col, num):
            self[row][col] = num
            return True
        else:
            return bool(self.initial_values[row][col])

    def __solve(self, row, col) -> None:
        for num in range(1, 10):
            if self.insert(row, col, num):
                col = (col + 1) % 9
                row = row if col else row + 1
                if (row, col) != (0, 0):
                    self.__solve(row, col)
            elif num == 9:
                self[row][col] = 0

    def solve(self): return self.__solve(0, 0)

    def __str__(self):
        def rep_row(row):
            return ' '.join((str(num) if num else '_' for num in row))
        # top, bottom = '─' * 17 + '¬' + '\n', '\n' + '─' * 18
        return '\n'.join('|' + rep_row(row) + '|' for row in self)

    def __repr__(self):
        for arr in self.values:
            print(arr)


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
print(BOARD)
BOARD.solve
print(BOARD)
