from unittest import TestCase
import game
from unittest.mock import patch
import unittest.mock
import io


class TestSafeZone(TestCase):
    @patch('random.randint', return_value=1)
    def test_safe_zone_current_hp_and_mana_no_overflow(self, _):
        test_character = {'name': 'TChalla', 'Current HP': 159, 'title' : 'Panther', 'Level': 1,
                          'Current Mana': 79, 'domain': 'Kingdom of Wakanda', 'HP cap': 160, 'Mana cap': 80}
        game.safe_zone(test_character)
        expected_hp = 160
        expected_mana = 80
        self.assertEqual(expected_hp, test_character["Current HP"])
        self.assertEqual(expected_mana, test_character["Current Mana"])

    @patch('random.randint', return_value=10)
    def test_safe_zone_no_duck_juice(self, _):
        test_character = {'name': 'TChalla', 'Current HP': 1, 'title': 'Panther', 'Level': 1,
                          'Current Mana': 1, 'domain': 'Kingdom of Wakanda', 'HP cap': 160, 'Mana cap': 80}
        game.safe_zone(test_character)
        expected_hp = 1
        expected_mana = 1
        self.assertEqual(expected_hp, test_character["Current HP"])
        self.assertEqual(expected_mana, test_character["Current Mana"])