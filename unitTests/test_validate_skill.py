from unittest import TestCase
import game
from unittest.mock import patch
import unittest.mock
import io


class TestValidateSkill(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_validate_skill_special_ability_with_little_mana(
            self, mock_response):  # you need 45 mana at level 3 to cast the special ability
        test_skill = "4"
        test_character = {'Current HP': 160, 'Current Mana': 44, 'ATK': 160, 'DEF': 140, 'title': 'Panther',
                          'domain': 'Kingdom of Wakanda', 'HP cap': 160, 'Mana cap': 80, "Level": 3}
        actual = game.validate_skill(test_character, test_skill)
        expected_print_statement = "Nuh-uh-uh! You ain't go no more mana!" \
                                   "\nTry another ability!\n"
        self.assertFalse(actual)
        self.assertEqual(mock_response.getvalue(), expected_print_statement)

    def test_validate_skill_special_ability_with_mana(self):
        test_skill = "4"
        test_character = {'Current HP': 160, 'Current Mana': 45, 'ATK': 160, 'DEF': 140, 'title': 'Panther',
                          'domain': 'Kingdom of Wakanda', 'HP cap': 160, 'Mana cap': 80, "Level": 3}
        actual = game.validate_skill(test_character, test_skill)
        self.assertTrue(actual)

    def test_validate_skill_character_unmodified(self):
        test_character = {'name': 'TChalla', 'EXP': 0, 'EXP needed': 60, 'Current HP': 160,
                          'Current Mana': 80, 'ATK': 160, 'DEF': 140, 'title': 'Panther',
                          'domain': 'Kingdom of Wakanda', 'HP cap': 160, 'Mana cap': 80, "Level": 2}
        test_skill = "4"
        game.validate_skill(test_character, test_skill)
        character_unmodified = {'name': 'TChalla', 'EXP': 0, 'EXP needed': 60, 'Current HP': 160,
                                'Current Mana': 80, 'ATK': 160, 'DEF': 140, 'title': 'Panther',
                                'domain': 'Kingdom of Wakanda', 'HP cap': 160, 'Mana cap': 80, "Level": 2}
        self.assertEqual(test_character, character_unmodified)

    def test_validate_skill_strong_attack_with_no_mana(self):
        test_skill = "3"  # you need 30 mana at level 3 to cast the special ability
        test_character = {'Current HP': 160, 'Current Mana': 0, 'ATK': 160, 'DEF': 140, 'title': 'Panther',
                          'domain': 'Kingdom of Wakanda', 'HP cap': 160, 'Mana cap': 80, "Level": 3}
        actual = game.validate_skill(test_character, test_skill)
        self.assertFalse(actual)

    def test_validate_skill_strong_attack_with_just_enough_mana(self):
        test_skill = "3"  # you need 30 mana at level 3 to cast the special ability
        test_character = {'Current HP': 160, 'Current Mana': 30, 'ATK': 160, 'DEF': 140, 'title': 'Panther',
                          'domain': 'Kingdom of Wakanda', 'HP cap': 160, 'Mana cap': 80, "Level": 3}
        actual = game.validate_skill(test_character, test_skill)
        self.assertTrue(actual)

    def test_validate_skill_basic_attack_with_no_mana(self):
        test_skill = "1"  # you need 30 mana at level 3 to cast the special ability
        test_character = {'Current HP': 160, 'Current Mana': 0, 'ATK': 160, 'DEF': 140, 'title': 'Panther',
                          'domain': 'Kingdom of Wakanda', 'HP cap': 160, 'Mana cap': 80, "Level": 3}
        actual = game.validate_skill(test_character, test_skill)
        self.assertTrue(actual)
