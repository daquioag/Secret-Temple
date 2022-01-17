from unittest import TestCase
import game
from unittest.mock import patch
import unittest.mock
import io


class TestChooseClass(TestCase):
    @patch('builtins.input', side_effect=[1])
    def test_choose_class_Iron_Heart_Mark_I(self, _):
        test_character = game.make_character()
        test_character.update({'name': 'Test'})
        actual = game.choose_class(test_character)
        expected = "Iron Heart Mark I"
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=[2])
    def test_choose_class_Frog_of_Thunder(self, _):
        test_character = game.make_character()
        test_character.update({'name': 'Test'})
        actual = game.choose_class(test_character)
        expected = "Frog of Thunder"
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=[3])
    def test_choose_class_Panther(self, _):
        test_character = game.make_character()
        test_character.update({'name': 'Test'})
        actual = game.choose_class(test_character)
        expected = "Panther"
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=[4])
    def test_choose_class_Sorcerer_in_training(self, _):
        test_character = game.make_character()
        test_character.update({'name': 'Test'})
        actual = game.choose_class(test_character)
        expected = "Sorcerer in Training"
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=[4])
    def test_choose_class_character_unmodified(self, _):
        test_character = game.make_character()
        test_character.update({'name': 'Test'})
        game.choose_class(test_character)
        expected = {'X-coordinate': 1, 'Y-coordinate': 1, 'Level': 1, 'EXP': 0, 'EXP needed': 30, 'title': '',
                    'domain': '', 'name': 'Test'}
        self.assertEqual(test_character, expected)

    @patch('builtins.input', side_effect=["g", 1])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_class_invalid_option(self, mock_output, _):
        test_character = game.make_character()
        test_character.update({'name': 'Test'})
        game.choose_class(test_character)
        expected = """Howard: "Hey Champ, You wanna pick a class? We gotta get you suped up for the big battle in the Secret Temple"

[1]  Class: Iron Heart Mark I    Stats: HP: 200 Mana: 100 ATK: 120 DEF: 120

[2]  Class: Frog of Thunder    Stats: HP: 220 Mana: 100 ATK: 140 DEF: 80

[3]  Class: Panther    Stats: HP: 160 Mana: 80 ATK: 160 DEF: 140

[4]  Class: Sorcerer in Training    Stats: HP: 140 Mana: 120 ATK: 200 DEF: 80

Howard:"Hey Champ, NO SUCH CLASS EXISTS!! Pick again, and this time, READ THE QUESTION!"
Howard: "Hey Champ, You wanna pick a class? We gotta get you suped up for the big battle in the Secret Temple"

[1]  Class: Iron Heart Mark I    Stats: HP: 200 Mana: 100 ATK: 120 DEF: 120

[2]  Class: Frog of Thunder    Stats: HP: 220 Mana: 100 ATK: 140 DEF: 80

[3]  Class: Panther    Stats: HP: 160 Mana: 80 ATK: 160 DEF: 140

[4]  Class: Sorcerer in Training    Stats: HP: 140 Mana: 120 ATK: 200 DEF: 80
\n"""
        self.assertEqual(mock_output.getvalue(), expected)

    @patch('builtins.input', side_effect=[3])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_class_print_statement(self, mock_output, _):
        test_character = game.make_character()
        test_character.update({'name': 'Test'})
        game.choose_class(test_character)
        expected = """Howard: "Hey Champ, You wanna pick a class? We gotta get you suped up for the big battle in the Secret Temple"

[1]  Class: Iron Heart Mark I    Stats: HP: 200 Mana: 100 ATK: 120 DEF: 120

[2]  Class: Frog of Thunder    Stats: HP: 220 Mana: 100 ATK: 140 DEF: 80

[3]  Class: Panther    Stats: HP: 160 Mana: 80 ATK: 160 DEF: 140

[4]  Class: Sorcerer in Training    Stats: HP: 140 Mana: 120 ATK: 200 DEF: 80
\n"""
        self.assertEqual(mock_output.getvalue(), expected)


if __name__ == '__main__':
    unittest.main()
