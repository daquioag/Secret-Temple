from unittest import TestCase
import game


class TestMoveCharacter(TestCase):
    def test_move_character_right(self):
        default_character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}
        direction = "right"
        game.move_character(default_character, direction)
        self.assertTrue(default_character["X-coordinate"] == 1 and default_character["Y-coordinate"] == 2)

    def test_move_character_up(self):
        test_character = {"X-coordinate": 3, "Y-coordinate": 2, "Current HP": 5}
        direction = "up"
        game.move_character(test_character, direction)
        self.assertTrue(test_character["X-coordinate"] == 2 and test_character["Y-coordinate"] == 2)

    def test_move_character_left(self):
        test_character = {"X-coordinate": 3, "Y-coordinate": 2, "Current HP": 5}
        direction = "left"
        game.move_character(test_character, direction)
        self.assertTrue(test_character["X-coordinate"] == 3 and test_character["Y-coordinate"] == 1)
