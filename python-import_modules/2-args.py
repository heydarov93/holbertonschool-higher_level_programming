#!/usr/bin/python3
from sys import argv


def print_args(argv):
    length = len(argv)
    if length < 2:
        print("0 arguments.")
        return
    word = "arguments" if length > 2 else "argument"
    print("{} {}:".format(length - 1, word))
    for i in range(1, length):
        print("{}: {}".format(i, argv[i]))


print_args(argv)
