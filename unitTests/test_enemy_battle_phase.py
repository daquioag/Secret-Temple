from unittest import TestCase
import game
from unittest.mock import patch
import unittest.mock
import io


#  (enemy['ATK'] * (4 * random.randint(2, enemy['Level'] + 3)) / character "DEF"]) --> damage calculator
class TestEnemyBattlePhase(TestCase):
    @patch('random.randint', return_value=2)
    def test_enemy_battle_phase_enemy_level_one_damage(self, _):
        test_character = {'Current HP': 160, 'DEF': 140}
        test_enemy = {"Name": "Galactus Ultron", "Level": 2, "HP": 0, "ATK": 100}
        game.enemy_battle_phase(test_character, test_enemy)
        expected_damage_taken = 6
        actual_damage_taken = round((100 * (4 * 2) / 140))
        actual_hp_after_taking_damage = test_character["Current HP"]
        self.assertEqual(expected_damage_taken, actual_damage_taken)
        self.assertEqual(154, actual_hp_after_taking_damage)

    @patch('random.randint', return_value=11)
    def test_enemy_battle_phase_enemy_level_eight_damage(self, _):
        test_character = {'Current HP': 160, 'DEF': 140}
        test_enemy = {"Name": "Galactus Ultron", "Level": 8, "HP": 0, "ATK": 100}
        game.enemy_battle_phase(test_character, test_enemy)
        expected_damage_taken = 31
        actual_damage_taken = round((100 * (4 * 11) / 140))
        actual_hp_after_taking_damage = test_character["Current HP"]
        self.assertEqual(expected_damage_taken, actual_damage_taken)
        self.assertEqual(129, actual_hp_after_taking_damage)

    @patch('random.randint', return_value=11)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_enemy_battle_phase_print_statement(self, mock_response, _):
        test_character = {'Current HP': 160, 'DEF': 140}
        test_enemy = {"Name": "Galactus Ultron", "Level": 8, "HP": 0, "ATK": 100}
        game.enemy_battle_phase(test_character, test_enemy)
        expected = "Galactus Ultron  attacked you for 31 damage!\n"
        self.assertEqual(mock_response.getvalue(), expected)

    @patch('random.randint', return_value=1)
    def test_enemy_battle_phase_boss_unmodified(self, _):
        test_character = {'Current HP': 160, 'DEF': 140}
        test_enemy = {"Name": "Galactus Ultron", "Level": 8, "HP": 0, "ATK": 100}
        game.enemy_battle_phase(test_character, test_enemy)
        boss_unmodified = {"Name": "Galactus Ultron", "Level": 8, "HP": 0, "ATK": 100}
        self.assertEqual(test_enemy, boss_unmodified)