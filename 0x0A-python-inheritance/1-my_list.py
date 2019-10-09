#!/usr/bin/python3
class MyList(list):
    """Represents a MyList."""

    def print_sorted(self):
        """Print the list in ascending order."""
        print(sorted(self))
