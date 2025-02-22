# Authors: Justin Wheeler, Karim Mohammad
# Completion Date: 2025-02-21
# Purpose: To process and test the areas of circles, trapeziums, ellipses, and rhombuses.
# File: Lab3_Mohammed_Justin

# Import Libraries
from math import pi

# circle_area Function: Takes a radius input, and returns the area of the circle.
def circle_area(r):
    if isinstance(r, (int, float)) and r >= 0:
        return pi * (r ** 2)
    else:
        raise ValueError("Invalid radius. Must be a non-negative number.")

# trapezium_area Function: Takes both bases and the height, and returns the area of the trapezium.
def trapezium_area(a, b, h):
    if all(isinstance(i, (int, float)) and i > 0 for i in [a, b, h]):
        return 0.5 * (a + b) * h
    else:
        raise ValueError("Invalid input. All values must be positive numbers.")

# ellipse_area Function: Takes both axis, and returns the area of the ellipse.
def ellipse_area(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)) and a > 0 and b > 0:
        return pi * a * b
    else:
        raise ValueError("Invalid input. Semi-major and semi-minor axes must be positive numbers.")

# rhombus_area Function: Takes both diagonals, and returns the area of the rhombus.
def rhombus_area(d1, d2):
    if isinstance(d1, (int, float)) and isinstance(d2, (int, float)) and d1 > 0 and d2 > 0:
        return 0.5 * d1 * d2
    else:
        raise ValueError("Invalid input. Diagonals must be positive numbers.")
