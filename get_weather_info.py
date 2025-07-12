import geocoder
import httpx


def get_json_weather_data():
    g = geocoder.ip('me')
    city = g.city

    if not city:
        print("City not found!")
        return

    city = city.replace(' ', '+')
    link = httpx.get(f'https://wttr.in/{city}?format=j1')

    data = link.json()
    return data

def get_c_weather():

    data = get_json_weather_data()

    temp_c = data['current_condition'][0]['temp_C']
    return temp_c


def get_sunrise():
    data = get_json_weather_data()

    sunrise = data['weather'][0]['astronomy'][0]['sunrise']
    return sunrise


def get_sunset():
    data = get_json_weather_data()

    sunset = data['weather'][0]['astronomy'][0]['sunset']
    return sunset

def get_moonset():
    data = get_json_weather_data()

    moonset = data['weather'][0]['astronomy'][0]['moonset']
    return moonset

def get_moonrise():
    data = get_json_weather_data()

    moonrise = data['weather'][0]['astronomy'][0]['moonrise']
    return moonrise

def get_desc():
    data = get_json_weather_data()

    desc = data['weather'][0]['hourly'][2]['weatherDesc'][0]['value']
    return desc