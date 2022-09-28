#!/usr/bin/python3


def weight_average(my_list=[]):
    '''function that returns the weighted average of all integers tuple'''
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)

    add = 0
    div = 0
    for tup in my_list:
        add += (tup[0] * tup[1])
        div += tup[1]
    return (add / div)

