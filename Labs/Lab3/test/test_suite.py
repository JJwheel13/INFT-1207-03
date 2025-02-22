# Authors: Justin Wheeler, Karim Mohammed
# Completion Date: 2025-02-21
# Purpose: To process and test the areas of circles, trapeziums, ellipses, and rhombuses.
# File: test_suite.py

# Import Libraries
import unittest

# Import Classes
from test_Lab3_Mohammed_Justin import TestShapes

# run_tests Function: Determines the user's selected shape for testing.
def run_tests(choice):
    suite = unittest.TestSuite()

    # Identify user's choice
    match choice:
        case "c":
            suite.addTest(TestShapes('test_circle_area_valid'))
            suite.addTest(TestShapes('test_circle_area_invalid'))
        case "t":
            suite.addTest(TestShapes('test_trapezium_area_valid'))
            suite.addTest(TestShapes('test_trapezium_area_invalid'))
        case "e":
            suite.addTest(TestShapes('test_ellipse_area_valid'))
            suite.addTest(TestShapes('test_ellipse_area_invalid'))
        case "r":
            suite.addTest(TestShapes('test_rhombus_area_valid'))
            suite.addTest(TestShapes('test_rhombus_area_invalid'))
        case _:
            print("Invalid choice. Exiting.")
            return

    # Execute Tests
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    # Greet User
    print("----- TEST-SUITE -----\nFile Identified: shape_area_calculator.py\n\nTest Options:\n- Circle: 'c'\n- Trapezium 't'\n- Ellipse 'e'\n- Rhombus 'r'\n")
    # Prompt User for Input, strip for matching
    choice = input("Please select an option: ").strip().lower()
    run_tests(choice)