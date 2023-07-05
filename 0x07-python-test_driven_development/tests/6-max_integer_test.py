#!/usr/bin/python3
# 6-max_integer_test.py
"""Unittests for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..]) """

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [2, 4, 6, 8]
        self.assertEqual(max_integer(ordered), 8)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [2, 1, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        max_at_beginning = [8, 6, 4, 2]
        self.assertEqual(max_integer(max_at_beginning), 8)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element = [5]
        self.assertEqual(max_integer(one_element), 5)

    def test_floats(self):
        """Test a list of floats."""
        floats = [3.57, 9.33, -18.13, 19.26, 8.10]
        self.assertEqual(max_integer(floats), 19.26)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [5.53, 16.1, -9, 12, 6.1]
        self.assertEqual(max_integer(ints_and_floats), 16.1)

    def test_string(self):
        """Test a string."""
        string = "Zebra"
        self.assertEqual(max_integer(string), 'r')  # the character with the highest ASCII value

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
