from unittest import TestCase
from Statistics import Statistics


class StatisticsTest(TestCase):
    def test_values(self):
        self.assertEqual(Statistics().values(""), [0, 0, 0, 0], "Cadena Vacía")

    def test_values_oneNumber(self):
        self.assertEqual(Statistics().values("1"), [1, 1, 1, 1], "Cadena Con un número")
        self.assertEqual(Statistics().values("5"), [1, 5, 5, 5], "Cadena Con un número")

    def test_values_twoNumbers(self):
        self.assertEqual(Statistics().values("1,2"), [2, 1, 2, 1.5], "Cadena Con dos números")
        self.assertEqual(Statistics().values("5,9"), [2, 5, 9, 7], "Cadena Con dos números")

    def test_values_NNumbers(self):
        self.assertEqual(Statistics().values("1,2,6,2"), [4, 1, 6, 2.75], "Cadena Con mas de dos números")
        self.assertEqual(Statistics().values("10,2,6,2,5,2,6"), [7, 2, 10, 4.7142857142857], "Cadena Con mas de dos números")

