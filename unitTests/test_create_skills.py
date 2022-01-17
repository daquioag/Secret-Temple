from unittest import TestCase
import game


class TestCreateSkills(TestCase):
    def test_create_skills_default(self):
        actual = game.create_skills()
        expected = {'1': 'Punch', '2': 'Kick', '9': 'RUN AWAY!'}
        self.assertEqual(actual, expected)
