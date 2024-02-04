#!/usr/bin/python3
"""
A module that contains add_integer function
"""


def add_integer(a, b=98):
    """
    Adds two integer
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
