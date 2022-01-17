from unittest import TestCase
import game
from unittest.mock import patch
import unittest.mock
import io


class TestEnemyFlee(TestCase):
    @patch('random.randint', return_value=2)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_enemy_flee_success(self, mock_stdout, _):
        test_enemy = {"Name": "Test Enemy", 'class': 'enemy'}
        actual = game.enemy_flee(test_enemy)
        expected_print_statement = 'Test Enemy runs away!\n'
        self.assertTrue(actual)
        self.assertEqual(expected_print_statement, mock_stdout.getvalue())

    @patch('random.randint', return_value=10)
    def test_enemy_flee_fail(self, _):
        test_enemy = {"Name": "Test Enemy", 'class': 'enemy'}
        actual = game.enemy_flee(test_enemy)
        self.assertFalse(actual)

    @patch('random.randint', return_value=2)
    def test_enemy_enemy_unmodified(self, _):
        test_enemy = {"Name": "Test Enemy", 'class': 'enemy'}
        game.enemy_flee(test_enemy)
        enemy_unmodified = {"Name": "Test Enemy", 'class': 'enemy'}
        self.assertEqual(test_enemy, enemy_unmodified)
