#!/usr/bin/python3
"""
File: 4-print_square.py

By: Samson Tedla <samitedla23@gmail.com>

Defines a function that prints a square with #
"""


def print_square(size):
    """
    Prints a square with # of given size

    Args:
        size (int); size of square to be printed
    Raises:
        TypeError: if size is not an integer
        TypeError: if size is less than 0
        TypeError: if size is is float and is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size - 1):
            print("#", end="")
        print("#")
