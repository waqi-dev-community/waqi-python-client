import unittest
import requests
from unittest.mock import patch, Mock
import sys

# replace the path below with your own path to run this
sys.path.append('/home/nonso/Documents/Projects/AQI_SDKs/waqi-python-client/src/waqi-python-client')

# Import the classes from your Python code
from waqi_api import WaqiAPI

class WaqiAPITest(unittest.TestCase):

    api_key = 'your_aqicn_api_key'

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.factory = WaqiAPI(self.api_key)


    @patch.object(requests, 'get')
    def test_city_feed_api(self, mock_get):
        mock_response = Mock()
        mock_response.text = '{"data": "city_feed_data"}'
        mock_get.return_value = mock_response

        city_feed_api = self.factory.city_feed()
        city = 'example_city'
        response_city = city_feed_api.set_city(city).fetch()
        
        self.assertEqual(response_city, '{"data": "city_feed_data"}')
        mock_get.assert_called_once_with(f'https://api.waqi.info/feed/{city}/?token={self.api_key}')

    @patch.object(requests, 'get')
    def test_search_api(self, mock_get):
        mock_response = Mock()
        mock_response.text = '{"data": "search_data"}'
        mock_get.return_value = mock_response

        search_api = self.factory.search()
        keyword = "Johannesburg"
        response_search = search_api.set_keyword(keyword).fetch()

        self.assertEqual(response_search, '{"data": "search_data"}')
        mock_get.assert_called_once_with(f'https://api.waqi.info/search/?token={self.api_key}&keyword={keyword}')

    @patch.object(requests, 'get')
    def test_geo_feed_api(self, mock_get):
        mock_response = Mock()
        mock_response.text = '{"data": "geo_feed_data"}'
        mock_get.return_value = mock_response

        geo_feed_api = self.factory.geo_feed()

        lat = 37.7749
        lon = -122.4194
        response_geo = geo_feed_api.set_coordinates(lat, lon).fetch()

        self.assertEqual(response_geo, '{"data": "geo_feed_data"}')
        mock_get.assert_called_once_with(f'https://api.waqi.info/feed/geo:{lat};{lon}/?token={self.api_key}')

    @patch.object(requests, 'get')
    def test_map_stations_api(self, mock_get):
        mock_response = Mock()
        mock_response.text = '{"data": "map_stations_data"}'
        mock_get.return_value = mock_response
        map_stations_api = self.factory.map_station()

        response_map_stations = map_stations_api.set_map_bounds(40.712, -74.006, 34.052, -118.243).fetch()

        self.assertEqual(response_map_stations, '{"data": "map_stations_data"}')
        mock_get.assert_called_once_with(f'https://api.waqi.info/map/bounds/?token={self.api_key}&latlng=40.712,-74.006,34.052,-118.243')


if __name__ == '__main__':
    unittest.main()
