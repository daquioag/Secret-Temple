from unittest import TestCase

import game


class TestGainedLevel(TestCase):
    def test_gained_level_one_to_two(self):
        test_sorcerer_character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Level': 1, 'EXP': 30, 'EXP needed': 30,
                                   'title': 'Sorcerer in Training', 'domain': 'Temple of Vishanti', 'Current HP': 1,
                                   'Current Mana': 140, 'ATK': 200, 'DEF': 80, 'HP cap': 120, 'Mana cap': 140}
        game.gained_level(test_sorcerer_character)
        expected = {'X-coordinate': 1, 'Y-coordinate': 1, 'Level': 2, 'EXP': 0, 'EXP needed': 60,
                    'title': 'Sorcerer in Training', 'domain': 'Temple of Vishanti', 'Current HP': 220,
                    'Current Mana': 240, 'ATK': 300, 'DEF': 180, 'HP cap': 220, 'Mana cap': 240}
        actual = test_sorcerer_character
        self.assertEqual(expected, actual)

    # def test_gained_level_2_to_3(self):
    #     test_sorcerer_character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Level': 2, 'EXP': 60, 'EXP needed': 60,
    #                                'title': 'Sorcerer in training', 'domain': 'Temple of Vishanti', 'Current HP': 220,
    #                                'Current Mana': 240, 'ATK': 300, 'DEF': 180, 'HP cap': 220, 'Mana cap': 240}
    #     game.gained_level(test_sorcerer_character)
    #     expected = {'X-coordinate': 1, 'Y-coordinate': 1, 'Level': 3, 'EXP': 0, 'EXP needed': 120,
    #                 'title': 'Sorcerer in training', 'domain': 'Temple of Vishanti', 'Current HP': 370,
    #                 'Current Mana': 390, 'ATK': 450, 'DEF': 330, 'HP cap': 370, 'Mana cap': 390}
    #     actual = test_sorcerer_character
    #     self.assertEqual(expected, actual)
    #
    # def test_gained_level_3_to_4(self):
    #     test_sorcerer_character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Level': 3, 'EXP': 120, 'EXP needed': 120,
    #                                'title': 'Sorcerer in training', 'domain': 'Temple of Vishanti', 'Current HP': 370,
    #                                'Current Mana': 390, 'ATK': 450, 'DEF': 330, 'HP cap': 370, 'Mana cap': 390}
    #     game.gained_level(test_sorcerer_character)
    #     expected = {'X-coordinate': 1, 'Y-coordinate': 1, 'Level': 4, 'EXP': 0, 'EXP needed': 240,
    #                 'title': 'Sorcerer in training', 'domain': 'Temple of Vishanti', 'Current HP': 570,
    #                 'Current Mana': 590, 'ATK': 650, 'DEF': 530, 'HP cap': 570, 'Mana cap': 590}
    #     actual = test_sorcerer_character
    #     self.assertEqual(expected, actual)

    def test_gained_level_four_to_five(self):
        test_sorcerer_character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Level': 4, 'EXP': 240, 'EXP needed': 240,
                                   'title': 'Sorcerer in training', 'domain': 'Temple of Vishanti', 'Current HP': 570,
                                   'Current Mana': 590, 'ATK': 650, 'DEF': 530, 'HP cap': 570, 'Mana cap': 590}
        game.gained_level(test_sorcerer_character)
        expected = {'X-coordinate': 1, 'Y-coordinate': 1, 'Level': 5, 'EXP': 0, 'EXP needed': 480,
                    'title': 'Sorcerer in training', 'domain': 'Temple of Vishanti', 'Current HP': 820,
                    'Current Mana': 840, 'ATK': 900, 'DEF': 780, 'HP cap': 820, 'Mana cap': 840}
        actual = test_sorcerer_character
        self.assertEqual(expected, actual)
