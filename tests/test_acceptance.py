import unittest
from unittest import mock

import os
import requests_mock

from concourse_demo_python_service import app
from concourse_demo_python_service.animal_repository import AnimalNotFound
from concourse_demo_python_service.colour_repository import ColourNotFound


class TestAcceptance(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    @requests_mock.mock()
    def test_integrated_coloured_animal_returned(self, mock_request):
        os.environ['ANIMAL_SERVICE'] = 'http://animal-service:8080'
        mock_request.get("http://animal-service:8080/animal/c", text="Cat", status_code=200)

        response = self.app.get("/coloured_animal?colour=R&animal=C")

        self.assertEqual(200, response.status_code)
        self.assertEqual(b"Red Cat", response.data)

    @mock.patch('concourse_demo_python_service.colour_repository')
    @mock.patch('concourse_demo_python_service.animal_repository')
    def test_coloured_animal_returned(self, animal_repository, colour_repository):
        animal_repository.fetch_by_letter.return_value = 'Hamster'
        colour_repository.fetch_by_letter.return_value = 'Orange'

        response = self.app.get("/coloured_animal?colour=O&animal=H")

        animal_repository.fetch_by_letter.assert_called_once_with('H')
        colour_repository.fetch_by_letter.assert_called_once_with('O')

        self.assertEqual(200, response.status_code)
        self.assertEqual(b"Orange Hamster", response.data)

    @mock.patch('concourse_demo_python_service.colour_repository')
    @mock.patch('concourse_demo_python_service.animal_repository')
    def test_404_when_colour_not_found(self, animal_repository, colour_repository):
        colour_repository.fetch_by_letter.side_effect = ColourNotFound()
        animal_repository.fetch_by_letter.return_value = 'Dog'

        response = self.app.get("/coloured_animal?colour=O&animal=H")

        self.assertEqual(404, response.status_code)

    @mock.patch('concourse_demo_python_service.colour_repository')
    @mock.patch('concourse_demo_python_service.animal_repository')
    def test_404_when_animal_not_found(self, animal_repository, colour_repository):
        colour_repository.fetch_by_letter.return_value = 'Red'
        animal_repository.fetch_by_letter.side_effect = AnimalNotFound()

        response = self.app.get("/coloured_animal?colour=O&animal=H")

        self.assertEqual(404, response.status_code)

    def test_400_when_animal_is_missing(self):
        response = self.app.get("/coloured_animal?colour=O")

        self.assertEqual(400, response.status_code)

    def test_400_when_colour_is_missing(self):
        response = self.app.get("/coloured_animal?animal=H")

        self.assertEqual(400, response.status_code)