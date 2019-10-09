#!/usr/bin/python3
"""
This is the "is same class" module.

The is same class module supplies one function, is_same_class().
"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of the specified class."""
    return type(obj) == a_class
