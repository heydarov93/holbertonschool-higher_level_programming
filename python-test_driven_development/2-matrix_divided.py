#!/usr/bin/python3
"""
    Insert here module comment


    Write a function that divides all elements of a matrix.

    Prototype: def matrix_divided(matrix, div):
    matrix must be a list of lists of integers or floats,
    otherwise raise a TypeError exception with the message
    matrix must be a matrix (list of lists)
    of integers/floats

    Each row of the matrix must be of the same size,
    otherwise raise a TypeError exception
    with the message Each row of the matrix must have
    the same size

    div must be a number (integer or float),
    otherwise raise a TypeError exception
    with the message div must be a number

    div can’t be equal to 0, otherwise raise a
    ZeroDivisionError exception
    with the message division by zero

    All elements of the matrix should be divided by div,
    rounded to 2 decimal places
    Returns a new matrix
    You are not allowed to import any module
"""


def matrix_divided(matrix, div):
    """ Divide a matrix by a number div """
    list_error = "matrix must be a matrix (list of lists) of integers/floats"
    len_error = "Each row of the matrix must have the same size"
    div_int_error = "div must be a number"
    div_zero_error = "division by zero"
    new_matrix = []
    new_list = []
    if not matrix:
        raise TypeError(list_error)
    if type(div) is not int and type(div) is not float:
        raise TypeError(div_int_error)
    if div is 0:
        raise ZeroDivisionError(div_zero_error)
    longitud = len(matrix[0])
    for lista in matrix:
        if type(lista) is not list:
            raise TypeError(list_error)
        if len(lista) != longitud:
            raise TypeError(len_error)
        for item in lista:
            if type(item) is not int and type(item) is not float:
                raise TypeError(list_error)
            num = item / div
            new_list.append(round(num, 2))
        new_matrix.append(new_list)
        new_list = []
    return new_matrix
