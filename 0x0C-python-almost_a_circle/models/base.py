#!/usr/bin/python3
"""
Define a Base class.
"""
from os import path
import json
import csv


class Base:
    """Define a Base class."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if not list_dictionaries or list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation."""
        if not json_string or json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        filename = cls.__name__ + '.json'
        dictionary = []
        if list_objs is not None:
            dictionary = [obj.to_dictionary() for obj in list_objs]
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(dictionary))

    @classmethod
    def load_from_file(cls):
        """Return a list of instances."""
        filename = cls.__name__ + '.json'
        if path.isfile(filename):
            with open(filename, 'r') as f:
                dictionary = json.load(f)
            return [cls.create(**obj) for obj in dictionary]
        return []

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if cls.__name__ == 'Rectangle':
            new_base = cls(1, 1)
        else:
            new_base = cls(1)
        cls.update(new_base, **dictionary)
        return new_base

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV representation of list_objs to a file."""
        filename = cls.__name__ + '.csv'
        if list_objs is not None:
            if cls.__name__ == 'Rectangle':
                data = [[obj.id, obj.width, obj.height, obj.x, obj.y]
                        for obj in list_objs]
            else:
                data = [[obj.id, obj.size, obj.x, obj.y] for obj in list_objs]
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(data)

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of instances."""
        filename = cls.__name__ + '.csv'
        dictionary = []
        if path.isfile(filename):
            with open(filename, 'r', newline='') as f:
                reader = csv.reader(f)
                for row in reader:
                    if cls.__name__ == 'Rectangle':
                        data = {'id': int(row[0]), 'width': int(row[1]),
                                'height': int(row[2]), 'x': int(row[3]),
                                'y': int(row[4])}
                    else:
                        data = {'id': int(row[0]), 'size': int(row[1]),
                                'x': int(row[2]), 'y': int(row[3])}
                        dictionary.append(cls.create(**data))
        return dictionary
