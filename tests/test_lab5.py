import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../labs')))

from Lab5 import calcFedIncTax

class TestLab5(unittest.TestCase):

    def test_calcFedIncTax(self):
        self.assertEqual(calcFedIncTax(5000), "The federal income tax for a taxable income of $5,000 is 500.")
        self.assertEqual(calcFedIncTax(20000), "The federal income tax for a taxable income of $20,000 is 2538.")
        self.assertEqual(calcFedIncTax(50000), "The federal income tax for a taxable income of $50,000 is 8293.")
        self.assertEqual(calcFedIncTax(100000 ), "The federal income tax for a taxable income of $100,000 is 21071.")
        self.assertEqual(calcFedIncTax(400000 ), "The federal income tax for a taxable income of $400,000 is 112606.")
        self.assertEqual(calcFedIncTax(412000  ), "The federal income tax for a taxable income of $412,000 is 119576.")
        self.assertEqual(calcFedIncTax(500000  ), "The federal income tax for a taxable income of $500,000 is 154369.")

if __name__ == '__main__':
    unittest.main()
