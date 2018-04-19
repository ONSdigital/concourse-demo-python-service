import unittest

from concourse_demo_python_service import colour_repository


class TestColourRepository(unittest.TestCase):
    def test_returns_red_for_r(self):
        self.assertEqual(colour_repository.fetch_by_letter('r'), 'Red')

    def test_returns_green_for_g(self):
        self.assertEqual(colour_repository.fetch_by_letter('g'), 'Green')

    def test_returns_blue_for_b(self):
        self.assertEqual(colour_repository.fetch_by_letter('b'), 'Blue')

    def test_colour_with_uppercase_letters(self):
        self.assertEqual(colour_repository.fetch_by_letter('R'), 'Red')

    def test_raise_exception_if_colour_not_found(self):
        with self.assertRaises(colour_repository.ColourNotFound):
            colour_repository.fetch_by_letter('X')
