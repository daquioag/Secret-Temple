from unittest import TestCase
import game


class TestIsAlive(TestCase):
    def test_is_alive_character_is_alive(self):
        character_alive = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 1}
        self.assertTrue(game.is_alive(character_alive))

    def test_is_alive_character_is_dead(self):
        character_dead = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 0}
        self.assertFalse(game.is_alive(character_dead))

    def test_is_alive_character_unmodified(self):
        character_alive = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
        game.is_alive(character_alive)
        character_unmodified = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
        self.assertEqual(character_alive, character_unmodified)
