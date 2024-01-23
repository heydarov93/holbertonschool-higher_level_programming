#!/usr/bin/python3
for decimal in range(97, 123):
    if chr(decimal) != 'q' and chr(decimal) != 'e':
        print("{}".format(chr(decimal)), end="")
