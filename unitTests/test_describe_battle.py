from unittest import TestCase
import game
from unittest.mock import patch
import unittest.mock
import io


class TestDescribeBattle(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_battle_white_spacing_long_name(self, mock_response):
        test_character = {'HP cap': 160, 'Mana cap': 80, "name": "test character", 'Current HP': 100,
                          'Current Mana': 80, 'ATK': 160, 'DEF': 140, 'Level': 2}
        test_enemy = {"Name": "God Emperor Doom of the world!", 'class': 'boss', "Level": 8, "HP": 800, "ATK": 500,
                      "EXP given": 50}
        game.describe_battle(test_character, test_enemy)
        expected = f"""{'-' * 60}
God Emperor Doom of the world!{' ' * (40 - len("God Emperor Doom of the world!"))}test character
Level: 8{' ' * (40 - len('Level: 8'))}Level: 2
Foe HP: 800{' ' * (40 - len('Foe HP: 800'))}HP: 100/160  MANA: 80/80
{'-' * 60}
"""
        self.assertEqual(expected, mock_response.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_battle_white_spacing_short_name(self, mock_response):
        test_character = {'HP cap': 160, 'Mana cap': 80, "name": "test character", 'Current HP': 100,
                          'Current Mana': 80, 'ATK': 160, 'DEF': 140, 'Level': 2}
        test_enemy = {"Name": "al", 'class': 'boss', "Level": 8, "HP": 800, "ATK": 500,
                      "EXP given": 50}
        game.describe_battle(test_character, test_enemy)
        expected = f"""{'-' * 60}
{test_enemy['Name']}{' ' * (40 - len(test_enemy['Name']))}{test_character['name']}
Level: {test_enemy["Level"]}{' ' * (40 - len(f'Level: {test_enemy["Level"]}'))}Level: {test_character['Level']}
Foe HP: {test_enemy["HP"]}{' ' * (40 - len(f'Foe HP: {test_enemy["HP"]}'))}HP: {int(round(test_character['Current HP']))}/{test_character['HP cap']}  MANA: {test_character['Current Mana']}/{test_character['Mana cap']}
{'-' * 60}
"""
        self.assertEqual(expected, mock_response.getvalue())
