#!/usr/bin/python3
"""
This is the BaseGeometry module.

The BaseGeometry module contains two functions, area() and integer_validator().
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


"""
This is the Rectangle module.

The Rectangle module defines the Rectangle class.
"""


class Rectangle(BaseGeometry):
    """Represents a Rectangle."""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
