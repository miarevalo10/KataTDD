from unittest import TestCase
from Statistics import Statistics

class StatisticsTest(TestCase):
    def test_values(self):
        self.assertEqual(Statistics().values(""), [0], "Cadena Vacía")

    def test_values_oneNumber(self):
        self.assertEqual(Statistics().values("1"), [1], "Cadena Con un número")
        self.assertEqual(Statistics().values("5"), [1], "Cadena Con un número")

