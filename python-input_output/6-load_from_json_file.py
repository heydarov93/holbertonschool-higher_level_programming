#!/usr/bin/python3
"""This is a '6-load_from_json_file' module"""


import json


def load_from_json_file(filename):
    """creates an Object from a 'JSON file'"""

    with open(filename, "r", encoding="utf-8") as afile:
        return json.load(afile)
