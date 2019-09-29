from unittest import TestCase
from Statistics import Statistics

class StatisticsTest(TestCase):
    def test_values(self):
        self.assertEqual(Statistics().values(""), [], "Cadena Vacía")
