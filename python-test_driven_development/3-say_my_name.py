#!/usr/bin/python3
"""
    Insert here module comment

    Write a function that prints My name is <first name> <last name>

    Prototype: def say_my_name(first_name, last_name=""):
    first_name and last_name must be strings otherwise,
    raise a TypeError exception with the message
    first_name must be a string or last_name must be a string
    You are not allowed to import any module

"""


def say_my_name(first_name, last_name=""):
    """ print my first and last name """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
