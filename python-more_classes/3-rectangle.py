#!/usr/bin/python3
"""A Module Rectangle that defines a rectangle class"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initializes object"""
        self.width = width
        self.height = height

    def __str__(self):
        if self.width == 0:
            return ""

        for i in range(self.height):
            print("#" * self.width, end="" if i == self.height - 1 else "\n")
        return ""

    @property
    def width(self):
        """Retrieves private instance attribute width"""
        return self.__width

    @property
    def height(self):
        """Retrieves private instance attribute height"""
        return self.__height

    @width.setter
    def width(self, value):
        """Sets private instance attr. width"""
        self.checkvalue("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets private instance attr. height"""
        self.checkvalue("height", value)
        self.__height = value

    @staticmethod
    def checkvalue(attname, value):
        """Checks value and raises exception if there is a mistake"""
        if not isinstance(value, int):
            raise TypeError(f"{attname} must be an integer")
        if value < 0:
            raise ValueError(f"{attname} must be >= 0")

    def area(self):
        """Measures and returns the rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """Measures and returns the rectangle perimeter"""
        if 0 in {self.width, self.height}:
            return 0
        return (self.width + self.height) * 2
