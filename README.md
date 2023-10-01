# WAQI Python Client

Python client library for the World Air Quality Index (WAQI) APIs. See documentation [here](https://aqicn.org/json-api/doc/).
All available API modules are supported - City feed, Geolocalized feed, Search, and Map Queries.

### Installation

You can install this package with composer using the command below

```shell
 composer require nonsoniyi/waqi-php-client
```

### Get API key

Sign up for an API key [here](https://aqicn.org/data-platform/token/)

### Making Requests

The primary `WAQI\API` class is a factory class that creates objects for each of the API modules, allowing you to make requests to any of them with your desired request parameters. You have to first create an object for it, then access your desired API module via the object. See the code snippets below:

```py
from waqi_api import WaqiAPI

api = WaqiAPI(WAQI_TOKEN)
```

**For City Feed:**

```py
response = api.city_feed().set_city("Munich").fetch()
```

**For Search:**

```py
response = api.search().set_keyword("Johannesburg").fetch()
```

**For Lat/Lng based Geolocalized feed:**

```py
response = api.geo_feed().set_coordinates(37.7749, -122.4194).fetch()
```

**For IP based Geolocalized feed:**

```py
response = api.ip_feed().set_ip("MY_IP").fetch()
```

**For Map Queries:**

```py
response = api.map_station().set_map_bounds(40.712, -74.006, 34.052, -118.243).fetch()
```
