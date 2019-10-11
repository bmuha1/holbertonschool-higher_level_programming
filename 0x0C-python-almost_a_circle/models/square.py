#!/usr/bin/python3
"""
Define a Square class.
"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Define a Square class."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Print the square attributes."""
        return ('[Square] (' + str(self.id) + ') ' + str(self._Rectangle__x) +
                '/' + str(self._Rectangle__y) + ' - ' +
                str(self._Rectangle__width))

    def to_dictionary(self):
        """Return dictionary representation of square."""
        return {'id': self.id, 'size': self.size, 'x': self._Rectangle__x,
                'y': self._Rectangle__y}

    @property
    def size(self):
        """Get the size."""
        return self._Rectangle__width

    @size.setter
    def size(self, value):
        """Set the size."""
        self.integer_validator('size', value)
        self._Rectangle__width = value
        self._Rectangle__height = value

    def update(self, *args, **kwargs):
        """Update the square: id, size, x, y."""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self._Rectangle__x = args[2]
            if len(args) >= 4:
                self._Rectangle__y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
