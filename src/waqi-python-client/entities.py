import requests

class WaqiAPIEntity:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.waqi.info/"
        self.query_params = {}

    def set_query_param(self, param, value):
        self.query_params[param] = value
        return self  # Return the class object to enable method chaining

    def build_query_params(self):
        if not self.query_params:
            return ''
        return '&' + '&'.join([f'{param}={value}' for param, value in self.query_params.items()])

    def fetch(self):
        url = self.url() + '?token=' + self.api_key + self.build_query_params() 
        print(url)
        response = requests.get(url)
        return response.text

    def url(self):
        raise NotImplementedError("Subclasses must implement url()")


class CityFeed(WaqiAPIEntity):
    def set_city(self, city):
        self.query_params['city'] = city
        return self  # Return the class object to enable method chaining

    def url(self):
        # /feed/:city/?token=:token
        url = f'{self.base_url}feed/{self.query_params["city"]}/'
        self.query_params = {}
        return url


class Search(WaqiAPIEntity):
    def set_keyword(self, keyword):
        self.query_params['keyword'] = keyword
        return self  # Return the class object to enable method chaining

    def url(self):
        return f'{self.base_url}search/'

class GeoFeed(WaqiAPIEntity):
    def set_coordinates(self, latitude, longitude):
        self.query_params['lat'] = latitude
        self.query_params['lon'] = longitude
        return self  # Return the class object to enable method chaining

    def url(self):
        # /feed/geo::lat;:lng/?token=:token
        url = f'{self.base_url}feed/geo:{self.query_params["lat"]};{self.query_params["lon"]}/'
        self.query_params = {}
        return url
    

class MapStation(WaqiAPIEntity):
    def set_map_bounds(self, latitude_north, longitude_west, latitude_south, longitude_east):
        self.query_params['latlng'] = f"{latitude_north},{longitude_west},{latitude_south},{longitude_east}"
        return self  # Return the class object to enable method chaining

    def url(self):
        return f'{self.base_url}map/bounds/'
    

class IPFeed(WaqiAPIEntity):
    def set_ip(self, ip_address):
        self.query_params['ip'] = ip_address
        return self
    
    def url(self):
        return f"{self.base_url}feed/here/"


