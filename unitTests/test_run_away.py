from unittest import TestCase
import game
from unittest.mock import patch
import unittest.mock
import io


class TestRunAway(TestCase):
    @patch('random.randint', return_value=10)
    def test_run_away_no_damage(self, _):
        test_sorcerer_character = {'Level': 1, 'Current HP': 200, 'Current Mana': 140, 'ATK': 200, 'DEF': 80,
                                   'HP cap': 200, 'Mana cap': 140}
        test_enemy = {"Name": "Kree", 'class': 'enemy', "Level": 2, "HP": 90, "ATK": 110}
        game.run_away(test_sorcerer_character, test_enemy)
        character_expected_hp = 200
        actual_hp = test_sorcerer_character["Current HP"]
        self.assertEqual(character_expected_hp, actual_hp)

    @patch('random.randint', return_value=1)  # formula for damage calculation is enemy['ATK'] * random.randint(1, enemy['Level']) / character["DEF"])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_run_away_take_damage(self, mock_stdout,  _):
        test_sorcerer_character = {'Level': 1, 'Current HP': 200, 'Current Mana': 140, 'ATK': 200, 'DEF': 80,
                                   'HP cap': 200, 'Mana cap': 140}
        test_enemy = {"Name": "Kree", 'class': 'enemy', "Level": 2, "HP": 90, "ATK": 110}
        game.run_away(test_sorcerer_character, test_enemy)
        character_expected_hp = 200 - 1
        actual_hp = test_sorcerer_character["Current HP"]
        expected_print_statement = """You run away!
Kree deals 1 damage you as you run away!\n\n"""
        self.assertEqual(character_expected_hp, actual_hp)
        self.assertEqual(expected_print_statement, mock_stdout.getvalue())

    @patch('random.randint', return_value=1)
    def test_run_away_enemy_unmodified(self, _):
        test_sorcerer_character = {'Level': 1, 'Current HP': 200, 'Current Mana': 140, 'ATK': 200, 'DEF': 80,
                                   'HP cap': 200, 'Mana cap': 140}
        test_enemy = {"Name": "Kree", 'class': 'enemy', "Level": 2, "HP": 90, "ATK": 110}
        game.run_away(test_sorcerer_character, test_enemy)
        enemy_unmodified = {"Name": "Kree", 'class': 'enemy', "Level": 2, "HP": 90, "ATK": 110}
        self.assertEqual(test_enemy, enemy_unmodified)
