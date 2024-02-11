#!/usr/bin/python3
"""This is a '7-add_item' module"""

from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"

new_list_elements = argv[1:]

try:
    original_list = load_from_json_file(filename)
except FileNotFoundError:
    original_list = []

for item in new_list_elements:
    original_list.append(item)

save_to_json_file(original_list, filename)
