#!/usr/bin/python3
"""
This is the "is kind of class" module.

The is kind of class module supplies one function, is_kind_of_class().
"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of, or an instance of a class
    that inherited from, the specified class."""
    return isinstance(obj, a_class)
