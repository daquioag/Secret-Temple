from unittest import TestCase
import game
from unittest.mock import patch
import unittest.mock
import io


class TestStrongAttack(TestCase):
    @patch('random.randint', return_value=1)
    def test_strong_attack_damage_dealt(self, _):
        test_character = {'name': 'TChalla', 'EXP': 0, 'EXP needed': 60, 'Current HP': 160,
                          'Current Mana': 80, 'ATK': 160, 'DEF': 140, 'title': 'Panther',
                          'domain': 'Kingdom of Wakanda', 'HP cap': 160, 'Mana cap': 80, "Level": 2}
        all_skills = {'1': 'Punch', '2': 'King\'s Mercy', "3": "Vibranium Burst",
                      "4": "Ultimate Ability: Panther Goddess Bast", '9': 'RUN AWAY!'}
        mock_skill = "3"
        test_enemy = {"Name": "Galactus Ultron", 'class': 'boss', "Level": 8, "HP": 700, "ATK": 700, "EXP given": 50}
        game.hero_battle_phase(test_character, test_enemy, mock_skill, all_skills)
        expected_enemy_hp = 620
        actual_enemy_hp = test_enemy["HP"]
        self.assertEqual(expected_enemy_hp, actual_enemy_hp)

    @patch('random.randint', return_value=3)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_strong_attack_barely_hit(self, mock_response, _):
        test_character = {'name': 'TChalla', 'EXP': 0, 'EXP needed': 60, 'Current HP': 160,
                          'Current Mana': 80, 'ATK': 160, 'DEF': 140, 'title': 'Panther',
                          'domain': 'Kingdom of Wakanda', 'HP cap': 160, 'Mana cap': 80, "Level": 2}
        all_skills = {'1': 'Punch', '2': 'King\'s Mercy', "3": "Vibranium Burst",
                      "4": "Ultimate Ability: Panther Goddess Bast", '9': 'RUN AWAY!'}
        mock_skill = "3"
        test_enemy = {"Name": "Galactus Ultron", 'class': 'boss', "Level": 8, "HP": 700, "ATK": 700, "EXP given": 50}
        game.hero_battle_phase(test_character, test_enemy, mock_skill, all_skills)
        expected = "Howard: Do you know how to aim?! Barely hit em...." \
                   "\n\nVibranium Burst dealt 27 damage to Galactus Ultron" \
                   "\nYou lost 20 Mana\n"
        self.assertEqual(mock_response.getvalue(), expected)

    @patch('random.randint', return_value=1)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_strong_attack_direct_hit(self, mock_response, _):
        test_character = {'name': 'TChalla', 'EXP': 0, 'EXP needed': 60, 'Current HP': 160,
                          'Current Mana': 80, 'ATK': 160, 'DEF': 140, 'title': 'Panther',
                          'domain': 'Kingdom of Wakanda', 'HP cap': 160, 'Mana cap': 80, "Level": 2}
        all_skills = {'1': 'Punch', '2': 'King\'s Mercy', "3": "Vibranium Burst",
                      "4": "Ultimate Ability: Panther Goddess Bast", '9': 'RUN AWAY!'}
        mock_skill = "3"
        test_enemy = {"Name": "Galactus Ultron", 'class': 'boss', "Level": 8, "HP": 700, "ATK": 700, "EXP given": 50}
        game.hero_battle_phase(test_character, test_enemy, mock_skill, all_skills)
        expected = "Howard: Direct HIT!! Its super effective!" \
                   "\n\nVibranium Burst dealt 80 damage to Galactus Ultron" \
                   "\nYou lost 20 Mana\n"
        self.assertEqual(mock_response.getvalue(), expected)

    def test_strong_attack_mana_change(self):
        test_character = {'name': 'TChalla', 'EXP': 0, 'EXP needed': 60, 'Current HP': 160,
                          'Current Mana': 80, 'ATK': 160, 'DEF': 140, 'title': 'Panther',
                          'domain': 'Kingdom of Wakanda', 'HP cap': 160, 'Mana cap': 80, "Level": 2}
        all_skills = {'1': 'Punch', '2': 'King\'s Mercy', "3": "Vibranium Burst",
                      "4": "Ultimate Ability: Panther Goddess Bast", '9': 'RUN AWAY!'}
        mock_skill = "3"
        test_enemy = {"Name": "Galactus Ultron", 'class': 'boss', "Level": 8, "HP": 700, "ATK": 700, "EXP given": 50}
        game.hero_battle_phase(test_character, test_enemy, mock_skill, all_skills)
        expected_mana = 60
        self.assertEqual(expected_mana, test_character["Current Mana"])
