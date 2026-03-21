import requests


def get_weather(city):
    reponse = requests.get(f"https://api.weater.com/v1/{city}")
    if reponse.status_code == 200:
        return response.json
    else:
        raise ValueError("Could not fetch weather data")
