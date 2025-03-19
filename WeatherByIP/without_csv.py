import requests
import csv

def get_location(ip_address):
    header = {"apikey": "API KEY"}
    url = f'https://api.ipbase.com/v2/info?apikey={API KEY}&ip={ip_address}'
    response = requests.get(url, headers=header)
    result = response.json()
    latitude = result['data']['location']['latitude']
    longitude = result['data']['location']['longitude']
    country = result['data']['location']['country']['name']

    return latitude, longitude, country


def get_weather(given_latitude, given_longitude):
    header = {"apikey": "API KEY"}
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={given_latitude}&lon={given_longitude}&appid={API KEY}'
    response = requests.get(url, headers=header)
    response.encoding = 'utf-8'
    result = response.json()
    city = result['name']
    weather = result['weather'][0]['main']
    temp = result['main']['temp']
    celsius = round(temp - 273.15, 1)
    return city, celsius, weather


ip_list = ['78.62.230.137', '122.35.203.161', '174.217.10.111', '187.121.176.91', '174.59.204.133', '54.209.112.174',
           '109.185.143.49', '176.114.253.216', '210.171.87.76', '24.169.250.142']
for ip in ip_list:
    ip_latitude, ip_longitude, ip_country = get_location(ip)
    weather_info = get_weather(ip_latitude, ip_longitude)
    print(f'{ip}: {ip_country}, {weather_info[0]}, {weather_info[1]}, {weather_info[2]}')
