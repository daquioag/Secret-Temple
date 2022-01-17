from unittest import TestCase
import game
from unittest.mock import patch
import unittest.mock
import io


class TestDescribeCurrentStatus(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_status_panther(self, mock_response):
        test_character = {'name': 'TChalla', 'EXP': 0, 'EXP needed': 60, 'Current HP': 160,
                          'Current Mana': 80, 'ATK': 160, 'DEF': 140, 'title': 'Panther',
                          'domain': 'Kingdom of Wakanda', 'HP cap': 160, 'Mana cap': 80, "Level": 2}
        default_skills = {'1': 'Punch', '2': 'King\'s Mercy', "3": "Vibranium Burst", '9': 'RUN AWAY!'}
        game.describe_current_status(test_character, default_skills)
        actual = "\033[1;32;40mTChalla, Panther, from the Kingdom of Wakanda, Level: 2" \
                 "\nHP: 160/160   Mana:80/80  ATK: 160  DEF: 140  EXP:  0/60  Abilities: Punch, King\'s Mercy, Vibranium Burst, RUN AWAY!\n"
        self.assertEqual(actual, mock_response.getvalue())
