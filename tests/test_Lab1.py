import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../labs')))

from Lab1 import leapYear

class TestLab1(unittest.TestCase):

    def test_leapYear(self):
        self.assertEqual(leapYear(2000), True)
        self.assertEqual(leapYear(2001), False)
        self.assertEqual(leapYear(1900), False)
        self.assertEqual(leapYear(2004), True)
        self.assertEqual(leapYear(2008), True)  
        self.assertEqual(leapYear(2012), True)
        self.assertEqual(leapYear(2016), True)
        self.assertEqual(leapYear(2020), True)
        



if __name__ == '__main__':
    unittest.main()