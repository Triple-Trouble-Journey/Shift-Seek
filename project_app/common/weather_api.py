import requests

WEATHER_API_KEY =  "8e6511af6c4b4c708db214451241402"
WEATHER_API_URL = "http://api.weatherapi.com/v1/current.json"

def get_city_weather(city):

    params = {
        'key': WEATHER_API_KEY,
        'q': city
    }

    response = requests.get(WEATHER_API_URL, params=params)
    data = response.json()

    city = data['location']['name']
    country = data['location']['country']
    region = data['location']['region']
    temperature = data['current']['temp_c']
    weather_description = data['current']['condition']['text']

    return {"location": f'{city} | {country}',
            "region": region,
            "temperature": temperature, 
            "weather_description": weather_description}
