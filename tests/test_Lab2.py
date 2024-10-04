import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../labs')))

from Lab2 import getDiscountedPrice

class TestLab2(unittest.TestCase):

    def test_getDiscountedPrice(self):
        self.assertEqual(getDiscountedPrice(180), 180)
        self.assertEqual(getDiscountedPrice(2170), 1953.0)
        self.assertEqual(getDiscountedPrice(3100), 2790.0)
        self.assertEqual(getDiscountedPrice(9339), 8405.1)
        self.assertEqual(getDiscountedPrice(2001), 1800.9)
        


if __name__ == '__main__':
    unittest.main()