def gen_clist(my_list):
    """ Retorna cíclicamente los elementos de una lista """
    i = 0
    while True:
        yield my_list[i % len(my_list)]
        i += 1
