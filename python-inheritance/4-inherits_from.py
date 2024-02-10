#!/usr/bin/python3
"""
This is the "4-inherits_from" module.
"""


def inherits_from(obj, a_class):
    """inherits from"""
    if not type(obj) is a_class:
        return isinstance(obj, a_class)

    return False
