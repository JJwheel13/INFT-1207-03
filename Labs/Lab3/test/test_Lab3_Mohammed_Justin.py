# Authors: Justin Wheeler, Karim Mohammed
# Completion Date: 2025-02-21
# Purpose: To process and test the areas of circles, trapeziums, ellipses, and rhombuses.
# File: test_Lab3_Mohammed_Justin.py

# Import Libraries
import unittest
from math import pi

# Import Classes
from app.Lab3_Mohammed_Justin import circle_area, trapezium_area, ellipse_area, rhombus_area

class TestShapes(unittest.TestCase):

    # setUp Method: Notifies the user of a prepared test.
    def setUp(self):
        print("\nSetup: Preparing test...")

    # tearDown Method: Notifies the user of a test cleaning.
    def tearDown(self):
        print("Teardown: Cleaning up after test...")

    # Circle Area Tests
    def test_circle_area_valid(self):
        self.assertAlmostEqual(circle_area(3), pi * 9)
        self.assertAlmostEqual(circle_area(10), pi * 100)
        self.assertAlmostEqual(circle_area(0.0), 0)

    def test_circle_area_invalid(self):
        with self.assertRaises(ValueError):
            circle_area(-1)
        with self.assertRaises(ValueError):
            circle_area("abc")

    # Trapezium Area Tests
    def test_trapezium_area_valid(self):
        self.assertAlmostEqual(trapezium_area(4, 6, 5), 25)
        self.assertAlmostEqual(trapezium_area(2, 3, 4), 10)
        self.assertAlmostEqual(trapezium_area(0.1, 2.3, 6.8), 8.16)

    def test_trapezium_area_invalid(self):
        with self.assertRaises(ValueError):
            trapezium_area(-4, 6, 5)
        with self.assertRaises(ValueError):
            trapezium_area(4, "b", 5)

    # Ellipse Area Tests
    def test_ellipse_area_valid(self):
        self.assertAlmostEqual(ellipse_area(3, 7), pi * 21)
        self.assertAlmostEqual(ellipse_area(5, 2), pi * 10)
        self.assertAlmostEqual(ellipse_area(0.1, 4.6), 1.4451326206)

    def test_ellipse_area_invalid(self):
        with self.assertRaises(ValueError):
            ellipse_area(-3, 7)
        with self.assertRaises(ValueError):
            ellipse_area(3, "x")

    # Rhombus Area Tests
    def test_rhombus_area_valid(self):
        self.assertAlmostEqual(rhombus_area(8, 10), 40)
        self.assertAlmostEqual(rhombus_area(5, 6), 15)
        self.assertAlmostEqual(rhombus_area(0.1, 6.5), 0.325)

    def test_rhombus_area_invalid(self):
        with self.assertRaises(ValueError):
            rhombus_area(-5, 10)
        with self.assertRaises(ValueError):
            rhombus_area("d", 10)

# Execute Testing
if __name__ == "__main__":
    unittest.main()