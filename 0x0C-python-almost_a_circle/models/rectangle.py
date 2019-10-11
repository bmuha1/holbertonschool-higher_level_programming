#!/usr/bin/python3
"""
Define a Rectangle class.
"""
from models.base import Base


class Rectangle(Base):
    """Define a Rectangle class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle instance."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """Print the rectangle attributes."""
        return ('[Rectangle] (' + str(self.id) + ') ' + str(self.__x) + '/' +
                str(self.__y) + ' - ' + str(self.__width) + '/' +
                str(self.__height))

    def integer_validator(self, name, value):
        """Validate value."""
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0 and (name == 'width' or name == 'height' or
                           name == 'size'):
            raise ValueError('{} must be > 0'.format(name))
        if value < 0 and (name == 'x' or name == 'y'):
            raise ValueError('{} must be >= 0'.format(name))

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """Print the rectangle."""
        print('\n' * self.__y + (' ' * self.__x + '#' * self.__width + '\n') *
              self.__height, end='')

    def update(self, *args, **kwargs):
        """Update the rectangle: id, width, height, x, y."""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation of rectangle."""
        return {'id': self.id, 'width': self.__width, 'height': self.__height,
                'x': self.__x, 'y': self.__y}

    @property
    def width(self):
        """Get the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width."""
        self.integer_validator('width', value)
        self.__width = value

    @property
    def height(self):
        """Get the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height."""
        self.integer_validator('height', value)
        self.__height = value

    @property
    def x(self):
        """Get x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x."""
        self.integer_validator('x', value)
        self.__x = value

    @property
    def y(self):
        """Get y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y."""
        self.integer_validator('y', value)
        self.__y = value
