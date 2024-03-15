import unittest
from weatherkit.daily_weather import daily_weather

class TestDailyWeather(unittest.TestCase):
    def setUp(self):
        self.weather = daily_weather(37.7749, -122.4194)

    def test_max_temperature(self):
        temperature = self.weather.max_temperature()
        self.assertIsInstance(temperature, float)
        self.assertGreaterEqual(temperature, -100)
        self.assertLessEqual(temperature, 100)

    def test_min_temperature(self):
        temperature = self.weather.min_temperature()
        self.assertIsInstance(temperature, float)
        self.assertGreaterEqual(temperature, -100)
        self.assertLessEqual(temperature, 100)

    def test_precipitation_sum(self):
        precipitation = self.weather.precipitation_sum()
        self.assertIsInstance(precipitation, float)
        self.assertGreaterEqual(precipitation, 0)

    def test_weather_code(self):
        weather_code = self.weather.weather_code()
        self.assertIsInstance(weather_code, int)
        self.assertGreaterEqual(weather_code, 0)
        self.assertLessEqual(weather_code, 9)

if __name__ == '__main__':
    unittest.main()