import unittest
from intermediate_test import (
    add_to_list,
    remove_from_list,
    insert_at_beginning,
    reverse_list,
    create_new_tuple,
    check_if_value_exists,
    find_intersection,
    find_union,
    find_difference,
    add_student,
    change_bob_grade,
    delete_charlie,
    retrieve_alice_grade
)

class TestIntermediateFunctions(unittest.TestCase):

    def test_add_to_list(self):
        self.assertEqual(add_to_list([1, 2, 3]), [1, 2, 3, 6])

    def test_remove_from_list(self):
        self.assertEqual(remove_from_list([1, 2, 3, 4]), [1, 2, 4])

    def test_insert_at_beginning(self):
        self.assertEqual(insert_at_beginning([1, 2, 3]), [0, 1, 2, 3])

    def test_reverse_list(self):
        self.assertEqual(reverse_list([1, 2, 3]), [3, 2, 1])

    def test_create_new_tuple(self):
        self.assertEqual(create_new_tuple((5, 10, 15, 20)), (5, 10))

    def test_check_if_value_exists(self):
        self.assertTrue(check_if_value_exists((5, 10, 15, 20), 15))
        self.assertFalse(check_if_value_exists((5, 10, 15, 20), 25))

    def test_find_intersection(self):
        set1 = {1, 2, 3, 4}
        set2 = {3, 4, 5, 6}
        self.assertEqual(find_intersection(set1, set2), {3, 4})

    def test_find_union(self):
        set1 = {1, 2, 3, 4}
        set2 = {3, 4, 5, 6}
        self.assertEqual(find_union(set1, set2), {1, 2, 3, 4, 5, 6})

    def test_find_difference(self):
        set1 = {1, 2, 3, 4}
        set2 = {3, 4, 5, 6}
        self.assertEqual(find_difference(set1, set2), {1, 2})

    def test_add_student(self):
        student_grades = {'Alice': 85, 'Bob': 90, 'Charlie': 78}
        self.assertEqual(add_student(student_grades), {'Alice': 85, 'Bob': 90, 'Charlie': 78, 'David': 92})

    def test_change_bob_grade(self):
        student_grades = {'Alice': 85, 'Bob': 90, 'Charlie': 78}
        self.assertEqual(change_bob_grade(student_grades), {'Alice': 85, 'Bob': 95, 'Charlie': 78})

    def test_delete_charlie(self):
        student_grades = {'Alice': 85, 'Bob': 90, 'Charlie': 78}
        self.assertEqual(delete_charlie(student_grades), {'Alice': 85, 'Bob': 90})

    def test_retrieve_alice_grade(self):
        student_grades = {'Alice': 85, 'Bob': 90, 'Charlie': 78}
        self.assertEqual(retrieve_alice_grade(student_grades), 85)

if __name__ == "__main__":
    unittest.main()
