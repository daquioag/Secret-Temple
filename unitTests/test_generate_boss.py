from unittest import TestCase
from unittest.mock import patch
import unittest.mock
import game


class TestGenerateBoss(TestCase):
    @patch('random.randint', return_value=1)
    def test_generate_boss_ultron(self, _):
        actual = game.generate_boss()
        expected = {"Name": "Galactus Ultron", 'class': 'boss', "Level": 7, "HP": 600, "ATK": 600, "EXP given": 50}
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=4)
    def test_generate_boss_thanos(self, _):
        actual = game.generate_boss()
        expected = {"Name": "Astral Regulator Thanos", 'class': 'boss', "Level": 7, "HP": 900, "ATK": 300,
                    "EXP given": 50}
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=9)
    def test_generate_boss_doom(self, _):
        actual = game.generate_boss()
        expected = {"Name": "God Emperor Doom", 'class': 'boss', "Level": 7, "HP": 800, "ATK": 400, "EXP given": 50}
        self.assertEqual(actual, expected)
