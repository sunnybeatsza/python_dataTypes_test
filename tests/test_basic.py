import unittest
from basic_test import (
    int_division,
    float_multiplication,
    combine_operations,
    extract_word,
    to_lowercase,
    count_o,
    evaluate_boolean
)

class TestBasicFunctions(unittest.TestCase):

    def test_int_division(self):
        self.assertEqual(int_division(), 3)

    def test_float_multiplication(self):
        self.assertEqual(float_multiplication(), 6.0)

    def test_combine_operations(self):
        self.assertEqual(combine_operations(), 6.0)

    def test_extract_word(self):
        self.assertEqual(extract_word(), "awesome")

    def test_to_lowercase(self):
        self.assertEqual(to_lowercase(), "python is awesome!")

    def test_count_o(self):
        self.assertEqual(count_o(), 2)

    def test_evaluate_boolean(self):
        self.assertFalse(evaluate_boolean()) 

if __name__ == "__main__":
    unittest.main()
