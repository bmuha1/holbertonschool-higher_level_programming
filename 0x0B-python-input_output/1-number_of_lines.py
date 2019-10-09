#!/usr/bin/python3
"""
This is the "read file" module.

The read file module defines one function, read_file().
"""

def number_of_lines(filename=""):
    """Print the contents of a text file."""
    count = 0
    with open(filename, 'r') as f:
        for line in f:
            count += 1
    return count
