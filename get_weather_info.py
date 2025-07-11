import geocoder

g = geocoder.ip('me')



city = g.city
city = str(city)
if ' ' in city:
    city = city.replace(' ', '+')
link = f'https://wttr.in/{city}?format=1'
link = f'https://wttr.in/{city}?format=j1'


