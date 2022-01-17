from unittest import TestCase
import game
from unittest.mock import patch
import unittest.mock
import io


class TestBasicAttack(TestCase):
    @patch('random.randint', return_value=1)
    def test_basic_attack_damage_dealt(self, _):
        test_character = {'name': 'TChalla', 'EXP': 0, 'EXP needed': 60, 'Current HP': 160,
                          'Current Mana': 80, 'ATK': 160, 'DEF': 140, 'title': 'Panther',
                          'domain': 'Kingdom of Wakanda', 'HP cap': 160, 'Mana cap': 80, "Level": 2}
        all_skills = {'1': 'Punch', '2': 'King\'s Mercy', "3": "Vibranium Burst",
                      "4": "Ultimate Ability: Panther Goddess Bast", '9': 'RUN AWAY!'}
        mock_skill = "2"
        test_enemy = {"Name": "Galactus Ultron", 'class': 'boss', "Level": 8, "HP": 700, "ATK": 700, "EXP given": 50}
        game.hero_battle_phase(test_character, test_enemy, mock_skill, all_skills)
        expected_enemy_hp = 647
        actual_enemy_hp = test_enemy["HP"]
        self.assertEqual(expected_enemy_hp, actual_enemy_hp)

    def test_basic_attack_character_unmodified(self):  # when using a baisc attack, the character shouldnt be modified
        test_character = {'name': 'TChalla', 'EXP': 0, 'EXP needed': 60, 'Current HP': 160,
                          'Current Mana': 80, 'ATK': 160, 'DEF': 140, 'title': 'Panther',
                          'domain': 'Kingdom of Wakanda', 'HP cap': 160, 'Mana cap': 80, "Level": 2}
        all_skills = {'1': 'Punch', '2': 'King\'s Mercy', "3": "Vibranium Burst",
                      "4": "Ultimate Ability: Panther Goddess Bast", '9': 'RUN AWAY!'}
        mock_skill = "2"
        test_enemy = {"Name": "Galactus Ultron", 'class': 'boss', "Level": 8, "HP": 700, "ATK": 700, "EXP given": 50}
        game.hero_battle_phase(test_character, test_enemy, mock_skill, all_skills)
        character_unmodified = {'name': 'TChalla', 'EXP': 0, 'EXP needed': 60, 'Current HP': 160,
                                'Current Mana': 80, 'ATK': 160, 'DEF': 140, 'title': 'Panther',
                                'domain': 'Kingdom of Wakanda', 'HP cap': 160, 'Mana cap': 80, "Level": 2}
        actual = test_character
        self.assertEqual(actual, character_unmodified)

    @patch('random.randint', return_value=3)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_basic_attack_not_very_effective(self, mock_response, _):
        test_character = {'name': 'TChalla', 'EXP': 0, 'EXP needed': 60, 'Current HP': 160,
                          'Current Mana': 80, 'ATK': 160, 'DEF': 140, 'title': 'Panther',
                          'domain': 'Kingdom of Wakanda', 'HP cap': 160, 'Mana cap': 80, "Level": 2}
        all_skills = {'1': 'Punch', '2': 'King\'s Mercy', "3": "Vibranium Burst",
                      "4": "Ultimate Ability: Panther Goddess Bast", '9': 'RUN AWAY!'}
        mock_skill = "2"
        test_enemy = {"Name": "Galactus Ultron", 'class': 'boss', "Level": 8, "HP": 700, "ATK": 700, "EXP given": 50}
        game.hero_battle_phase(test_character, test_enemy, mock_skill, all_skills)
        expected = "Howard: Its not very effective...." \
                   "\n\nKing's Mercy dealt 18 damage to Galactus Ultron" \
                   "\nYou lost 0 Mana\n"
        self.assertEqual(mock_response.getvalue(), expected)
