#!/usr/bin/python3
"""This is a "8-rectangle" module"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class based on BaseGeometry base class"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"

    def area(self):
        return self.__width * self.__height
