import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../labs')))

from Lab4 import determineQuadrant

class TestLab4(unittest.TestCase):

    def test_determineQuadrant(self):
        self.assertEqual(determineQuadrant(4, 2).strip(), "Quadrant 1")
        self.assertEqual(determineQuadrant(-3, 7).strip(), "Quadrant 2")
        self.assertEqual(determineQuadrant(5, 0).strip(), "0")
        self.assertEqual(determineQuadrant(0, -8).strip(), "Quadrant 4")
        self.assertEqual(determineQuadrant(-6, -4).strip(), "Quadrant 3")
        self.assertEqual(determineQuadrant(0, 9).strip(), "0")
        self.assertEqual(determineQuadrant(-10, 0).strip(), "0")
        self.assertEqual(determineQuadrant(1, -7).strip(), "Quadrant 4")


if __name__ == '__main__':
    unittest.main()