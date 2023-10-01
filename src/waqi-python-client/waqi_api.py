from entities import CityFeed, IPFeed, Search, GeoFeed, MapStation
# Factory class for creating API objects
class WaqiAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def city_feed(self):
        return CityFeed(self.api_key)

    def search(self):
        return Search(self.api_key)
    
    def geo_feed(self):
        return GeoFeed(self.api_key)
    
    def ip_feed(self):
        return IPFeed(self.api_key)
    
    def map_station(self):
        return MapStation(self.api_key)