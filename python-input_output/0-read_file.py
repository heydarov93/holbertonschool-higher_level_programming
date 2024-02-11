#!/usr/bin/python3
"""This is '0-read_file' module"""


def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as afile:
        print(afile.read().rstrip(), end="")
