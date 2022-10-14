#!/usr/bin/python3
"""
File: 3-say_my_name.py

By: Samson Tedla <samitedla23@gmail.com>

Defines a function that prints "My name is <first name> <last name>"
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>"

    Args:
        first_name (string): first name input
        last_name (string); last name input
    Raises:
        TypeError: if first_name is not a string
        TypeError: if last_namme is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
