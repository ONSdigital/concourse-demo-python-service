import unittest

from concourse_demo_python_service import app


class TestAcceptance(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_coloured_animal_returned(self):
        response = self.app.get("/coloured_animal?colour=R&animal=C")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Red Cat")
