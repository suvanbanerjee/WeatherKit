# Usage

## Current Weather

Current weather can be accessed by creating an object of the `current_weather` class. The object can be created by providing the city name or the latitude and longitude of the location. The object provides the following methods to get the weather details:
### Sample usage providing city name

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

### Sample usage providing latitude and longitude

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
## Daily Forecast

Daily forecast can be accessed by creating an object of the `daily_forecast` class. The object can be created by providing the city name or the latitude and longitude of the location. The object provides the following methods to get the weather details:

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
print(NYC.precipitation_sum())
# Output: 0.0
print(NYC.precipitation_sum(day_offset=3))
# Output: 3.2
print(NYC.precipitation_sum(units='imperial'))
# Output: 0.0 (in Inches)
print(NYC.weather_code())
# Output: 3
print(NYC.weather_code(day_offset=3))
# Output: 3
```
### Note 
- Similar to current weather, daily forecast can also be used by providing latitude and longitude.

- day_offset is the number of days from today for which the forecast is required. day_offset=0 (which is default) will give the forecast for today, day_offset=1 will give the forecast for tomorrow and so on.
