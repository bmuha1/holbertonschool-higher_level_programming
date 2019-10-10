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

    def to_json(self, attrs=None):
        """Retrieve specified attributes of a Student."""
        if not attrs or type(attrs) != list:
            return self.__dict__
        my_attrs = {}
        for key in attrs:
            if key in self.__dict__.keys():
                my_attrs[key] = self.__dict__[key]
        return my_attrs
