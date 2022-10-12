#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """class that has a private instance attribute"""
    def __init__(self, size=None):
        """Initialize a new Square

        Args: size (int): size of Square
        """
        self.__size = size
