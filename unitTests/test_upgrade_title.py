from unittest import TestCase

import game_beta


class TestUpgradeTitle(TestCase):
    def test_upgrade_title_level_5_title(self):
        thunder_frog_character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Level': 1, 'EXP': 0, 'EXP needed': 30,
                                  'title': 'Frog of Thunder', 'domain': 'Asgardian Republic', 'Current HP': 220,
                                  'Current Mana': 100, 'ATK': 140, 'DEF': 80, 'HP cap': 220, 'Mana cap': 100}
        thunder_frog_titles = ["Frog of Thunder", "Thor Odinson", "God of Thunder", "Unworthy Thor",
                               "God King Thor"]
        thunder_frog_character.update({"Level": 5})
        game_beta.upgrade_title(thunder_frog_character, thunder_frog_titles)
        actual = thunder_frog_character['title']
        expected = "God King Thor"
        self.assertEqual(actual, expected)

    def test_upgrade_title_level_10_title(self):
        panther_character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Level': 1, 'EXP': 0, 'EXP needed': 30,
                             'title': 'Panther', 'domain': 'Kingdom of Wakanda', 'Current HP': 160,
                             'Current Mana': 80, 'ATK': 160, 'DEF': 140, 'HP cap': 160, 'Mana cap': 80}

        panther_titles = ["Panther", "Coal Tiger", "Ghost Panther", "The Black Panther", "King of Necropolis"]
        panther_character.update({"Level": 5})
        game_beta.upgrade_title(panther_character, panther_titles)
        actual = panther_character['title']
        expected = "King of Necropolis"
        self.assertEqual(actual, expected)

    def test_upgrade_title_level_1_title(self):
        iron_heart_character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Level': 1, 'EXP': 0, 'EXP needed': 30,
                                'title': 'Iron Heart Mark I', 'domain': 'House of Iron', 'Current HP': 200,
                                'Current Mana': 100, 'ATK': 120, 'DEF': 120, 'HP cap': 200, 'Mana cap': 100}

        iron_heart_titles = ["Iron Heart Mark I", "Iron Heart Mark III", "Iron Heart MK 40",
                             "Iron Heart Mark XXII: Thorbuster",
                             "Iron Heart Mark XLIV: Thanos-Buster"]
        iron_heart_character.update({"Level": 1})
        game_beta.upgrade_title(iron_heart_character, iron_heart_titles)
        actual = iron_heart_character['title']
        expected = "Iron Heart Mark I"
        self.assertEqual(actual, expected)

    def test_upgrade_title_level_3_title(self):
        sorcerer_character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Level': 1, 'EXP': 0, 'EXP needed': 30,
                              'title': 'Sorcerer in Training', 'domain': 'Temple of Vishanti', 'Current HP': 120,
                              'Current Mana': 140, 'ATK': 200, 'DEF': 80, 'HP cap': 120, 'Mana cap': 140}

        sorcerer_titles = ["Sorcerer in Training", "Master of the Mystic Arts", "Sorcerer Supreme",
                           "Disciple of Dormamu", "Dr. StrangeFate "]
        sorcerer_character.update({"Level": 3})
        game_beta.upgrade_title(sorcerer_character, sorcerer_titles)
        actual = sorcerer_character['title']
        expected = "Sorcerer Supreme"
        self.assertEqual(actual, expected)

    def test_upgrade_title_title_list_unmodified(self):
        panther_character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Level': 1, 'EXP': 0, 'EXP needed': 30,
                             'title': 'Panther', 'domain': 'Kingdom of Wakanda', 'Current HP': 160,
                             'Current Mana': 80, 'ATK': 160, 'DEF': 140, 'HP cap': 160, 'Mana cap': 80}

        panther_titles = ["Panther", "Coal Tiger", "Ghost Panther", "The Black Panther", "King of Necropolis"]
        panther_character.update({"Level": 5})
        game_beta.upgrade_title(panther_character, panther_titles)
        actual = panther_character['title']
        expected = ["Panther", "Coal Tiger", "Ghost Panther", "The Black Panther", "King of Necropolis"]
        self.assertEqual(panther_titles, expected)
