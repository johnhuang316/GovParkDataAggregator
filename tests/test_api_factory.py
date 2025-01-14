import unittest
from api.apifactory import ApiFactory
from api.iapi import IApi
from api.cities.newtaipeiapi import NewTaipeiApi
from api.cities.taipeiapi import TaipeiApi
from api.cities.taoyuanapi import TaoyuanApi

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
            self.assertEqual(api.__class__.__name__.lower(), api_name.lower() + "api")

    def test_get_invalid_api(self):
        """Test getting invalid API."""
        with self.assertRaises(ValueError):
            self.api_factory.get_api("InvalidCity")

    def test_get_all_apis(self):
        """Test getting all APIs."""
        apis = self.api_factory.get_all_apis()
        self.assertEqual(len(apis), 3)
        api_names = [api.__class__.__name__.lower() for api in apis]
        self.assertIn("taipeiapi", api_names)
        self.assertIn("taoyuanapi", api_names)
        self.assertIn("newtaipeiapi", api_names)

if __name__ == '__main__':
    unittest.main()
