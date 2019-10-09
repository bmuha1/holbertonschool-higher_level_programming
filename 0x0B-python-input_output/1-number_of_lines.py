#!/usr/bin/python3
"""
This is the "number of lines" module.

The number of lines module defines one function, number_of_lines().
"""

def number_of_lines(filename=""):
    """Print the contents of a text file."""
    count = 0
    with open(filename, 'r') as f:
        for line in f:
            count += 1
    return count
