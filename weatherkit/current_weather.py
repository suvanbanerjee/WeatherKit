# Copyright (c) 2024 Suvan Banerjee <banerjeesuvan@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

'''
Imports
'''
import geopy
import requests
import json

def is_float(n):
    '''
    This function is used to check if a number is a float.
    In this module it is use to check if the latitude and longitude are valid.
    '''
    try:
        float(n)
        return True
    except:
        return False

class current_weather:
    '''
    This class is used to get current weather details of any city in the world.
    '''
    def __init__(self, lat,lon=None):
        '''
        This is the constructor of the Weather class.
        '''
        if lon or ( is_float(lat) and is_float(lon)):
            self.lat = lat
            self.lon = lon
        else:
            try:
                geolocator = geopy.geocoders.Nominatim(user_agent="geoapiExercises")
                location = geolocator.geocode(lat)
                self.lat = location.latitude
                self.lon = location.longitude
            except:
                self.lat = None
                self.lon = None

    def temperature(self,units='metric'):
        '''
        This method is used to get the current temperature of the city.
        '''
        if self.lat and self.lon:
            url = "https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&current=temperature_2m".format(self.lat, self.lon)
            if units == 'imperical':
                url = url + "&temperature_unit=fahrenheit"
            try:
                data = requests.get(url).json()
                return data["current"]["temperature_2m"]
            except Exception as e:
                return "Error fetching weather data:", e
        else:
            return "Invalid Latitude or Longitude"
        
    def humidity(self):
        '''
        This method is used to get the current humidity of the city.
        '''
        if self.lat and self.lon:
            url = "https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&current=relative_humidity_2m".format(self.lat, self.lon)
            try:
                data = requests.get(url).json()
                return data["current"]["relative_humidity_2m"]
            except Exception as e:
                return "Error fetching weather data:", e
        else:
            return "Invalid Latitude or Longitude"
    def precipitation(self,units='metric'):
        '''
        This method is used to get the current precipitation of the city.
        '''
        if self.lat and self.lon:
            url = "https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&current=precipitation".format(self.lat, self.lon)
            if units == 'imperical':
                url = url + "&precipitation_unit=inch"
            try:
                data = requests.get(url).json()
                return data["current"]["precipitation"]
            except Exception as e:
                return "Error fetching weather data:", e
        else:
            return "Invalid Latitude or Longitude"
    def weather_code(self):
        '''
        This method is used to get the current weather code of the city.
        '''
        if self.lat and self.lon:
            url = "https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&current=weather_code".format(self.lat, self.lon)
            try:
                data = requests.get(url).json()
                return data["current"]["weather_code"]
            except Exception as e:
                return "Error fetching weather data:", e
        else:
            return "Invalid Latitude or Longitude"