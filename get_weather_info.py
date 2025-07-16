import geocoder
import httpx
from PyQt6.QtGui import QPixmap
from io import BytesIO

class WeatherInfo:
    def __init__(self):
        self.g = None
        self.city = None
        self.link = None
        self.data = None
        self.icon = None

    def get_json_weather_data(self):
        self.g = geocoder.ip('me')
        self.city = str(self.g.city).replace(' ', '+')
    
        self.link = httpx.get(f'https://wttr.in/{self.city}?format=j1')
        self.data = self.link.json()
        weather_code = self.data['current_condition'][0].get('weatherCode')
        self.icon = f"http://cdn.weatherapi.com/weather/128x128/day/{weather_code}.png"

        return self.data, self.icon

    def get_c_weather(self):

        data = self.get_json_weather_data()

        temp_c = data['current_condition'][0]['temp_C']
        print(f'Temperature in Celsius: {temp_c}°C')
        return temp_c


    def get_sunrise(self):
        data = self.get_json_weather_data()

        sunrise = data['weather'][0]['astronomy'][0]['sunrise']
        return sunrise


    def get_sunset(self):
        data = self.get_json_weather_data()

        sunset = data['weather'][0]['astronomy'][0]['sunset']
        return sunset

    def get_moonset(self):
        data = self.get_json_weather_data()

        moonset = data['weather'][0]['astronomy'][0]['moonset']
        return moonset

    def get_moonrise(self):
        data = self.get_json_weather_data()

        moonrise = data['weather'][0]['astronomy'][0]['moonrise']
        return moonrise

    def get_desc(self):
        data = self.get_json_weather_data()

        desc = data['weather'][0]['hourly'][2]['weatherDesc'][0]['value']
        return desc

