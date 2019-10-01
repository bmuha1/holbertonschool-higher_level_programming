#!/usr/bin/python3
class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initializes the data"""
        self.size = size

    @property
    def size(self):
        """Get the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size"""
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Return the area of the square"""
        return self.__size**2

    def my_print(self):
        """Print the square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print('#' * self.__size)
