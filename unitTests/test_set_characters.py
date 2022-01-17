from unittest import TestCase
from unittest.mock import patch
import unittest.mock
import io
import game


class TestSetCharacters(TestCase):

    @patch('random.randint', return_value=0)
    def test_set_characters_default_spots(self, _):
        rows = 6
        columns = 6
        test_character = game.make_character()
        test_board = game.make_board(rows, columns)
        test_map = game.make_map(rows, columns)
        game.set_characters(test_character, test_board, test_map)
        expected_map = [['  |  ', '_____', '_____', '_____', '_____', '  |  '],
                        ['  |  ',
                         '|YOU|',
                         '|_\x1b[1;36;40m!\x1b[1;37;40m_|',
                         '|_\x1b[1;36;40m!\x1b[1;37;40m_|',
                         '|_\x1b[1;36;40m!\x1b[1;37;40m_|',
                         '  |  '],
                        ['  |  ',
                         '|_\x1b[1;36;40m!\x1b[1;37;40m_|',
                         '|_\x1b[1;36;40m!\x1b[1;37;40m_|',
                         '|_\x1b[1;36;40m!\x1b[1;37;40m_|',
                         '|_\x1b[1;36;40m!\x1b[1;37;40m_|',
                         '  |  '],
                        ['  |  ',
                         '|_\x1b[1;36;40m!\x1b[1;37;40m_|',
                         '|_\x1b[1;36;40m!\x1b[1;37;40m_|',
                         '|_\x1b[1;36;40m!\x1b[1;37;40m_|',
                         '|_\x1b[1;36;40m!\x1b[1;37;40m_|',
                         '  |  '],
                        ['  |  ',
                         '|_\x1b[1;36;40m!\x1b[1;37;40m_|',
                         '|_\x1b[1;36;40m!\x1b[1;37;40m_|',
                         '|_\x1b[1;36;40m!\x1b[1;37;40m_|',
                         ' BOSS',
                         '  |  '],
                        ['  |  ', '_____', '_____', '_____', '_____', '  |  ']]
        self.assertEqual(expected_map, test_map)

    def test_set_characters_unmodified(self):
        rows = 7
        columns = 7
        test_character = game.make_character()
        test_board = game.make_board(rows, columns)
        test_map = game.make_map(rows, columns)
        game.set_characters(test_character, test_board, test_map)
        character_unmodified = game.make_character()
        self.assertEqual(character_unmodified, test_character)

    @patch('random.randint', return_value=13)
    def test_set_characters_default_spots_stars(self, _):
        rows = 10
        columns = 10
        test_character = game.make_character()
        test_board = game.make_board(rows, columns)
        test_map = game.make_map(rows, columns)
        game.set_characters(test_character, test_board, test_map)
        expected_map = [['  |  ',
                         '_____',
                         '_____',
                         '_____',
                         '_____',
                         '_____',
                         '_____',
                         '_____',
                         '_____',
                         '  |  '],
                        ['  |  ',
                         '|YOU|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '  |  '],
                        ['  |  ',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '  |  '],
                        ['  |  ',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '  |  '],
                        ['  |  ',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '  |  '],
                        ['  |  ',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '  |  '],
                        ['  |  ',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '  |  '],
                        ['  |  ',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '  |  '],
                        ['  |  ',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         '|_\x1b[1;33;40m*\x1b[1;37;40m_|',
                         ' BOSS',
                         '  |  '],
                        ['  |  ',
                         '_____',
                         '_____',
                         '_____',
                         '_____',
                         '_____',
                         '_____',
                         '_____',
                         '_____',
                         '  |  ']]
        self.assertEqual(expected_map, test_map)
