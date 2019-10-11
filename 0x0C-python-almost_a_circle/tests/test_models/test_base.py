#!/usr/bin/python3
"""
Collection of tests for Base class.
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class BaseTest(unittest.TestCase):
    """Test Base methods."""

    def setUp(self):
        """Set up Base class tests."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Tidy up after test methods."""
        pass

    def test_id(self):
        """Test id."""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base(-1)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, -1)

    def test_to_json(self):
        """Test to_json_string method."""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(str(type(json_dictionary)), "<class 'str'>")

    def test_to_json_empty(self):
        """Test to_json_string method with empty and None."""
        json_dictionary = Base.to_json_string(None)
        self.assertEqual(json_dictionary, '[]')
        json_dictionary = Base.to_json_string([])
        self.assertEqual(json_dictionary, '[]')

    def test_to_json_empty(self):
        """Test to_json_string method with empty string."""
        json_dictionary = Base.to_json_string('')
        self.assertEqual(json_dictionary, '[]')

if __name__ == '__main__':
    unittest.main()
