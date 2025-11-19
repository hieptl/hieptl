#!/usr/bin/env python3
"""
Simple tests for the add_numbers module.
"""

import unittest
from add_numbers import add_numbers


class TestAddNumbers(unittest.TestCase):
    """Test cases for the add_numbers function."""
    
    def test_positive_numbers(self):
        """Test adding positive numbers."""
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(10, 15), 25)
    
    def test_negative_numbers(self):
        """Test adding negative numbers."""
        self.assertEqual(add_numbers(-2, -3), -5)
        self.assertEqual(add_numbers(-10, 5), -5)
    
    def test_zero(self):
        """Test adding with zero."""
        self.assertEqual(add_numbers(0, 5), 5)
        self.assertEqual(add_numbers(10, 0), 10)
        self.assertEqual(add_numbers(0, 0), 0)
    
    def test_decimal_numbers(self):
        """Test adding decimal numbers."""
        self.assertAlmostEqual(add_numbers(2.5, 3.7), 6.2)
        self.assertAlmostEqual(add_numbers(0.1, 0.2), 0.3)


if __name__ == "__main__":
    unittest.main()