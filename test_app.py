from app import app
from unittest import TestCase

class MadlibsFormTestCase(TestCase):
    def test_form(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1 id="story-header">Dadlibs.</h1>', html)