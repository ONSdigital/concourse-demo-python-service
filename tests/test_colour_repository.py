import unittest

from concourse_demo_python_service import colour_repository


class TestColourRepository(unittest.TestCase):
    def test_returns_red_for_r(self):
        self.assertEqual('Red', colour_repository.fetch_by_letter('r'))

    def test_returns_green_for_g(self):
        self.assertEqual('Green', colour_repository.fetch_by_letter('g'))

    def test_returns_blue_for_b(self):
        self.assertEqual('Blue', colour_repository.fetch_by_letter('b'))

    def test_colour_with_uppercase_letters(self):
        self.assertEqual('Red', colour_repository.fetch_by_letter('R'))

    def test_raise_exception_if_colour_not_found(self):
        with self.assertRaises(colour_repository.ColourNotFound):
            colour_repository.fetch_by_letter('X')
