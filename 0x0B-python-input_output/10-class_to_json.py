#!/usr/bin/python3
"""
This is the "class to json" module.

The class to json module defines one function, class_to_json().
"""


def class_to_json(obj):
    """Return the dictionary description for JSON serialization of an object."""
    return obj.__dict__
