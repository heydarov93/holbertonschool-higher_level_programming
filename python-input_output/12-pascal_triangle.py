#!/usr/bin/python3
"""This is a '12-pascal_triangle' module"""


def pascal_triangle(n):
    """
    returns a list of lists of integers
    representing the Pascal’s triangle of n
    """

    if n <= 0:
        return list()

    arr = [[1]]

    for i in range(1, n):
        tmp = []
        idx = i - 1
        length = len(arr[idx])

        for num in range(length):
            try:
                if num == 0:
                    tmp.append(1)

                if num == length - 1:
                    tmp.append(1)

                tmp.append(arr[idx][num] + arr[idx][num + 1])
            except IndexError:
                arr.append(tmp)

    return arr
