import unittest
import funkcijos


class TestFunctions(unittest.TestCase):
    def test_3_number_sum(self):
        self.assertEqual(6, funkcijos.sum_number(1, 2, 3))
        self.assertEqual(99, funkcijos.sum_number(100, 0, -1))
        self.assertEqual(-6, funkcijos.sum_number(-1, -2, -3))
        self.assertEqual(0, funkcijos.sum_number(-5, 6, -1))
        self.assertEqual(20.5, funkcijos.sum_number(10.5, 20, -10))
        self.assertEqual("Type must be Integer or Float!", funkcijos.sum_number(-6.5, 6, "7"))
        self.assertEqual("Type must be Integer or Float!", funkcijos.sum_number(-6.5, 6, "String"))

    def test_sum_list_numbers(self):
        self.assertEqual(6, funkcijos.sum_list([1, 2, 3]))
        self.assertEqual(-6, funkcijos.sum_list([-1, -2, -3]))
        self.assertEqual(6, funkcijos.sum_list([2.5, 2.75, 0.75]))
        self.assertEqual(6, funkcijos.sum_list([2.5, 2.5, 1, -1, 1]))
        self.assertEqual("Type must be Integer or Float!", funkcijos.sum_list([2.5, 2.5, 1, -1, 1, "8"]))
        self.assertEqual("Type must be Integer or Float!", funkcijos.sum_list([2.5, 2.5, 1, -1, 1, "String"]))

    def test_largest_number(self):
        self.assertEqual(33, funkcijos.find_max(1, 4, 5, 32, 6, 7, 33, 23, 5))
        self.assertEqual(33.1, funkcijos.find_max(1, 4, 5, 32.9, 6, 7, 33.1, 23.2, 5))
        self.assertEqual(32, funkcijos.find_max(1, 4, 5, 32, 6, 7, -33, 23, 5))
        self.assertEqual(-1, funkcijos.find_max(-1, -4, -5, -32, -6, -7, -33, -23, -5))
        self.assertEqual(-0.1, funkcijos.find_max(-0.1, -4, -5, -32, -6, -7, -33, -23, -0.12))
        self.assertEqual("Type must be Integer or Float!", funkcijos.find_max(1, 4, 5, "32", 6, 7, "33", 23, 5))

    def test_string_reverse(self):
        self.assertEqual("droW", funkcijos.reverse_string("Word"))
        self.assertEqual("snoisserpxE ralugeR", funkcijos.reverse_string("Regular Expressions"))
        self.assertEqual("`~;':,./][}{+_)(*&^%$#@!", funkcijos.reverse_string("!@#$%^&*()_+{}[]/.,:';~`"))
        self.assertEqual("987654321", funkcijos.reverse_string("123456789"))
        self.assertEqual("!6432@resu iH", funkcijos.reverse_string("Hi user@2346!"))
        self.assertEqual(['Hello', 'User'], funkcijos.reverse_string(['User', 'Hello']))
        self.assertEqual(('Hello', 'User'), funkcijos.reverse_string(('User', 'Hello')))
        self.assertEqual(f"Action is not valid with type: {type({'User': "Tom", 'Age': "23"})}",
                         funkcijos.reverse_string({'User': "Tom", 'Age': "23"}))
        self.assertEqual("Type must be String!", funkcijos.reverse_string(12))
        self.assertEqual("Type must be String!", funkcijos.reverse_string(5.5))
