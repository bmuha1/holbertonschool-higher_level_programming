#!/usr/bin/python3
"""
This is the "read file" module.

The read file module defines one function, read_file().
"""


def read_file(filename=""):
    """Print the contents of a text file."""
    with open(filename, 'r') as f:
        print(f.read(), end='')
