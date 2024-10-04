import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../labs')))

from Lab5 import calcFedIncTax

class TestLab5(unittest.TestCase):

    def test_calcFedIncTax(self):
        self.assertEqual(calcFedIncTax(5000), "The federal income tax for a taxable income of   $5,000 is 500.0.")
        


if __name__ == '__main__':
    unittest.main()