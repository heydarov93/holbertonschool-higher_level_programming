#!/usr/bin/python3
"""Document for Module"""


class Square:
    """Defines square"""

    def __init__(self, size=0):
        """Checks size and assigns it
        to private instance var
        """
        Square.checksize(size)
        self.__size = size

    def area(self):
        """calculates are of square object

        Return:
        - area of square object
        """
        return self.__size ** 2

    @property
    def size(self):
        """Retrieves the value of private size field"""
        return self.__size

    @size.setter
    def size(self, value):
        """Checks and assigns value to private instance size field"""
        Square.checksize(value)
        self.__size = value

    @classmethod
    def checksize(cls, size):
        """Checks size and raises exception
        if size doesn't fit expectations
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
