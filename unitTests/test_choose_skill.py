from unittest import TestCase
import game
from unittest.mock import patch
import unittest.mock
import io


class TestChooseSkill(TestCase):
    @patch('builtins.input', side_effect=[9, 1])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_skill_runaway_from_boss(self, mock_response, _):
        all_skills = {'1': 'Punch', '2': 'King\'s Mercy', "3": "Vibranium Burst",
                      "4": "Ultimate Ability: Legacy of Odinson", '9': 'RUN AWAY!'}
        test_enemy = {"Name": "Galactus Ultron", 'class': 'boss', "Level": 8, "HP": 700, "ATK": 700, "EXP given": 50}
        game.choose_skill(all_skills, test_enemy)
        expected_print_statement = """What skill do you use?
[1]: Punch
[2]: King's Mercy
[3]: Vibranium Burst
[4]: Ultimate Ability: Legacy of Odinson
[9]: RUN AWAY!
You try and run away!
You cant escape a boss fight!
What skill do you use?
[1]: Punch
[2]: King's Mercy
[3]: Vibranium Burst
[4]: Ultimate Ability: Legacy of Odinson
You choose to Punch....
"""
        expected_skills_dictionary = {'1': 'Punch', '2': 'King\'s Mercy', "3": "Vibranium Burst",
                                      "4": "Ultimate Ability: Legacy of Odinson"}
        self.assertEqual(mock_response.getvalue(), expected_print_statement)
        self.assertEqual(all_skills, expected_skills_dictionary)

    @patch('builtins.input', side_effect=[9])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_skill_runaway_from_enemy(self, mock_response, _):
        all_skills = {'1': 'Punch', '2': 'King\'s Mercy', "3": "Vibranium Burst",
                      "4": "Ultimate Ability: Legacy of Odinson", '9': 'RUN AWAY!'}
        test_enemy = {"Name": "Frost Giant", 'class': 'enemy', "Level": 8, "HP": 700, "ATK": 700,
                      "EXP given": 50}
        game.choose_skill(all_skills, test_enemy)
        expected_print_statement = """What skill do you use?
[1]: Punch
[2]: King's Mercy
[3]: Vibranium Burst
[4]: Ultimate Ability: Legacy of Odinson
[9]: RUN AWAY!
You try and run away!
"""
        self.assertEqual(mock_response.getvalue(), expected_print_statement)

    @patch('builtins.input', side_effect=["g", 2])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_skill_invalid_input(self, mock_response, _):
        all_skills = {'1': 'Punch', '2': 'King\'s Mercy', "3": "Vibranium Burst",
                      "4": "Ultimate Ability: Legacy of Odinson", '9': 'RUN AWAY!'}
        test_enemy = {"Name": "Galactus Ultron", 'class': 'boss', "Level": 8, "HP": 700, "ATK": 700, "EXP given": 50}
        game.choose_skill(all_skills, test_enemy)
        expected_print_statement = """What skill do you use?
[1]: Punch
[2]: King's Mercy
[3]: Vibranium Burst
[4]: Ultimate Ability: Legacy of Odinson
[9]: RUN AWAY!
That is an invalid number!
Please pick again

What skill do you use?
[1]: Punch
[2]: King's Mercy
[3]: Vibranium Burst
[4]: Ultimate Ability: Legacy of Odinson
[9]: RUN AWAY!
You choose to King\'s Mercy....
"""

        self.assertEqual(mock_response.getvalue(), expected_print_statement)

    @patch('builtins.input', side_effect=[3])
    def test_choose_skill_enemy_unmodified(self, _):

        all_skills = {'1': 'Punch', '2': 'King\'s Mercy', "3": "Vibranium Burst",
                      "4": "Ultimate Ability: Panther Goddess Bast", '9': 'RUN AWAY!'}
        test_enemy = {"Name": "Galactus Ultron", 'class': 'boss', "Level": 8, "HP": 700, "ATK": 700, "EXP given": 50}
        game.choose_skill(all_skills, test_enemy)
        enemy_unmodified = {"Name": "Galactus Ultron", 'class': 'boss', "Level": 8, "HP": 700, "ATK": 700, "EXP given": 50}
        self.assertEqual(test_enemy, enemy_unmodified)

    @patch('builtins.input', side_effect=[4])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_skill_valid_input(self, mock_response, _):
        all_skills = {'1': 'Punch', '2': 'King\'s Mercy', "3": "Vibranium Burst",
                      "4": "Ultimate Ability: Legacy of Odinson", '9': 'RUN AWAY!'}
        test_enemy = {"Name": "Galactus Ultron", 'class': 'boss', "Level": 8, "HP": 700, "ATK": 700, "EXP given": 50}
        game.choose_skill(all_skills, test_enemy)
        expected_print_statement = """What skill do you use?
[1]: Punch
[2]: King's Mercy
[3]: Vibranium Burst
[4]: Ultimate Ability: Legacy of Odinson
[9]: RUN AWAY!
You choose to Ultimate Ability: Legacy of Odinson....
"""
        self.assertEqual(mock_response.getvalue(), expected_print_statement)