#!/usr/bin/python3
class BaseGeometry:
    """Represents a BaseGeometry."""
    pass

    def area(self):
        """Raise an exception."""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validate value."""
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    """Represents a Rectangle."""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __repr__(self):
        """Print the width and height of the rectangle."""
        return '[Rectangle] ' + str(self.__width) + '/' + str(self.__height)

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height


class Square(Rectangle):
    """Represents a Square."""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
