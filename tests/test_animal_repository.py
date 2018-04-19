import unittest

from concourse_demo_python_service import animal_repository


class TestAnimalRepository(unittest.TestCase):
    def test_returns_cat_for_c(self):
        self.assertEqual('Cat', animal_repository.fetch_by_letter('c'))

    def test_returns_dog_for_d(self):
        self.assertEqual('Dog', animal_repository.fetch_by_letter('d'))

    def test_returns_snake_for_s(self):
        self.assertEqual('Snake', animal_repository.fetch_by_letter('s'))

    def test_animal_with_uppercase_letters(self):
        self.assertEqual('Cat', animal_repository.fetch_by_letter('C'))

    def test_raise_exception_if_animal_not_found(self):
        with self.assertRaises(animal_repository.AnimalNotFound):
            animal_repository.fetch_by_letter('X')