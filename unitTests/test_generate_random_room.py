from unittest import TestCase
import game
from unittest.mock import patch


class TestGenerateRandomRoom(TestCase):
    @patch('random.randint', return_value=1)
    def test_generate_random_room_empty_room(self, _):
        actual = "a wrecked room full of shattered iron man suits." \
                 "\nHoward: 'Where could have Tony gone?!'"
        expected = game.generate_random_room()
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=5)
    def test_generate_random_room__another_empty_room(self, _):
        actual = "an empty room with used arrows and a broken quiver." \
                 "\nHoward: 'We need to find Clint!'"
        expected = game.generate_random_room()
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=25)
    def test_generate_random_room_a_doll_room(self, _):
        actual = "a room with enemy bodies in pieces. Mystic energy fills the air. " \
                 "\nHoward: \"Wanda was just here. She's close by.\""
        expected = game.generate_random_room()
        self.assertEqual(expected, actual)
