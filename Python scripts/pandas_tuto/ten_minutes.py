""" 10 minutes to pandas """
import numpy as np
import pandas as pd

# S = pd.Series(np.random.randn(5), index=['primero', 'segundo', 'tercero', 'cuarto', 'quinto'])
# print(S)

# Series puede instanciarse como dict()
DICT = {'b': 1, 'a': 0, 'c': 2}
SDICT = pd.Series(DICT, index=('b', 'd', 'c', 'a'))
print(SDICT.c)

DATES = pd.date_range('20201215', periods=6)
print(DATES)

DF1 = pd.DataFrame({
    'A': 1.,
    'B': pd.Timestamp('20130102'),
    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
    'D': np.array([3] * 4, dtype='int32'),
    'E': pd.Categorical(["test", "train", "test", "train"]),
    'F': 'foo'
})
print(DF1)
