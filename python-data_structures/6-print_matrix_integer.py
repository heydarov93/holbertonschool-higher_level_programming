#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        size = len(i)
        for j in range(size):
            print("{:d}".format(i[j]), end=" " if j != size - 1 else "")
        print()
