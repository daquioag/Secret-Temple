from unittest import TestCase
import game


class TestUpgradeSkills(TestCase):
    def test_upgrade_skills_level_1(self):
        test_character = {'Level': 1, 'domain': "Asgardian Republic"}
        default_skills = {"1": 'Punch', "2": 'Kick', "9": "RUN AWAY!"}
        game.upgrade_skills(default_skills, test_character)
        expected_skills = {"1": 'Punch', "2": 'Kick', "9": "RUN AWAY!"}
        self.assertEqual(default_skills, expected_skills)

    def test_upgrade_skills_level_2(self):
        test_character = {'Level': 2, 'domain': "Asgardian Republic"}
        default_skills = {"1": 'Punch', "2": 'Kick', "9": "RUN AWAY!"}
        game.upgrade_skills(default_skills, test_character)
        expected_skills = {"1": 'Punch', "2": "Throw Mjolnir", "3": 'Crashing Thunder', "9": "RUN AWAY!"}
        self.assertEqual(default_skills, expected_skills)

    def test_upgrade_skills_level_3_gradually(self):
        test_character = {'Level': 1, 'domain': "Asgardian Republic"}
        default_skills = {"1": 'Punch', "2": 'Kick', "9": "RUN AWAY!"}
        game.upgrade_skills(default_skills, test_character)
        test_character["Level"] += 1  # gain a level (now level 2)
        game.upgrade_skills(default_skills, test_character)
        test_character["Level"] += 1  # gain a level (now level 3)
        game.upgrade_skills(default_skills, test_character)
        expected_skills = {"1": 'Stormbreaker and Mjolnir Combo', "2": "Throw Mjolnir", "3": 'Crashing Thunder',
                           "4": "Ultimate Ability: Legacy of Odinson", "9": "RUN AWAY!"}
        self.assertEqual(default_skills, expected_skills)
