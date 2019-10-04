#!/usr/bin/python3
"""
This is the "matrix mul" module.

The matrix mul module supplies one function, matrix_mul().
"""


def matrix_mul(m_a, m_b):
    """
    Return the product of two matrices.
    """

    if type(m_a) is not list:
        raise TypeError('m_a must be a list')
    if type(m_b) is not list:
        raise TypeError('m_b must be a list')

    for row in m_a:
        if type(row) is not list:
            raise TypeError('m_a must be a list of lists')
    for row in m_b:
        if type(row) is not list:
            raise TypeError('m_b must be a list of lists')

    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        if len(row) == 0:
            raise ValueError("m_a can't be empty")
    for row in m_b:
        if len(row) == 0:
            raise ValueError("m_b can't be empty")

    for row in m_a:
        for col in row:
            if type(col) is not int and type(col) is not float:
                raise TypeError('m_a should contain only integers or floats')
    for row in m_b:
        for col in row:
            if type(col) is not int and type(col) is not float:
                raise TypeError('m_b should contain only integers or floats')

    for row in m_a:
        if len(row) != len(m_a[0]):
            raise TypeError('each row of m_a must be of the same size')
    for row in m_b:
        if len(row) != len(m_b[0]):
            raise TypeError('each row of m_b must be of the same size')

    rowsA = len(m_a)
    colsA = len(m_a[0])
    rowsB = len(m_b)
    colsB = len(m_b[0])

    if colsA != rowsB:
        raise ValueError("m_a and m_b can't be multiplied")

    new = [[0 for row in range(colsB)] for col in range(rowsA)]
    for i in range(rowsA):
        for j in range(colsB):
            for k in range(colsA):
                new[i][j] += m_a[i][k] * m_b[k][j]
    return new
