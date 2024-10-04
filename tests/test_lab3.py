import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../labs')))

from Lab3 import isOdd

class TestLab3(unittest.TestCase):

    def test_isOdd(self):
        self.assertEqual(isOdd(2), False)
        self.assertEqual(isOdd(1), True)
        self.assertEqual(isOdd(3), True)
        self.assertEqual(isOdd(4), False)
        self.assertEqual(isOdd(11000005), True)
        self.assertEqual(isOdd(600), False)
        self.assertEqual(isOdd(107), True)


if __name__ == '__main__':
    unittest.main()