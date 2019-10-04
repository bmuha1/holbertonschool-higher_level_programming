#!/usr/bin/python3
"""
This is the "lazy matrix mul" module.

The lazy matrix mul module supplies one function, lazy_matrix_mul().
"""


def lazy_matrix_mul(m_a, m_b):
    """
    Return the product of two matrices.
    """
    import numpy as np

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

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return np.array(m_a).dot(np.array(m_b))
