#!/usr/bin/python3
"""
This is the "pascal triangle" module.

The pascal triangle module defines one function, pascal_triangle().
"""


def pascal_triangle(n):
    """Return a list of integers representing Pascal's triangle of n."""
    list = []
    if n <= 0:
        return list
    for i in range(1, n + 1):
        value = 1
        temp_list = []
        for j in range(1, i + 1):
            temp_list.append(str(value))
            value = int(value * (i - j) / j)
        list.append(temp_list)
    return list
