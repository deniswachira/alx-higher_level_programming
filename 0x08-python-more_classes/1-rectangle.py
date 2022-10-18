#!/usr/bin/python3
"""
File: 1-rectangle.py

Author: Samson Tedla <samitedla23@gmail.com>

Defines a class that represents a rectangle
"""


class Rectangle:
    """
    A class that represents a rectangle
    """

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle

        Args:
        width (int): width of rectangle
        height (int): height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set height of a rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
