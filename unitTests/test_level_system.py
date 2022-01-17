from unittest import TestCase
import game


class TestLevelSystem(TestCase):
    def test_level_system_gain_exp(self):
        test_enemy = {"Name": "Hydra Agent", "Level": 2, "HP": 120, "ATK": 120, "EXP given": 15}
        test_character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Level': 1, 'EXP': 0, 'EXP needed': 30, 'title': '',
                          'domain': ''}
        game.level_system(test_character, test_enemy)
        expected = {'X-coordinate': 1, 'Y-coordinate': 1, 'Level': 1, 'EXP': 15, 'EXP needed': 30, 'title': '',
                    'domain': ''}
        actual = test_character
        self.assertEqual(expected, actual)

    def test_level_system_increased_level_with_one_HP(self):
        test_enemy = {"Name": "Frost Giant", "Level": 2, "HP": 120, "ATK": 120, "EXP given": 30}
        test_sorcerer_character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Level': 1, 'EXP': 0, 'EXP needed': 30,
                                   'title': 'Sorcerer in training', 'domain': 'Temple of Vishanti', 'Current HP': 1,
                                   'Current Mana': 140, 'ATK': 200, 'DEF': 80, 'HP cap': 120, 'Mana cap': 140}
        game.level_system(test_sorcerer_character, test_enemy)
        expected = {'X-coordinate': 1, 'Y-coordinate': 1, 'Level': 2, 'EXP': 0, 'EXP needed': 60,
                    'title': 'Sorcerer in training', 'domain': 'Temple of Vishanti', 'Current HP': 220,
                    'Current Mana': 240, 'ATK': 300, 'DEF': 180, 'HP cap': 220, 'Mana cap': 240}
        actual = test_sorcerer_character
        self.assertEqual(expected, actual)

    def test_level_system_increased_level_overflow(self):
        test_enemy = {"Name": "Dark Elf", "Level": 2, "HP": 120, "ATK": 120, "EXP given": 90}
        thunder_frog_character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Level': 2, 'EXP': 0, 'EXP needed': 60,
                                  'title': 'Frog of Thunder', 'domain': 'Asgardian Republic', 'Current HP': 220,
                                  'Current Mana': 100, 'ATK': 140, 'DEF': 80, 'HP cap': 220, 'Mana cap': 100}
        game.level_system(thunder_frog_character, test_enemy)
        expected = {'X-coordinate': 1, 'Y-coordinate': 1, 'Level': 3, 'EXP': 30, 'EXP needed': 120,
                    'title': 'Frog of Thunder', 'domain': 'Asgardian Republic', 'Current HP': 370,
                    'Current Mana': 250, 'ATK': 290, 'DEF': 230, 'HP cap': 370, 'Mana cap': 250}
        actual = thunder_frog_character
        self.assertEqual(expected, actual)
