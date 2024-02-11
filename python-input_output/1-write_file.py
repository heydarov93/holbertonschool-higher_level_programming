#!/usr/bin/python3
"""This is a '1-write_file' module"""


def write_file(filename="", text=""):
    """
    opens file and writes into it by overwriting the content
    if it already exists
    """
    with open(filename, "w", encoding="utf-8") as afile:
        return afile.write(text)
