from unittest import TestCase

import game


class TestAddClassStats(TestCase):
    def test_add_class_stats_Iron_Heart_Mark_I(self):
        test_character = game.make_character()
        iron_heart_class_title = "Iron Heart Mark I"
        game.add_class_stats(test_character, iron_heart_class_title)
        expected = {'X-coordinate': 1, 'Y-coordinate': 1, 'Level': 1, 'EXP': 0, 'EXP needed': 30,
                    'title': 'Iron Heart Mark I', 'domain': 'House of Iron', 'Current HP': 200, 'Current Mana': 100,
                    'ATK': 120, 'DEF': 120, 'HP cap': 200, 'Mana cap': 100}
        actual = test_character
        self.assertEqual(expected, actual)

    def test_add_class_stats_Frog_of_Thunder(self):
        test_character = game.make_character()
        iron_heart_class_title = "Frog of Thunder"
        game.add_class_stats(test_character, iron_heart_class_title)
        expected = {'X-coordinate': 1, 'Y-coordinate': 1, 'Level': 1, 'EXP': 0, 'EXP needed': 30,
                    'title': 'Frog of Thunder', 'domain': 'Asgardian Republic', 'Current HP': 220, 'Current Mana': 100,
                    'ATK': 140, 'DEF': 80, 'HP cap': 220, 'Mana cap': 100}
        actual = test_character
        self.assertEqual(expected, actual)

    def test_add_class_stats_Panther(self):
        test_character = game.make_character()
        iron_heart_class_title = "Panther"
        game.add_class_stats(test_character, iron_heart_class_title)
        expected = {'X-coordinate': 1, 'Y-coordinate': 1, 'Level': 1, 'EXP': 0, 'EXP needed': 30,
                    'title': 'Panther', 'domain': 'Kingdom of Wakanda', 'Current HP': 160, 'Current Mana': 80,
                    'ATK': 160, 'DEF': 140, 'HP cap': 160, 'Mana cap': 80}
        actual = test_character
        self.assertEqual(expected, actual)

    def test_add_class_stats_Sorcerer_in_Training(self):
        test_character = game.make_character()
        iron_heart_class_title = "Sorcerer in Training"
        game.add_class_stats(test_character, iron_heart_class_title)
        expected = {'X-coordinate': 1, 'Y-coordinate': 1, 'Level': 1, 'EXP': 0, 'EXP needed': 30,
                    'title': 'Sorcerer in Training', 'domain': 'Temple of Vishanti', 'Current HP': 140,
                    'Current Mana': 120, 'ATK': 200, 'DEF': 80, 'HP cap': 140, 'Mana cap': 120}
        actual = test_character
        self.assertEqual(expected, actual)
