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

class daily_weather:
    '''
    This class is used to get daily weather details of any city in the world.
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
    def max_temperature(self,units='metric'):
        '''
        This method is used to get the maximum temperature of a city.
        '''
        if self.lat and self.lon:
            url = "https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&daily=temperature_2m_max".format(self.lat, self.lon)
            try:
                data = requests.get(url).json()
                temp = data["daily"]["temperature_2m_max"][0]
                return temp
            except Exception as e:
                print("Error fetching weather data:", e)
        else:
            print("Invalid Latitude and Longitude")
    
    def min_temperature(self,units='metric'):
        '''
        This method is used to get the minimum temperature of a city.
        '''
        if self.lat and self.lon:
            url = "https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&daily=temperature_2m_min".format(self.lat, self.lon)
            try:
                data = requests.get(url).json()
                temp = data["daily"]["temperature_2m_min"][0]
                return temp
            except Exception as e:
                print("Error fetching weather data:", e)
        else:
            print("Invalid Latitude and Longitude")
        
City = daily_weather(52.5200, 13.4050)
print(City.max_temperature())
print(City.min_temperature())
