from unittest import TestCase
from unittest.mock import patch
import game


class TestMakeBoard(TestCase):
    @patch('random.randint', return_value=1)
    def test_make_board_with_only_iron_man_suits(self, _):
        test_rows = 4
        test_columns = 4
        actual = {(0, 0): 'a wrecked room full of shattered iron man suits.\n'
                          "Howard: 'Where could have Tony gone?!'",
                  (0, 1): 'a wrecked room full of shattered iron man suits.\n'
                          "Howard: 'Where could have Tony gone?!'",
                  (0, 2): 'a wrecked room full of shattered iron man suits.\n'
                          "Howard: 'Where could have Tony gone?!'",
                  (0, 3): 'a wrecked room full of shattered iron man suits.\n'
                          "Howard: 'Where could have Tony gone?!'",
                  (1, 0): 'a wrecked room full of shattered iron man suits.\n'
                          "Howard: 'Where could have Tony gone?!'",
                  (1, 1): 'a wrecked room full of shattered iron man suits.\n'
                          "Howard: 'Where could have Tony gone?!'",
                  (1, 2): 'a wrecked room full of shattered iron man suits.\n'
                          "Howard: 'Where could have Tony gone?!'",
                  (1, 3): 'a wrecked room full of shattered iron man suits.\n'
                          "Howard: 'Where could have Tony gone?!'",
                  (2, 0): 'a wrecked room full of shattered iron man suits.\n'
                          "Howard: 'Where could have Tony gone?!'",
                  (2, 1): 'a wrecked room full of shattered iron man suits.\n'
                          "Howard: 'Where could have Tony gone?!'",
                  (2, 2): 'The Final Destination',
                  (2, 3): 'a wrecked room full of shattered iron man suits.\n'
                          "Howard: 'Where could have Tony gone?!'",
                  (3, 0): 'a wrecked room full of shattered iron man suits.\n'
                          "Howard: 'Where could have Tony gone?!'",
                  (3, 1): 'a wrecked room full of shattered iron man suits.\n'
                          "Howard: 'Where could have Tony gone?!'",
                  (3, 2): 'a wrecked room full of shattered iron man suits.\n'
                          "Howard: 'Where could have Tony gone?!'",
                  (3, 3): 'a wrecked room full of shattered iron man suits.\n'
                          "Howard: 'Where could have Tony gone?!'"}
        expected = game.make_board(test_rows, test_columns)
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=14)
    def test_make_board_with_only_doll_rooms(self, _):
        test_rows = 7
        test_columns = 7
        actual = {(0, 0): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'",
                  (0, 1): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'",
                  (0, 2): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'",
                  (0, 3): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'",
                  (0, 4): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'",
                  (0, 5): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'",
                  (0, 6): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'",
                  (1, 0): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'",
                  (1, 1): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'",
                  (1, 2): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'",
                  (1, 3): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'",
                  (1, 4): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'",
                  (1, 5): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'",
                  (1, 6): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'",
                  (2, 0): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'",
                  (2, 1): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'",
                  (2, 2): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'",
                  (2, 3): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'",
                  (2, 4): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'",
                  (2, 5): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'",
                  (2, 6): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'",
                  (3, 0): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'",
                  (3, 1): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'",
                  (3, 2): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'",
                  (3, 3): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'",
                  (3, 4): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'",
                  (3, 5): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'",
                  (3, 6): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'",
                  (4, 0): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'",
                  (4, 1): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'",
                  (4, 2): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'",
                  (4, 3): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'",
                  (4, 4): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'",
                  (4, 5): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'",
                  (4, 6): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'",
                  (5, 0): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'",
                  (5, 1): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'",
                  (5, 2): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'",
                  (5, 3): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'",
                  (5, 4): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'",
                  (5, 5): 'The Final Destination',
                  (5, 6): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'",
                  (6, 0): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'",
                  (6, 1): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'",
                  (6, 2): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'",
                  (6, 3): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'",
                  (6, 4): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'",
                  (6, 5): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'",
                  (6, 6): 'a room full of bloody webs.\n'
                          "Howard: 'Peter's in trouble! We gotta help him!'"}
        expected = game.make_board(test_rows, test_columns)
        self.assertEqual(expected, actual)
