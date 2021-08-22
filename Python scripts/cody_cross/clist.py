def gen_clist(my_list):
    """ Retorna cíclicamente los elementos de una lista """
    while True:
        for item in my_list:
            yield item
