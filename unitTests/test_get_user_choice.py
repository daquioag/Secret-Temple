from unittest import TestCase
from unittest.mock import patch
import game
import unittest.mock
import io


class TestGetUserChoice(TestCase):
    @patch('builtins.input', side_effect=[1])
    def test_get_user_choice_go_up(self, _):
        expected = "up"
        actual = game.get_user_choice()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=[2])
    def test_get_user_choice_go_down(self, _):
        expected = "down"
        actual = game.get_user_choice()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=[3])
    def test_get_user_choice_go_left(self, _):
        expected = "left"
        actual = game.get_user_choice()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=[4])
    def test_get_user_choice_go_right(self, _):
        actual = game.get_user_choice()
        expected = "right"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["Q"])
    def test_get_user_choice_quit_upper_case_Q(self, _):
        actual = game.get_user_choice()
        expected = "quit"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["q"])
    def test_get_user_choice_quit_lower_case_q(self, _):
        actual = game.get_user_choice()
        expected = "quit"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["g", 4])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_invalid_input(self, mock_response, _):
        game.get_user_choice()
        expected = ("1 up"
                    "\n2 down"
                    "\n3 left"
                    "\n4 right"
                    "\nq quit"
                    "\nThat is an invalid number!"
                    "\nPlease pick again\n"
                    "\n1 up"
                    "\n2 down"
                    "\n3 left"
                    "\n4 right"
                    "\nq quit"
                    "\nYou choose to move through a portal in the rightward direction\n")
        self.assertEqual(mock_response.getvalue(), expected)
