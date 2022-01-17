from unittest import TestCase
import game


class TestMakeCharacter(TestCase):
    def test_make_character(self):
        actual = game.make_character()

        expected = {'X-coordinate': 1, 'Y-coordinate': 1, 'Level': 1, 'EXP': 0, 'EXP needed': 30, 'title': '',
                    'domain': ''}
        self.assertEqual(actual, expected)
