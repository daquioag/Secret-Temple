from unittest import TestCase

import game


class TestBossDead(TestCase):
    def test_boss_dead_true(self):
        test_boss = {"Name": "Galactus Ultron", 'class': 'boss', "Level": 8, "HP": 0, "ATK": 700, "EXP given": 50}
        actual = game.boss_dead(test_boss)
        self.assertTrue(actual)
