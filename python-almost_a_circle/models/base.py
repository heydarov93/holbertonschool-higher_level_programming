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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        dicts_list = []

        if list_objs is not None:
            for obj in list_objs:
                dicts_list.append(obj.to_dictionary())

        json_str = cls.to_json_string(dicts_list)

        filename = f"{cls.__name__}.json"
        with open(filename, "w", encoding="utf-8") as afile:
            afile.write(json_str)

    @classmethod
    def create(cls, **dictionary):
        """
        Class method that returns an instance with all attributes
        already set
        """
        dummy = cls(1, 1 if len(dictionary) > 1 else 0)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Class method that returns a list of instances
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r", encoding="utf-8") as afile:
                json_str = afile.read()
            dict_list = Base.from_json_string(json_str)
            instance_list = []
            for dictry in dict_list:
                obj = cls.create(**dictry)
                instance_list.append(obj)
            return instance_list
        except FileNotFoundError:
            return []

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Static method that returns the JSON string
        representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)
