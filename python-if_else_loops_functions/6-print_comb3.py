#!/usr/bin/python3
for dec in range(9):
    for unit in range((dec + 1), 10):
        if dec != 8 or unit != 9:
            print("{}{}, ".format(dec, unit), end="")
        else:
            print("{}{}".format(dec, unit))
