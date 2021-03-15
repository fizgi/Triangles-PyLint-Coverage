""" The primary goal of this file is to demonstrate a simple unittest implementation

    author: @fizgi
    date: 15-Mar-2021
    python: v3.9.2
"""

import unittest
from triangles import classify_triangle


class TestTriangles(unittest.TestCase):
    """ Test class of the methods """

    def test_right_triangle(self):
        """ Test methods for Right [Scalene, Isosceles] triangle """
        self.assertEqual(classify_triangle(3, 4, 5), 'Right Scalene')
        self.assertEqual(classify_triangle(10, 6, 8), 'Right Scalene')
        self.assertEqual(classify_triangle(24, 25, 7), 'Right Scalene')

        self.assertEqual(classify_triangle(5, 5, 7.07106781187), 'Right Isosceles')
        self.assertEqual(classify_triangle(8, 11.313708499, 8), 'Right Isosceles')
        self.assertEqual(classify_triangle(14.1421356237, 10, 10), 'Right Isosceles')

    def test_equilateral_triangle(self):
        """ Test methods for Equilateral triangle """
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral', '1,1,1 is equilateral')
        self.assertEqual(classify_triangle(5, 5, 5), 'Equilateral', '5,5,5 is equilateral')
        self.assertEqual(classify_triangle(10, 10, 10), 'Equilateral', '10,10,10 is equilateral')

    def test_isosceles_triangle(self):
        """ Test methods for Isosceles triangle """
        self.assertEqual(classify_triangle(2, 2, 3), 'Isosceles', '2,2,4 is Isosceles')
        self.assertEqual(classify_triangle(3, 5, 3), 'Isosceles', '3,5,3 is Isosceles')
        self.assertEqual(classify_triangle(4, 6, 6), 'Isosceles', '4,6,6 is Isosceles')

    def test_scalene_triangle(self):
        """ Test methods for Scalene triangle """
        self.assertEqual(classify_triangle(4, 5, 6), 'Scalene', '4,5,6 is Scalene')
        self.assertEqual(classify_triangle(6, 5, 4), 'Scalene', '6,5,4 is Scalene')
        self.assertEqual(classify_triangle(5, 4, 6), 'Scalene', '5,4,6 is Scalene')
        self.assertEqual(classify_triangle(10, 11, 12), 'Scalene', '10,11,12 is Scalene')

    def test_not_a_triangle(self):
        """ Test methods for NotATriangle """
        self.assertEqual(classify_triangle(4, 7, 21), 'NotATriangle', '4,7,21 is not a triangle')
        self.assertEqual(classify_triangle(5, 1, 1), 'NotATriangle', '5, 1, 1 is not a triangle')
        self.assertEqual(classify_triangle(2, 6, 2), 'NotATriangle', '2,6,2 is not a triangle')
        self.assertEqual(classify_triangle(1, 1, 5), 'NotATriangle', '1,1,5 is not a triangle')

    def test_invalid_input(self):
        """ Test methods for InvalidInput """
        self.assertEqual(classify_triangle(-4, -6, -7), 'InvalidInput')
        self.assertEqual(classify_triangle(200, 200, -300), 'InvalidInput')
        self.assertEqual(classify_triangle(3, 'x', 4), 'InvalidInput')
        self.assertEqual(classify_triangle('x', 'y', 'z'), 'InvalidInput')
        self.assertEqual(classify_triangle('x', 1, -1), 'InvalidInput')
        self.assertEqual(classify_triangle(-4, 'y', 'z'), 'InvalidInput')


if __name__ == '__main__':
    unittest.main()
