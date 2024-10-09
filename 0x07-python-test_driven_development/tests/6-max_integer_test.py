#!/usr/bin/python3
"""Unittest for max_integer([..]) function.
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define unittests for the max_integer function."""

    def test_max_at_end(self):
        """Test when the max integer is at the end of the list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_in_middle(self):
        """Test when the max integer is in the middle of the list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_single_element(self):
        """Test when the list has a single element."""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Test when the list is empty."""
        self.assertEqual(max_integer([]), None)

    def test_max_at_beginning(self):
        """Test when the max integer is at the beginning of the list."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_all_negative(self):
        """Test a list with all negative integers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_signs(self):
        """Test a list with both negative and positive integers."""
        self.assertEqual(max_integer([-10, 5, 3, -2]), 5)

    def test_duplicates(self):
        """Test a list with duplicates."""
        self.assertEqual(max_integer([1, 3, 3, 2]), 3)

    def test_floats_in_list(self):
        """Test a list containing floats and integers."""
        self.assertEqual(max_integer([1, 3.5, 2, 5.7]), 5.7)

    def test_string_input(self):
        """Test when the input is a string."""
        with self.assertRaises(TypeError):
            max_integer("string")

    def test_none_input(self):
        """Test when the input is None."""
        with self.assertRaises(TypeError):
            max_integer(None)

if __name__ == "__main__":
    unittest.main()
