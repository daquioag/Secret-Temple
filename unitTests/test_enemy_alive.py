from unittest import TestCase
import game


class TestEnemyAlive(TestCase):
    def test_enemy_alive_true(self):
        foe_test = {"Name": "Kree", 'class': 'enemy', "Level": 2, "HP": 120, "ATK": 120, "EXP given": 15}
        actual = game.enemy_alive(foe_test)
        self.assertTrue(actual)

    def test_enemy_alive_false(self):
        foe_test = {"Name": "Kree", 'class': 'enemy', "Level": 2, "HP": 0, "ATK": 120, "EXP given": 15}
        actual = game.enemy_alive(foe_test)
        self.assertFalse(actual)
