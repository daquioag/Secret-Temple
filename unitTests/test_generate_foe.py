from unittest import TestCase
import game
from unittest.mock import patch


class TestGenerateFoe(TestCase):
    @patch('random.randint', return_value=1)  # test the first number in the random randint range
    def test_generate_foe_hydra_agent(self, _):
        test_character = game.make_character()
        actual = game.generate_foe(test_character)
        expected = {'ATK': 120,
                    'EXP given': 20,
                    'HP': 100,
                    'Level': 2,
                    'Name': 'Hydra Agent',
                    'class': 'enemy'}
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=12)  # test the last number in the random randint range
    def test_generate_foe_Kree(self, _):
        test_character = game.make_character()
        actual = game.generate_foe(test_character)
        expected = {'ATK': 120,
                    'EXP given': 20,
                    'HP': 100,
                    'Level': 2,
                    'Name': 'Kree',
                    'class': 'enemy'}
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=6)  # test the middle number in the random randint range
    def test_generate_foe_dark_elf(self, _):
        test_character = game.make_character()
        actual = game.generate_foe(test_character)
        expected = {"Name": "Dark Elf", "Level": 2, "HP": 100, "ATK": 120,
                    "EXP given": 20, 'class': 'enemy'}

        self.assertEqual(actual, expected)
