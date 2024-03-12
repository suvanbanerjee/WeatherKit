# WeatherKit ☀️
## What is It?
WeatherKit is a python pacakge that provides a simple interface to get weather data without any API key or any other credentials. It is a simple and easy to use package that provides the current weather data of any location in the world. It can get weather details from address, city, country, or even from the latitude and longitude of the location.

Currently it Provies the following weather details for current time and forecast for 7 days:
- Temperature ☀️
- Humidity 💧
- Wind Speed 💨
- Weather Code ⛅️
- Precipitation ☔️

## Where to get it?

The easy way to get WeatherKit is from pip:

```bash
pip install weatherkit
```

## Dependencies
[geopy](https://pypi.org/project/geopy/) - For getting latitude and longitude of the location if the location is given in address or city format.

## Installing from source
Download the source code by cloning the repository or by clicking [here](https://github.com/suvanbanerjee/weatherkit/archive/refs/heads/main.zip)

```
git clone https://github.com/suvanbanerjee/weatherkit.git
cd weatherkit
```
Build the package using the following command:
```
python setup.py sdist bdist_wheel
```
Install the package using the following command:
```
pip install dist/*.whl
```

## Documentation
The documentation of WeatherKit can be found [here](example.com)

## Contributing
Contributions are welcome, and they are greatly appreciated! just fork the repository, make changes and create a pull request.

## License
WeatherKit is distributed under the MIT License. See the [LICENSE](https://github.com/suvanbanerjee/weatherkit/blob/main/LICENSE) file for more information.