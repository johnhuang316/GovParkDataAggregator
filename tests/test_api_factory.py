import unittest
from api import ApiFactory, IApi

class TestApiFactory(unittest.TestCase):
    def setUp(self):
        """Set up test cases."""
        self.api_factory = ApiFactory()

    def test_get_valid_api(self):
        """Test getting valid APIs."""
        # Test each supported city
        apis = ["Taipei", "Taoyuan", "NewTaipei"]
        for api_name in apis:
            api = self.api_factory.get_api(api_name)
            self.assertIsNotNone(api)
            self.assertTrue(isinstance(api, IApi))
            self.assertEqual(api.api_name, api_name)

    def test_get_invalid_api(self):
        """Test getting invalid API."""
        with self.assertRaises(ValueError):
            self.api_factory.get_api("InvalidCity")

if __name__ == '__main__':
    unittest.main()
