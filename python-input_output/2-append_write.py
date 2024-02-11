#!/usr/bin/python3
"""This is a ''2-append_write' module"""


def append_write(filename="", text=""):
    """opens file and appends into it"""

    with open(filename, "a", encoding="utf-8") as afile:
        return afile.write(text)
