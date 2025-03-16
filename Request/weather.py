# Parašykite programą, kuri iš adreso https://orai.15min.lt/prognozes ištrauktų ir atspausdintų orų prognozę Vilniuje šiuo metu.

import re
import requests


def get_temperature(city):
    url = f'https://orai.15min.lt/prognoze/{city.lower()}'
    response = requests.get(url)

    if response.ok:
        html = response.text
        match = re.search(r'([+-]?\d+)°', html)

        if match:
            temperature = match.group(1)
            return f'Current temperature in {city.capitalize()} is {temperature}°'
        else:
            return "Temperature not found!"
    else:
        return "Failed to load the page"


VILNIUS = "Vilnius"
KAUNAS = "Kaunas"
KLAIPEDA = "Klaipeda"
SIAULIAI = "Siauliai"
PANEVEZYS = "Panevezys"

city_temperature = get_temperature(VILNIUS)
print(city_temperature)
