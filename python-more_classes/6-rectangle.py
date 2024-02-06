#!/usr/bin/python3
"""A Module Rectangle that defines a rectangle class"""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes object"""
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

    def __str__(self):
        """returns presentation of rectangle using # chars"""
        rect = ""
        if 0 in {self.width, self.height}:
            return rect

        for i in range(self.height):
            rect += "#" * self.width + ("\n" if i != self.height - 1 else "")
        return rect

    def __repr__(self):
        """
        representation of the rectangle to be able
        to recreate a new instance by using eval()
        """
        return f"{self.__class__.__name__}({self.width}, {self.height})"

    def __del__(self):
        self.__class__.number_of_instances -= 1
        print("Bye rectangle...")

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
