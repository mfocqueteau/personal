import csv
import sys

_, name, *args = sys.argv

FILE = open(f'boards/{name}.csv', 'r')
BOARD = csv.reader(FILE, delimiter=',', *args)

for i, row in enumerate(BOARD):
    for j, value in enumerate(row):
        if value != '_':
            print(f'cell{(i, j, int(value))}.')

FILE.close()
