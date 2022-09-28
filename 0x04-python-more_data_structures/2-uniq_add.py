#!/usr/bin/python3


def uniq_add(my_list=[]):
    ''' function that adds all unique integers
    in a list (only once for each integer)'''
    unique = set(my_list)
    add = 0
    for i in unique:
        add += i
    return (add)
