#!/usr/bin/python3
"""This is a "8-rectangle" module"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class based on BaseGeometry base class"""

    def __init__(self, width, height):
        classname = self.__class__
        classname.integer_validator(self, "width", width)
        classname.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height
