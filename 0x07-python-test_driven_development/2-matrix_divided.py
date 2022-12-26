#!/usr/bin/python3

"""a function that divides all elements of a matrix."""

def matrix_divided(matrix, div):
    matrix2 = []
    l = len(matrix[0])
    for row in matrix:
        row2 = []
        if len(row) != l:
            raise TypeError('Each row of the matrix must have the same size')
        for value in row:
            if not isinstance(value, int) or isinstance(value, float):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
            if not isinstance(div, int) or isinstance(div, float):
                raise TypeError('div must be a number')
            if div == 0:
                raise ZeroDivisionError('division by zero')
            row2.append(round(value / div, 2))
        matrix2.append(row2)
    return matrix2
