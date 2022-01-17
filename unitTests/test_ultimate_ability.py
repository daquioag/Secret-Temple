from unittest import TestCase
import game
from unittest.mock import patch
import unittest.mock
import io


class TestUltimateAbility(TestCase):
    @patch('random.randint', return_value=1)
    def test_ultimate_ability_damage_dealt(self, _):
        test_character = {'Current HP': 220, 'Current Mana': 100, 'ATK': 140, 'DEF': 80, 'title': 'Frog of Thunder',
                          'domain': 'Asgardian Republic', 'HP cap': 220, 'Mana cap': 100, "Level": 3}
        all_skills = {'1': 'Punch', '2': 'King\'s Mercy', "3": "Vibranium Burst",
                      "4": "Ultimate Ability: Legacy of Odinson", '9': 'RUN AWAY!'}
        mock_skill = "4"
        test_enemy = {"Name": "Galactus Ultron", 'class': 'boss', "Level": 8, "HP": 700, "ATK": 700, "EXP given": 50}
        game.hero_battle_phase(test_character, test_enemy, mock_skill, all_skills)
        expected_enemy_hp = 560
        actual_enemy_hp = test_enemy["HP"]
        self.assertEqual(expected_enemy_hp, actual_enemy_hp)

    @patch('random.randint', return_value=3)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_ultimate_ability_print_statement(self, mock_response, _):
        test_character = {'Current HP': 220, 'Current Mana': 100, 'ATK': 140, 'DEF': 80, 'title': 'Frog of Thunder',
                          'domain': 'Asgardian Republic', 'HP cap': 220, 'Mana cap': 100, "Level": 3}
        all_skills = {'1': 'Punch', '2': "Throw Mjolnir", "3": 'Crashing Thunder',
                      "4": "Ultimate Ability: Legacy of Odinson", '9': 'RUN AWAY!'}
        mock_skill = "4"
        test_enemy = {"Name": "Galactus Ultron", 'class': 'boss', "Level": 8, "HP": 700, "ATK": 700, "EXP given": 50}
        game.hero_battle_phase(test_character, test_enemy, mock_skill, all_skills)
        expected = "You used Ultimate Ability: Legacy of Odinson!" \
                   "\nUltimate Ability: Legacy of Odinson was super effective! 47 damage was dealt to Galactus Ultron " \
                   "\nYou lost 45 Mana\n"
        self.assertEqual(mock_response.getvalue(), expected)

    def test_ultimate_ability_mana_cost(self):
        test_character = {'Current HP': 220, 'Current Mana': 100, 'ATK': 140, 'DEF': 80, 'title': 'Frog of Thunder',
                          'domain': 'Asgardian Republic', 'HP cap': 220, 'Mana cap': 100, "Level": 3}
        all_skills = {'1': 'Punch', '2': "Throw Mjolnir", "3": 'Crashing Thunder',
                      "4": "Ultimate Ability: Legacy of Odinson", '9': 'RUN AWAY!'}
        mock_skill = "4"
        test_enemy = {"Name": "Galactus Ultron", 'class': 'boss', "Level": 8, "HP": 700, "ATK": 700, "EXP given": 50}
        game.hero_battle_phase(test_character, test_enemy, mock_skill, all_skills)
        expected_mana = 55
        self.assertEqual(expected_mana, test_character["Current Mana"])
