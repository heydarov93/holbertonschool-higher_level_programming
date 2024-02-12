#!/usr/bin/python3
"""This is a 'rectangle' module"""


from .base import Base


class Rectangle(Base):
    """
    class Rectangle that inherits from Base
    Private instance attributes, each with its own
    public getter and setter:
    - __width -> width
    - __height -> height
    - __x -> x
    - __y -> y

    Class constructor:
    - def __init__(self, width, height, x=0, y=0, id=None):
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)

    def area(self):
        return self.width * self.height

    @staticmethod
    def check_type(field, value):
        if type(value) is not int:
            raise TypeError(f"{field} must be an integer")

    @staticmethod
    def check_size_value(field, value):
        if value <= 0:
            raise ValueError(f"{field} must be > 0")

    @staticmethod
    def check_coordnte_value(field, value):
        if value < 0:
            raise ValueError(f"{field} must be >= 0")

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, value):
        self.check_type("x", value)
        self.check_coordnte_value("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        self.check_type("y", value)
        self.check_coordnte_value("y", value)
        self.__y = value

    @width.setter
    def width(self, value):
        self.check_type("width", value)
        self.check_size_value("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        self.check_type("height", value)
        self.check_size_value("height", value)
        self.__height = value
