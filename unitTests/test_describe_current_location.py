from unittest import TestCase
from unittest import TestCase
import game
from unittest.mock import patch
import unittest.mock
import io


class TestDescribeCurrentLocation(TestCase):
    @patch('random.randint', return_value=1)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_middle_of_map(self, mock_stdout, _):
        test_board = game.make_board(6, 6)
        character_in_middle_of_map = {'X-coordinate': 2, 'Y-coordinate': 2, 'Level': 5, 'EXP': 0,
                                      'EXP needed': 480,
                                      'title': 'Sorcerer in Training', 'domain': 'Temple of Vishanti',
                                      'Current HP': 820,
                                      'Current Mana': 840, 'ATK': 900, 'DEF': 780, 'HP cap': 820,
                                      'Mana cap': 840,
                                      "name": "random_name"}
        game.describe_current_location(test_board, character_in_middle_of_map)
        expected = """[1;31;40m
random_name, Sorcerer in Training, is in a wrecked room full of shattered iron man suits.
Howard: 'Where could have Tony gone?!' [1;37;40m[coordinates: (2, 2)]
[1;31;0m\n"""  # returns None
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_starting_position(self, mock_stdout):
        test_board = game.make_board(27, 27)
        character_in_end_goal = {'X-coordinate': 25, 'Y-coordinate': 25, 'Level': 5, 'EXP': 0,
                                 'EXP needed': 480,
                                 'title': 'Sorcerer in Training', 'domain': 'Temple of Vishanti',
                                 'Current HP': 820,
                                 'Current Mana': 840, 'ATK': 900, 'DEF': 780, 'HP cap': 820,
                                 'Mana cap': 840,
                                 "name": "random_name"}
        game.describe_current_location(test_board, character_in_end_goal)
        expected = """[1;31;40m
random_name, Sorcerer in Training, is in The Final Destination [1;37;40m[coordinates: (25, 25)]
[1;31;0m\n"""
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('random.randint', return_value=4)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_unmodified_board(self, _, __):
        test_board = game.make_board(10, 10)
        thunder_frog_character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Level': 1, 'EXP': 0, 'EXP needed': 30,
                                  'title': 'Frog of Thunder', 'domain': 'Asgardian Republic', 'name': 'Test',
                                  'Current HP': 220, 'Current Mana': 100, 'ATK': 140, 'DEF': 80, 'HP cap': 220,
                                  'Mana cap': 100}
        game.describe_current_location(test_board, thunder_frog_character)
        unmodified_board = game.make_board(10, 10)
        self.assertEqual(test_board, unmodified_board)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_unmodified_character(self, _):
        test_board = game.make_board(10, 10)
        thunder_frog_character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Level': 1, 'EXP': 0, 'EXP needed': 30,
                                  'title': 'Frog of Thunder', 'domain': 'Asgardian Republic', 'name': 'Test',
                                  'Current HP': 220, 'Current Mana': 100, 'ATK': 140, 'DEF': 80, 'HP cap': 220,
                                  'Mana cap': 100}
        game.describe_current_location(test_board, thunder_frog_character)
        unmodified_character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Level': 1, 'EXP': 0, 'EXP needed': 30,
                                'title': 'Frog of Thunder', 'domain': 'Asgardian Republic', 'name': 'Test',
                                'Current HP': 220, 'Current Mana': 100, 'ATK': 140, 'DEF': 80, 'HP cap': 220,
                                'Mana cap': 100}
        self.assertEqual(thunder_frog_character, unmodified_character)
