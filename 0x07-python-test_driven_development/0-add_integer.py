#!/usr/bin/python3
"""
File: 0-add_integer.py

By: Samson Tedla <samitedla23@gmail.com>

Defines an integer addition function
"""


def add_integer(a, b=98):
    """
    Returns integer sum of 2 integers.
    
    Casts float to integer.

    Rasies TypeErrors if input is not integer or float.
    """
    if (not isinstance(a, float) and not isinstance(a, int)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, float) and not isinstance(b, int)):
        raise TypeError("b must be an integer")
    return int((a) + int(b))
