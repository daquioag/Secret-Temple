from unittest import TestCase
import game
from unittest.mock import patch


class TestValidateMove(TestCase):
    def test_validate_move_down_from_starting_position(self):
        test_character_in_starting_position = game.make_character()
        hypothetical_direction = 'down'
        hypothetical_two_by_two_board = game.make_board(4, 4)
        expected = True
        actual = game.validate_move(hypothetical_two_by_two_board, test_character_in_starting_position,
                                    hypothetical_direction)
        self.assertEqual(expected, actual)

    def test_validate_move_left_from_top_right_corner(self):
        test_character_in_top_right_corner = {'X-coordinate': 1, 'Y-coordinate': 4, 'Level': 1, 'EXP': 0,
                                              'EXP needed': 30, 'title': '', 'domain': ''}
        hypothetical_direction = 'right'
        four_by_four_board = game.make_board(6, 6)
        expected = False
        actual = game.validate_move(four_by_four_board, test_character_in_top_right_corner, hypothetical_direction)
        self.assertEqual(expected, actual)

    def test_validate_move_unmodified_character_with_invalid_direction(self):
        test_character_in_starting_position = {'X-coordinate': 1, 'Y-coordinate': 1, 'Level': 1, 'EXP': 0,
                                               'EXP needed': 30, 'title': '', 'domain': ''}
        hypothetical_direction = 'right'
        hypothetical_two_by_two_board = game.make_board(4, 4)
        game.validate_move(hypothetical_two_by_two_board, test_character_in_starting_position, hypothetical_direction)
        unmodified_character_position = {'X-coordinate': 1, 'Y-coordinate': 1, 'Level': 1, 'EXP': 0, 'EXP needed': 30,
                                         'title': '', 'domain': ''}
        self.assertEqual(test_character_in_starting_position, unmodified_character_position)

    @patch('random.randint', return_value=1)
    def test_validate_move_unmodified_board(self, _):
        test_character = {'X-coordinate': 2, 'Y-coordinate': 2, 'Level': 1, 'EXP': 0,
                          'EXP needed': 30, 'title': '', 'domain': ''}
        hypothetical_direction = 'left'
        four_by_four_board = game.make_board(6, 6)
        game.validate_move(four_by_four_board, test_character, hypothetical_direction)
        unmodified_hypothetical_board = game.make_board(6, 6)
        self.assertEqual(four_by_four_board, unmodified_hypothetical_board)
