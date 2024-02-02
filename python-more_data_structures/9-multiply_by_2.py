#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newdict = a_dictionary.copy()
    for key in newdict:
        newdict[key] *= 2
    return newdict
