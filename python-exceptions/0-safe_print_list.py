#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        for i in range(x):
            print(my_list[i], end="")
        return i if i == 0 else i + 1
    except IndexError:
        return i
    finally:
        print()
