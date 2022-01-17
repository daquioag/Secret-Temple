import unittest
from unittest import TestCase
import game
from unittest.mock import patch
import unittest.mock
import io


class TestCreateName(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["Chris", "a"])
    def test_create_name_chris(self, _, mock_stdout):
        test_character = game.make_character()
        game.create_name(test_character)
        expected = "Chris"
        expected_print_statement = """You You wake up, dazed. You see a a giant temple in front of you.
???: Hey, Champ!. Get up, we got work to do!
Confused, you look down. You see a duck.
???: Whats Your name, Champ?!
It talks. The Duck talks.
???: Chris? Weird name.
???: My name Is Howard, Howard The Duck
[1;33;40m
[0m
"""
        self.assertEqual(expected, test_character['name'])
        self.assertEqual(expected_print_statement, mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["", ""])
    def test_create_name_empty_values(self, _, mock_stdout):
        test_character = game.make_character()
        game.create_name(test_character)
        expected = ""
        expected_print_statement = """You You wake up, dazed. You see a a giant temple in front of you.
???: Hey, Champ!. Get up, we got work to do!
Confused, you look down. You see a duck.
???: Whats Your name, Champ?!
It talks. The Duck talks.
???: ? Weird name.
???: My name Is Howard, Howard The Duck
[1;33;40m
[0m
"""
        self.assertEqual(expected, test_character['name'])
        self.assertEqual(expected_print_statement, mock_stdout.getvalue())

    @patch('builtins.input', side_effect=["Test", "a"])
    def test_create_name_other_key_value_pairs_unmodified(self, _):
        test_character = game.make_character()
        game.create_name(test_character)
        expected = {'X-coordinate': 1, 'Y-coordinate': 1, 'Level': 1, 'EXP': 0, 'EXP needed': 30, 'title': '', 'domain': '', 'name': 'Test'}
        self.assertEqual(expected, test_character)








