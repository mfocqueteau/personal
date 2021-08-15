import datetime
import pandas as pd
from collections import namedtuple

Session = namedtuple('Session', 'date pull_ups squats dips deadlifts rows push_ups')


def add_session(exercises):
    with open('data.csv', 'a') as file:
        file.write(f'\n{str(datetime.date.today())},{",".join(e for e in exercises)}')


def load_sessions():
    with open('data.csv', 'r') as file:
        return pd.read_csv(file, sep=';')


def test():
    data = load_sessions()
    print(data.columns)


if __name__ == '__main__':
    test()
