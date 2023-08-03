"""
Sample tests
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test calc module"""

    def test_add_numbers(self):
        """Test adding numbers"""
        x = 5
        y = 6
        res = calc.add(x, y)
        
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Test subtracting numbers"""
        x = 6
        y = 8
        res = calc.subtract(x, y)

        self.assertEqual(res, 2)
