#!/usr/bin/python3
"""Define a class called Square"""


class Square:
    """class with private instance attribute"""
    def __init__(self, size=0):
        """initialize  a new Square

        Args:
            size (int): size of the new Square.
        """
        self.size = size

    @property
    def size(self):
        """set the current size of the square"""

        return(self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Method to that returns the area based on the size"""
        return (self.__size ** 2)
