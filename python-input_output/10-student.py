#!/usr/bin/python3
"""This is a '9-student' module"""


class Student:
    """defines a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        dict_list = self.__dict__.items()
        if type(attrs) is list and all(type(i) is str for i in attrs):
            return {
                    key: value for key, value in dict_list if key in attrs
                    }

        return self.__dict__
