"""
Unit tests for calculator.py
These tests run automatically in the CI/CD pipeline
"""

import unittest
from calculator import add, subtract, multiply, divide, power

class TestCalculator(unittest.TestCase):
    

    def test_add(self):
        """Test addition function"""
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)


    def test_subtract(self):
        """Test subtraction function"""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(9, 10), -1)
        self.assertEqual(subtract(0, 0), 0)


    def test_multiply(self):
        """Test multiplication function"""
        self.assertEqual(multiply(5, 3), 15)
        self.assertEqual(multiply(1, -3), -3)
        self.assertEqual(multiply(0, 10), 0)


    def test_divide(self):
        """Test division function"""
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(9, 3), 3)
        self.assertEqual(divide(-8, 4), -2)
        

    def test_divide_by_zero(self):
        """Test dividing by zero error function"""
        with self.assertRaises(ValueError):
            divide(10,0)


    def test_power(self):
        """Test power function"""
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 2), 25)
        self.assertEqual(power(100, 0), 1)


    if __name__ == '__main__':
        unittest.main()
