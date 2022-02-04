from array import array
import sys
import numpy as np


def new_generator(maximus):
    return range(maximus + 1)


MAXIMUS = 2 ** 24
my_array = array("I", new_generator(MAXIMUS))
my_list = list(new_generator(MAXIMUS))
my_nparray = np.array(new_generator(MAXIMUS))
print("array item:", my_array.itemsize)
array_size = sys.getsizeof(my_array)
list_size = sys.getsizeof(my_list)
nparray_size = sys.getsizeof(my_nparray)
print(array_size)
print(list_size)
print(nparray_size)
print("%i" % (100 * array_size // list_size) + "%")
