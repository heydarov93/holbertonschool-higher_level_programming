#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not len(my_list):
        return
    print_reversed_list_integer(my_list[1:])
    print("{:d}".format(my_list[0]))
