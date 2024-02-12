#!/usr/bin/python3
"""This is a 'base' module"""


class Base:
    """
    This class will be the “base” of all other classes
    in this project. The goal of it is to manage id attribute
    in all your future classes and to avoid duplicating the
    same code (by extension, same bugs)
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            __class__.__nb_objects += 1
            self.id = __class__.__nb_objects
