from unittest import TestCase
import game
from unittest.mock import patch
import unittest.mock
import io


class TestFightOrRun(TestCase):
    @patch('builtins.input', side_effect=["y"])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_fight_or_run_fight(self, mock_response, _):
        actual = game.fight_or_run()
        expected_print_statement = "Howard: HECK YEAH!! WE GONNA MESS YOU UP!\n"
        self.assertTrue(actual)
        self.assertEqual(mock_response.getvalue(), expected_print_statement)

    @patch('builtins.input', side_effect=["Y"])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_fight_or_run_fight_upper_case_Y(self, mock_response, _):
        actual = game.fight_or_run()
        expected_print_statement = "Howard: HECK YEAH!! WE GONNA MESS YOU UP!\n"
        self.assertTrue(actual)
        self.assertEqual(mock_response.getvalue(), expected_print_statement)

    @patch('builtins.input', side_effect=["n"])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_fight_or_run_run(self, mock_response, _):
        expected_print_statement = "You scream \"Bawk Bawk!\" as you run away.\n"
        actual = game.fight_or_run()
        self.assertFalse(actual)
        self.assertEqual(mock_response.getvalue(), expected_print_statement)

    @patch('builtins.input', side_effect=[1, "y"])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_fight_or_run_invalid_input(self, mock_response, _):
        expected_print_statement = "Howard: Are you daft?! That is not a valid response!" \
                                   "\nHoward: HECK YEAH!! WE GONNA MESS YOU UP!\n"
        actual = game.fight_or_run()
        self.assertTrue(actual)
        self.assertEqual(mock_response.getvalue(), expected_print_statement)
