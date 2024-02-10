#!/usr/bin/python3
"""This is a '5-base_geometry' module"""


class BaseGeometry:
    """BaseGeometry class document string"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not type(value) is int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
