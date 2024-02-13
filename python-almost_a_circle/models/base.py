#!/usr/bin/python3
"""This is a 'base' module"""

import json


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

    def to_json_string(list_dictionaries):
        """
        Static method that returns the JSON string
        representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
