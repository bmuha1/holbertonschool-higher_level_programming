#!/usr/bin/python3
"""Define a node in a singly linked list."""


class Node:
    """Represents a node in a linked list."""

    def __init__(self, data, next_node=None):
        """Initializes the data."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data."""
        if type(value) != int:
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """Get the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node."""
        if type(value) != Node and value is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list."""

    def __init__(self):
        """Initialize the linked list."""
        self.head = None

    def __repr__(self):
        string = ''
        curr = self.head
        while curr:
            string += str(curr.data) + '\n'
            curr = curr.next_node
        return string[:-1]

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position."""
        new_node = Node(value)
        curr = self.head
        if curr is None:
            self.head = new_node
            return
        if curr.data > value:
            new_node.next_node = self.head
            self.head = new_node
            return
        while curr.next_node is not None:
            if curr.next_node.data > value:
                break
            curr = curr.next_node
        new_node.next_node = curr.next_node
        curr.next_node = new_node
        return
