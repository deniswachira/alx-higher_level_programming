#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    '''function that returns a new dictionary
    with all values multiplied by 2'''
    new_d = {i:j * 2 for (i, j) in a_dictionary.items()}
    return (new_d)
