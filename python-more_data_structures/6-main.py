#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keylist = sorted(list(a_dictionary))
    for key in keylist:
        print(f"{key}: {a_dictionary[key]}")
