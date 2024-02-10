#!/usr/bin/python3
"""This is a "10-square" module"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """The Square class inherits _from Rectangle class"""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
