import unittest
from unittest import mock

from concourse_demo_python_service import app
from concourse_demo_python_service.colour_repository import ColourNotFound


class TestAcceptance(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_integrated_coloured_animal_returned(self):
        response = self.app.get("/coloured_animal?colour=R&animal=C")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Red Cat")

    @mock.patch('concourse_demo_python_service.colour_repository')
    @mock.patch('concourse_demo_python_service.animal_repository')
    def test_coloured_animal_returned(self, animal_repository, colour_repository):
        animal_repository.fetch_by_letter.return_value = 'Hamster'
        colour_repository.fetch_by_letter.return_value = 'Orange'

        response = self.app.get("/coloured_animal?colour=O&animal=H")

        animal_repository.fetch_by_letter.assert_called_once_with('H')
        colour_repository.fetch_by_letter.assert_called_once_with('O')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Orange Hamster")

    @mock.patch('concourse_demo_python_service.colour_repository')
    @mock.patch('concourse_demo_python_service.animal_repository')
    def test_404_when_colour_not_found(self, animal_repository, colour_repository):
        colour_repository.fetch_by_letter.side_effect = ColourNotFound()
        animal_repository.fetch_by_letter.return_value = 'Dog'

        response = self.app.get("/coloured_animal?colour=O&animal=H")

        self.assertEqual(response.status_code, 404)