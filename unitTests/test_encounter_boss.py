from unittest import TestCase
import game


class TestEncounterBoss(TestCase):
    def test_encounter_boss_true(self):
        test_boss = {"Name": "Galactus Ultron", 'class': 'boss', "Level": 8, "HP": 700, "ATK": 700,
                     "EXP given": 50}
        test_character = {'X-coordinate': 5, 'Y-coordinate': 5, 'Current HP': 5}
        test_board = game.make_board(7, 7)
        actual = game.encounter_boss(test_character, test_board, test_boss)
        self.assertTrue(actual)

    def test_encounter_boss_false(self):
        test_boss = {"Name": "Galactus Ultron", 'class': 'boss', "Level": 8, "HP": 700, "ATK": 700,
                     "EXP given": 50}
        test_character = {'X-coordinate': 2, 'Y-coordinate': 2, 'Current HP': 5}
        test_board = game.make_board(7, 7)
        actual = game.encounter_boss(test_character, test_board, test_boss)
        self.assertFalse(actual)
