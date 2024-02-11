#!/usr/bin/python3
"""This is '0-read_file' module"""


def read_file(filename=""):
    """Opens file, reads it and prints to stdout"""

    with open(filename, "r", encoding="utf-8") as afile:
        for aline in afile:
            print(aline, end="")
