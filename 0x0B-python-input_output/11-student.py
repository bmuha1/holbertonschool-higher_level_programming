#!/usr/bin/python3
"""
This is the Student module.

The Student module defines the Student class.
"""


class Student:
    """Represents a Student."""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve a dictionary representation of a Student."""
        return self.__dict__
