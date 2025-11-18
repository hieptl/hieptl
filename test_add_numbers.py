#!/usr/bin/env python3
"""
Unit tests for the number addition programs.
"""

import unittest
from simple_add import add_numbers


class TestAddNumbers(unittest.TestCase):
    """Test cases for the add_numbers function."""
    
    def test_positive_integers(self):
        """Test addition of positive integers."""
        self.assertEqual(add_numbers(5, 3), 8)
        self.assertEqual(add_numbers(10, 20), 30)
    
    def test_negative_integers(self):
        """Test addition with negative integers."""
        self.assertEqual(add_numbers(-5, -3), -8)
        self.assertEqual(add_numbers(-10, 5), -5)
        self.assertEqual(add_numbers(10, -5), 5)
    
    def test_floating_point(self):
        """Test addition of floating point numbers."""
        self.assertAlmostEqual(add_numbers(3.5, 2.7), 6.2, places=1)
        self.assertAlmostEqual(add_numbers(0.1, 0.2), 0.3, places=1)
    
    def test_zero(self):
        """Test addition with zero."""
        self.assertEqual(add_numbers(0, 5), 5)
        self.assertEqual(add_numbers(5, 0), 5)
        self.assertEqual(add_numbers(0, 0), 0)
    
    def test_large_numbers(self):
        """Test addition of large numbers."""
        self.assertEqual(add_numbers(1000000, 2000000), 3000000)
        self.assertEqual(add_numbers(-1000000, 500000), -500000)


if __name__ == "__main__":
    unittest.main()