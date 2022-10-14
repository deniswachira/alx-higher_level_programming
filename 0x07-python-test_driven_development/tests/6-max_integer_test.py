#!/usr/bin/python3
"""
File: 6-max_integer_test.py

Author: Samson Tedla <samitedla23@gmail.com>

Unittests for max_integer(list=[])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer(list=[])"""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element = [9]
        self.assertEqual(max_integer(one_element), 9)

    def test_floats(self):
        """Test a list of floats."""
        floats = [67.78, 9.123, -9.123, 67.7, 7.0]
        self.assertEqual(max_integer(floats), 67.78)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [10.55, 105.5, -98, 89, 98]
        self.assertEqual(max_integer(ints_and_floats), 105.5)

    def test_string(self):
        """Test a string."""
        string = "Samson"
        self.assertEqual(max_integer(string), 's')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["my", "name", "is", "samson"]
        self.assertEqual(max_integer(strings), "samson")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
