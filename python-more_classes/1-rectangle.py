#!/usr/bin/python3
"""a class Rectangle that defines a rectangle"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """Initializes object"""
        self.width = width
        self.height = height

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
