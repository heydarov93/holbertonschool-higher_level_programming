#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx >= 0 and idx < len(my_list):
        new = my_list[0:]
        new[idx] = element
        return new
    return my_list[0:]
