from unittest import TestCase
import game
from unittest.mock import patch
import unittest.mock
import io


class TestCheckForFoes(TestCase):
    @patch('random.randint', return_value=1)
    @patch('builtins.input', side_effect=["y"])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_check_for_foes_enemy_attacks_you_fight(self, mock_response, _, __):
        game.check_for_foes()
        expected_print_statement = "Howard: 'Quack! Look out, an enemy is attacking!" \
                                   "\nHoward: HECK YEAH!! WE GONNA MESS YOU UP!\n"
        self.assertEqual(expected_print_statement, mock_response.getvalue())

    @patch('random.randint', return_value=2)
    @patch('builtins.input', side_effect=["n"])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_check_for_foes_enemy_attacks_you_run(self, mock_response, _, __):
        game.check_for_foes()
        expected_print_statement = "Howard: 'Quack! Look out, an enemy is attacking!" \
                                   "\nYou scream \"Bawk Bawk!\" as you run away.\n"
        self.assertEqual(expected_print_statement, mock_response.getvalue())

    @patch('random.randint', return_value=3)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_check_for_foes_enemy_doesnt_attack(self, mock_response, _):
        game.check_for_foes()
        expected_print_statement = "Howard: 'quack! I dont see any enemies here...\n"
        self.assertEqual(expected_print_statement, mock_response.getvalue())

    @patch('random.randint', return_value=10)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_check_for_foes_enemy_doesnt_attack_again(self, mock_response, _):
        game.check_for_foes()
        expected_print_statement = "Howard: 'quack! I dont see any enemies here...\n"
        self.assertEqual(expected_print_statement, mock_response.getvalue())
