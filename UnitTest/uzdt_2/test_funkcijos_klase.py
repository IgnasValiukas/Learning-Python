import unittest
from funkcijos_klase import Funkcijos


class TestFunkcijosKlase(unittest.TestCase):
    def setUp(self):
        self.object = Funkcijos()

    def test_3_number_sum(self):
        self.assertEqual(self.object.sum_number(1, 2, 3), 6)
        self.assertEqual(self.object.sum_number(100, 0, -1), 99)
        self.assertEqual(self.object.sum_number(-1, 2, -3), -2)
        self.assertEqual(self.object.sum_number(0, 0, 0), 0.0)
        self.assertEqual(self.object.sum_number(-5, 6, -1), 0.0)
        self.assertEqual(self.object.sum_number(10.5, 20, -10), 20.5)
        self.assertEqual(self.object.sum_number(-6.5, 6, "7"), "Type must be Integer or Float!")
        self.assertEqual(self.object.sum_number(-6.5, 6, "String"), "Type must be Integer or Float!")

    def test_sum_list_numbers(self):
        self.assertEqual(self.object.sum_list([1, 2, 3]), 6)
        self.assertEqual(self.object.sum_list([-1, -2, - 3]), -6)
        self.assertEqual(self.object.sum_list([2.5, 2.75, 0.75]), 6)
        self.assertEqual(self.object.sum_list([2.5, 2.5, 1, -1, 1]), 6)
        self.assertEqual(self.object.sum_list([2.5, 2.5, 1, -1, 1, "8"]), "Type must be Integer or Float!")
        self.assertEqual(self.object.sum_list([2.5, 2.5, 1, -1, 1, "String"]), "Type must be Integer or Float!")

    def test_largest_number(self):
        self.assertEqual(self.object.find_max(1, 4, 5, 32, 6, 7, 33, 23, 5), 33)
        self.assertEqual(self.object.find_max(1, 4, 5, 32.9, 6, 7, 33.1, 23.2, 5), 33.1)
        self.assertEqual(self.object.find_max(1, 4, 5, 32, 6, 7, -33, 23, 5), 32)
        self.assertEqual(self.object.find_max(-1, -4, -5, -32, -6, -7, -33, -23, -5), -1)
        self.assertEqual(self.object.find_max(-0.1, -4, -5, -32, -6, -7, -33, -23, -0.12), -0.1)
        self.assertEqual(self.object.find_max(1, 4, 5, "32", 6, 7, "33", 23, 5), "Type must be Integer or Float!")

    def test_string_reverse(self):
        self.assertEqual(self.object.reverse_string("Word"), "droW")
        self.assertEqual(self.object.reverse_string("Regular Expressions"), "snoisserpxE ralugeR")
        self.assertEqual(self.object.reverse_string("!@#$%^&*()_+{}[]/.,:';~`"), "`~;':,./][}{+_)(*&^%$#@!")
        self.assertEqual(self.object.reverse_string("123456789"), "987654321")
        self.assertEqual(self.object.reverse_string("Hi user@2346!"), "!6432@resu iH")
        self.assertEqual(self.object.reverse_string(['User', 'Hello']), ['Hello', 'User'])
        self.assertEqual(self.object.reverse_string(('User', 'Hello')), ('Hello', 'User'))
        self.assertEqual(self.object.reverse_string({'User': "Tom", 'Age': "23"}),
                         f"Action is not valid with type: {type({'User': "Tom", 'Age': "23"})}")
        self.assertEqual(self.object.reverse_string(12), "Type must be String!")
        self.assertEqual(self.object.reverse_string(5.5), "Type must be String!")
