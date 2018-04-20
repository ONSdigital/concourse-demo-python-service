import unittest

import os
import requests_mock
from requests_mock import mock

from concourse_demo_python_service import animal_repository


class TestAnimalRepository(unittest.TestCase):
    def setUp(self):
        os.environ['ANIMAL_SERVICE'] = 'http://animal-service'

    @requests_mock.mock()
    def test_request_to_animal_service(self, mock_request):
        mock_request.get("http://animal-service/animal/r", text = "Rabbit", status_code = 200)

        self.assertEqual("Rabbit", animal_repository.fetch_by_letter('r'))

    @requests_mock.mock()
    def test_request_to_animal_service_use_lowercase_letter(self, mock_request):
        mock_request.get("http://animal-service/animal/d", text = "Dog", status_code = 200)

        self.assertEqual("Dog", animal_repository.fetch_by_letter('D'))

    @requests_mock.mock()
    def test_raise_exception_if_animal_not_found(self, mock_request):
        mock_request.get("http://animal-service/animal/x", text="", status_code=404)

        with self.assertRaises(animal_repository.AnimalNotFound):
            animal_repository.fetch_by_letter('x')