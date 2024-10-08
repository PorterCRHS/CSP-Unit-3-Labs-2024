import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../labs')))

from Lab1 import leapYear

class TestLab1(unittest.TestCase):

    def test_leapYear(self):
        self.assertEqual(isLeapYear(2000), True)
        self.assertEqual(isLeapYear(2001), False)
        self.assertEqual(isLeapYear(1900), False)
        self.assertEqual(isLeapYear(2004), True)
        self.assertEqual(isLeapYear(2008), True)  
        self.assertEqual(isLeapYear(2012), True)
        self.assertEqual(isLeapYear(2016), True)
        self.assertEqual(isLeapYear(2020), True)
        



if __name__ == '__main__':
    unittest.main()
