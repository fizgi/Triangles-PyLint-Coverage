""" The primary goal of this file is to demonstrate a simple python program to classify triangles

    author: @fizgi
    date: 15-Mar-2021
    python: v3.9.2
"""
import math


def classify_triangle(side_a, side_b, side_c):
    """ Determines the triangle type """
    try:
        side_a = float(side_a)  # if an input (A, B or C)
        side_b = float(side_b)  # can not be converted to float
        side_c = float(side_c)  # it will raise ValueError

        if not all(number > 0 for number in [side_a, side_b, side_c]):
            raise ValueError  # all sides should be greater than 0
        if (side_a + side_b <= side_c) or \
                (side_a + side_c <= side_b) or (side_b + side_c <= side_a):
            return 'NotATriangle'
    except ValueError:
        return 'InvalidInput'

    triangle_types = []  # store the triangles types (Right, Equilateral, Isosceles, Scalene)

    # Determine if the triangle is a right triangle
    # math.isclose() is a function that allows to compare
    # whether the given values are close enough to each other to be considered as equal
    if (math.isclose(side_a**2 + side_b**2,  side_c**2)) \
            or math.isclose(side_b ** 2 + side_c ** 2, side_a ** 2) \
            or math.isclose(side_c ** 2 + side_a ** 2, side_b ** 2):
        triangle_types.append('Right')

    # Determine if the triangle is equilateral, isosceles, or scalene
    if side_a == side_b == side_c:
        triangle_types.append('Equilateral')
    elif side_a == side_b or side_a == side_c or side_b == side_c:
        triangle_types.append('Isosceles')
    else:
        triangle_types.append('Scalene')

    return ' '.join(triangle_types)
