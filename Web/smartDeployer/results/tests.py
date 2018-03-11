import unittest

class TestBasic(unittest.TestCase):
    "Basic tests"

    def test_get(self):
        """hello view actually tells 'Hello'."""
        # Setup.
        request = 'fake request'
        # Run.
        response = views.team(request)
        # Check.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, {})