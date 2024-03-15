# WeatherKit ☀️
## What is It?
WeatherKit is a python pacakge that provides a simple interface to get weather data without any API key or any other credentials. It is a simple and easy to use package that provides the current weather data of any location in the world. It can get weather details from address, city, country, or latitude and longitude of the location.

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

## Usage
### Current Weather
Sample usage providing city name
```python
import weatherkit
NYC = weatherkit.current_weather('New York')
print(NYC.temperature())
# Output: 20.0
print(NYC.temperature(units='imperial'))
# Output: 68.0
print(NYC.humidity())
# Output: 50
print(NYC.weather_code())
# Output: 3
print(NYC.precipitation())
# Output: 0.0
```
Sample usage providing latitude and longitude

```python
import weatherkit
NYC = weatherkit.current_weather(40.7128, -74.0060)
print(NYC.temperature())
# Output: 20.0
print(NYC.temperature(units='imperial'))
# Output: 68.0
print(NYC.humidity())
# Output: 50
print(NYC.weather_code())
# Output: 3
print(NYC.precipitation())
# Output: 0.0
```
### Daily Forecast
Sample usage providing city name
```python
import weatherkit
NYC = weatherkit.daily_forecast('New York')
print(NYC.max_temperature())
# Output: 20.0
print(NYC.max_temperature(units='imperial'))
# Output: 68.0
print(NYC.min_temperature())
# Output: 10.0
print(NYC.max_temperature(day_offset=3))
# Output: 20.0
print(NYC.max_temperature(day_offset=3, units='imperial'))
# Output: 68.0
print(NYC.prediction_sum())
# Output: 0.0
print(NYC.prediction_sum(day_offset=3))
# Output: 3.2
print(NYC.prediction_sum(units='imperial'))
# Output: 0.0 (in Inches)
print(NYC.weather_code())
# Output: 3
print(NYC.weather_code(day_offset=3))
# Output: 3
```
#### Note 
- Similar to current weather, daily forecast can also be used by providing latitude and longitude.

- day_offset is the number of days from today for which the forecast is required. day_offset=0 (which is default) will give the forecast for today, day_offset=1 will give the forecast for tomorrow and so on.

## Contributing
Contributions are welcome, and they are greatly appreciated! just fork the repository, make changes and create a pull request.

## License
WeatherKit is distributed under the MIT License. See the [LICENSE](https://github.com/suvanbanerjee/weatherkit/blob/main/LICENSE) file for more information.