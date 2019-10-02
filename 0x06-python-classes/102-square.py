#!/usr/bin/python3
"""Define a square that handles comparators."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes the data."""
        self.size = size

    def __eq__(self, other):
        """Check if two squares are equal."""
        return self.__size == other.__size

    def __ne__(self, other):
        """Check if two squares are not equal."""
        return self.__size != other.__size

    def __lt__(self, other):
        """Check if square 1 is less than square 2."""
        return self.__size < other.__size

    def __le__(self, other):
        """Check if square 1 is less than or equal to square 2."""
        return self.__size <= other.__size

    def __gt__(self, other):
        """Check if square 1 is greater than square 2."""
        return self.__size > other.__size

    def __ge__(self, other):
        """Check if square 1 is greater than or equal to square 2."""
        return self.__size >= other.__size

    @property
    def size(self):
        """Get the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size."""
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size**2
