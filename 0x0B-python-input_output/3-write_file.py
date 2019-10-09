#!/usr/bin/python3
"""
This is the "write file" module.

The write file module defines one function, write_file().
"""

def write_file(filename="", text=""):
    """Write a string to a text file."""
    with open(filename, 'w') as f:
        return f.write(str(text))
