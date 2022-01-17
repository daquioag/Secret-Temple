from unittest import TestCase
import game
from unittest.mock import patch


class TestListOfTitles(TestCase):
    @patch('builtins.input', side_effect=[1])
    def test_list_of_titles_house_of_iron_class_titles(self, _):
        iron_heart_character = game.make_character()
        iron_heart_character.update({'name': 'Test'})
        iron_heart_title = game.choose_class(iron_heart_character)
        game.add_class_stats(iron_heart_character, iron_heart_title)
        actual = game.list_of_titles(iron_heart_character)
        expected = ["Iron Heart Mark I", "Iron Heart Mark III", "Iron Heart MK 40", "Iron Heart Mark XXII: Thorbuster",
                    "Iron Heart Mark XLIV: Thanos-Buster"]
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=[2])
    def test_list_of_titles_asgardian_republic_class_titles(self, _):
        frog_of_thunder_character = game.make_character()
        frog_of_thunder_character.update({'name': 'Test'})
        frog_of_thunder_title = game.choose_class(frog_of_thunder_character)
        game.add_class_stats(frog_of_thunder_character, frog_of_thunder_title)
        actual = game.list_of_titles(frog_of_thunder_character)
        expected = ["Frog of Thunder", "Thor Odinson", "God of Thunder", "Unworthy Thor", "God King Thor"]
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=[3])
    def test_list_of_titles_kingdom_of_wakanda_class_titles(self, _):
        panther_character = game.make_character()
        panther_character.update({'name': 'Test'})
        panther_title = game.choose_class(panther_character)
        game.add_class_stats(panther_character, panther_title)
        actual = game.list_of_titles(panther_character)
        expected = ["Panther", "Coal Tiger", "Ghost Panther", "The Black Panther", "King of Necropolis"]
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=[4])
    def test_list_of_titles_Temple_of_Vishanti_class_titles(self, _):
        panther_character = game.make_character()
        panther_character.update({'name': 'Test'})
        panther_title = game.choose_class(panther_character)
        game.add_class_stats(panther_character, panther_title)
        actual = game.list_of_titles(panther_character)
        expected = ["Sorcerer in Training", "Master of the Mystic Arts", "Sorcerer Supreme",
                    "Disciple of Dormamu", "Dr. StrangeFate"]
        self.assertEqual(actual, expected)
