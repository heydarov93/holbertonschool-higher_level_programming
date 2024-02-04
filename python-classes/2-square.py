#!/usr/bin/python3
"""Square Module

This module defines a simple Square class
"""


class Square:
    """
    A class that defines a square.

    Attributes:
    - __size (:obj:int): Private instance attribute
    representing the size of the square.

    Methods:
    - __init__(self, size=0): Initializes a new instance
    of the Square class with an optional size.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Parameters:
        - size (int, optional): The size of the square. Defaults to 0.

        Checks:
        - size validation
        """
        Square.size_validation(self, size)
        self.__size = size

    def size_validation(self, size):
        """
        Initializes a new instance of the Square class.

        Parameters:
        - size (any): The size of the square to check.

        Raises:
        - TypeError: If size is not an integer.
        - ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
