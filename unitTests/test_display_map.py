from unittest import TestCase
from unittest.mock import patch
import unittest.mock
import io
import game


class TestDisplayMap(TestCase):

    @patch('random.randint', return_value=13)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_display_map_all_exclamation_points(self, mock_stdout, _):
        test_rows = 10
        test_columns = 10
        test_sorcerer_character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Level': 1, 'EXP': 30, 'EXP needed': 30,
                                   'title': 'Sorcerer in training', 'domain': 'Temple of Vishanti', 'Current HP': 1,
                                   'Current Mana': 140, 'ATK': 200, 'DEF': 80, 'HP cap': 120, 'Mana cap': 140}
        hypothetical_board = game.make_board(test_rows, test_columns)
        hypothetical_map = game.make_map(test_rows, test_columns)
        game.set_characters(test_sorcerer_character, hypothetical_board, hypothetical_map)
        game.display_map(test_sorcerer_character, hypothetical_map)
        expected = """[1;37;40m
  |  ________________________________________  |  
  |  |YOU||_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_|  |  
  |  |_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_|  |  
  |  |_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_|  |  
  |  |_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_|  |  
  |  |_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_|  |  
  |  |_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_|  |  
  |  |_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_|  |  
  |  |_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_||_[1;33;40m*[1;37;40m_| BOSS  |  
  |  ________________________________________  |  \n"""
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('random.randint', return_value=24)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_display_map_starting_position(self, mock_stdout, _):
        test_rows = 7
        test_columns = 7
        test_sorcerer_character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Level': 1, 'EXP': 30, 'EXP needed': 30,
                                   'title': 'Sorcerer in training', 'domain': 'Temple of Vishanti', 'Current HP': 1,
                                   'Current Mana': 140, 'ATK': 200, 'DEF': 80, 'HP cap': 120, 'Mana cap': 140}
        hypothetical_board = game.make_board(test_rows, test_columns)
        hypothetical_map = game.make_map(test_rows, test_columns)
        game.set_characters(test_sorcerer_character, hypothetical_board, hypothetical_map)
        game.display_map(test_sorcerer_character, hypothetical_map)
        expected = """[1;37;40m
  |  _________________________  |  
  |  |YOU||___||___||___||___|  |  
  |  |___||___||___||___||___|  |  
  |  |___||___||___||___||___|  |  
  |  |___||___||___||___||___|  |  
  |  |___||___||___||___| BOSS  |  
  |  _________________________  |  \n"""
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('random.randint', return_value=3)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_display_map_near_boss(self, mock_stdout, _):
        test_rows = 7
        test_columns = 7
        test_sorcerer_character = {'X-coordinate': 4, 'Y-coordinate': 4, 'Level': 1, 'EXP': 30, 'EXP needed': 30,
                                   'title': 'Sorcerer in training', 'domain': 'Temple of Vishanti', 'Current HP': 1,
                                   'Current Mana': 140, 'ATK': 200, 'DEF': 80, 'HP cap': 120, 'Mana cap': 140}
        hypothetical_board = game.make_board(test_rows, test_columns)
        hypothetical_map = game.make_map(test_rows, test_columns)
        game.set_characters(test_sorcerer_character, hypothetical_board, hypothetical_map)
        game.display_map(test_sorcerer_character, hypothetical_map)
        expected = """[1;37;40m
  |  _________________________  |  
  |  |_[1;36;40m![1;37;40m_||_[1;36;40m![1;37;40m_||_[1;36;40m![1;37;40m_||_[1;36;40m![1;37;40m_||_[1;36;40m![1;37;40m_|  |  
  |  |_[1;36;40m![1;37;40m_||_[1;36;40m![1;37;40m_||_[1;36;40m![1;37;40m_||_[1;36;40m![1;37;40m_||_[1;36;40m![1;37;40m_|  |  
  |  |_[1;36;40m![1;37;40m_||_[1;36;40m![1;37;40m_||_[1;36;40m![1;37;40m_||_[1;36;40m![1;37;40m_||_[1;36;40m![1;37;40m_|  |  
  |  |_[1;36;40m![1;37;40m_||_[1;36;40m![1;37;40m_||_[1;36;40m![1;37;40m_||YOU||_[1;36;40m![1;37;40m_|  |  
  |  |_[1;36;40m![1;37;40m_||_[1;36;40m![1;37;40m_||_[1;36;40m![1;37;40m_||_[1;36;40m![1;37;40m_| BOSS  |  
  |  _________________________  |  
Howard: 'My ducky senses are tingly... Something strong is near.L-Lets proceed with caution.'
"""
        self.assertEqual(mock_stdout.getvalue(), expected)
