import geocoder
import httpx

g = geocoder.ip('me')


city = g.city
city = str(city)
if ' ' in city:
    city = city.replace(' ', '+')
link = httpx.get(f'https://wttr.in/{city}?format=j1')
print(link.text)


