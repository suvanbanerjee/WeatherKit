import unittest
from current_weather import current_weather

class TestCurrentWeather(unittest.TestCase):
    def setUp(self):
        # Create an instance of current_weather with latitude and longitude
        self.weather = current_weather(37.7749, -122.4194)

    def test_temperature(self):
        # Test getting the current temperature
        temperature = self.weather.temperature()
        self.assertIsInstance(temperature, float)
        self.assertGreaterEqual(temperature, -100)
        self.assertLessEqual(temperature, 100)

    def test_humidity(self):
        # Test getting the current humidity
        humidity = self.weather.humidity()
        self.assertIsInstance(humidity, int)
        self.assertGreaterEqual(humidity, 0)
        self.assertLessEqual(humidity, 100)

    def test_precipitation(self):
        # Test getting the current precipitation
        precipitation = self.weather.precipitation()
        self.assertIsInstance(precipitation, float)
        self.assertGreaterEqual(precipitation, 0)

    def test_weather_code(self):
        # Test getting the current weather code
        weather_code = self.weather.weather_code()
        self.assertIsInstance(weather_code, int)
        self.assertGreaterEqual(weather_code, 0)
        self.assertLessEqual(weather_code, 9)

if __name__ == '__main__':
    unittest.main()