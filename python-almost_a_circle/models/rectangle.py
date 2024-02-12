#!/usr/bin/python3
"""This is a 'rectangle' module"""


from models.base import Base


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

    def __getattr__(self, name):
        return self.__dict__[f"__{name}"]

    def __setattr__(self, name, value):
        self.__dict__[f"__{name}"] = value
