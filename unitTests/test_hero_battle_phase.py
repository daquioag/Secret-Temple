from unittest import TestCase
import game
from unittest.mock import patch
import unittest.mock
import io


class TestHeroBattlePhase(TestCase):
    def test_hero_battle_phase_skills_unmodified(self):
        test_character = {'name': 'TChalla', 'EXP': 0, 'EXP needed': 60, 'Current HP': 160,
                          'Current Mana': 80, 'ATK': 160, 'DEF': 140, 'title': 'Panther',
                          'domain': 'Kingdom of Wakanda', 'HP cap': 160, 'Mana cap': 80, "Level": 2}
        all_skills = {'1': 'Punch', '2': 'King\'s Mercy', "3": "Vibranium Burst",
                      "4": "Ultimate Ability: Panther Goddess Bast", '9': 'RUN AWAY!'}
        mock_skill = "4"
        test_enemy = {"Name": "Galactus Ultron", 'class': 'boss', "Level": 8, "HP": 700, "ATK": 700, "EXP given": 50}
        game.hero_battle_phase(test_character, test_enemy, mock_skill, all_skills)
        skills_unmodified = {'1': 'Punch', '2': 'King\'s Mercy', "3": "Vibranium Burst",
                             "4": "Ultimate Ability: Panther Goddess Bast", '9': 'RUN AWAY!'}
        self.assertEqual(all_skills, skills_unmodified)

    @patch('random.randint', return_value=1)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_hero_battle_phase_enemy_dead(self, mock_response, _):
        test_character = {'name': 'TChalla', 'EXP': 0, 'EXP needed': 60, 'Current HP': 160,
                          'Current Mana': 80, 'ATK': 160, 'DEF': 140, 'title': 'Panther',
                          'domain': 'Kingdom of Wakanda', 'HP cap': 160, 'Mana cap': 80, "Level": 2}
        all_skills = {'1': 'Punch', '2': 'King\'s Mercy', "3": "Vibranium Burst",
                      "4": "Ultimate Ability: Panther Goddess Bast", '9': 'RUN AWAY!'}
        mock_skill = "4"
        test_enemy = {"Name": "Galactus Ultron", 'class': 'boss', "Level": 8, "HP": 1, "ATK": 700, "EXP given": 50}
        game.hero_battle_phase(test_character, test_enemy, mock_skill, all_skills)
        expected = "You used Ultimate Ability: Panther Goddess Bast!" \
                   "\nUltimate Ability: Panther Goddess Bast was super effective! 160 damage was dealt to Galactus Ultron " \
                   "\nYou lost 30 Mana" \
                   "\nYou killed Galactus Ultron\n"
        self.assertEqual(mock_response.getvalue(), expected)

    @patch('random.randint', return_value=1)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_hero_battle_phase_weak_attack(self, mock_response, _):
        test_character = {'name': 'TChalla', 'EXP': 0, 'EXP needed': 60, 'Current HP': 160,
                          'Current Mana': 80, 'ATK': 160, 'DEF': 140, 'title': 'Panther',
                          'domain': 'Kingdom of Wakanda', 'HP cap': 160, 'Mana cap': 80, "Level": 2}
        all_skills = {'1': 'Punch', '2': 'King\'s Mercy', "3": "Vibranium Burst",
                      "4": "Ultimate Ability: Panther Goddess Bast", '9': 'RUN AWAY!'}
        mock_skill = "1"
        test_enemy = {"Name": "Galactus Ultron", 'class': 'boss', "Level": 8, "HP": 500, "ATK": 700, "EXP given": 50}
        game.hero_battle_phase(test_character, test_enemy, mock_skill, all_skills)
        expected = "Howard: Its super effective!" \
                   "\n\nPunch dealt 53 damage to Galactus Ultron" \
                   "\nYou lost 0 Mana\n"
        self.assertEqual(mock_response.getvalue(), expected)

    @patch('random.randint', return_value=1)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_hero_battle_phase_strong_attack(self, mock_response, _):
        test_character = {'name': 'TChalla', 'EXP': 0, 'EXP needed': 60, 'Current HP': 160,
                          'Current Mana': 80, 'ATK': 160, 'DEF': 140, 'title': 'Panther',
                          'domain': 'Kingdom of Wakanda', 'HP cap': 160, 'Mana cap': 80, "Level": 2}
        all_skills = {'1': 'Punch', '2': 'King\'s Mercy', "3": "Vibranium Burst",
                      "4": "Ultimate Ability: Panther Goddess Bast", '9': 'RUN AWAY!'}
        mock_skill = "3"
        test_enemy = {"Name": "Galactus Ultron", 'class': 'boss', "Level": 8, "HP": 500, "ATK": 700,
                      "EXP given": 50}
        game.hero_battle_phase(test_character, test_enemy, mock_skill, all_skills)
        expected = "Howard: Direct HIT!! Its super effective!" \
                   "\n\nVibranium Burst dealt 80 damage to Galactus Ultron" \
                   "\nYou lost 20 Mana\n"
        self.assertEqual(mock_response.getvalue(), expected)
