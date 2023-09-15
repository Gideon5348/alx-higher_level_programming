#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_lists(self):
        """Test max_integer with regular lists."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([7, 2, 1, 8]), 8)
        self.assertEqual(max_integer([100, 1000, 10, 10000]), 10000)

    def test_empty_list(self):
        """Test max_integer with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test max_integer with negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)
        self.assertEqual(max_integer([-7, -2, -1, -8]), -1)
        self.assertEqual(max_integer([-100, -1000, -10, -10000]), -10)

    def test_mixed_numbers(self):
        """Test max_integer with mixed positive and negative numbers."""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([1, -3, 4, -2]), 4)
        self.assertEqual(max_integer([-7, 2, -1, -8]), 2)
        self.assertEqual(max_integer([100, -1000, 10, -10000]), 100)
