import unittest
from advanced_test import (
    create_squares_of_evens,
    convert_to_dict,
    access_value_x,
    append_to_list_in_dict,
    convert_tuple_to_list_and_append
)

class TestAdvancedFunctions(unittest.TestCase):

    def test_create_squares_of_evens(self):
        self.assertEqual(create_squares_of_evens(), [4, 16, 36, 64, 100])

    def test_convert_to_dict(self):
        students = [('Alice', 85), ('Bob', 90), ('Charlie', 78), ('David', 92)]
        self.assertEqual(convert_to_dict(students), {'Alice': 85, 'Bob': 90, 'Charlie': 78, 'David': 92})

    def test_access_value_x(self):
        nested = {'a': [1, 2, 3], 'b': (4, 5), 'c': {'x': 10, 'y': 20}}
        self.assertEqual(access_value_x(nested), 10)

    def test_append_to_list_in_dict(self):
        nested = {'a': [1, 2, 3], 'b': (4, 5), 'c': {'x': 10, 'y': 20}}
        self.assertEqual(append_to_list_in_dict(nested), {'a': [1, 2, 3, 6], 'b': (4, 5), 'c': {'x': 10, 'y': 20}})

    def test_convert_tuple_to_list_and_append(self):
        nested = {'a': [1, 2, 3], 'b': (4, 5), 'c': {'x': 10, 'y': 20}}
        self.assertEqual(convert_tuple_to_list_and_append(nested), {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': {'x': 10, 'y': 20}})

if __name__ == "__main__":
    unittest.main()
