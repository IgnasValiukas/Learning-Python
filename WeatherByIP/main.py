import requests
import csv

def get_location(ip_address):
    header = {"apikey": "ipb_live_jFf0sNG4R7Lqu2oqCVlsUS0GsPu32fjLd6s0sCoA"}
    url = f'https://api.ipbase.com/v2/info?apikey=ipb_live_jFf0sNG4R7Lqu2oqCVlsUS0GsPu32fjLd6s0sCoA&ip={ip_address}'
    response = requests.get(url, headers=header)
    result = response.json()
    latitude = result['data']['location']['latitude']
    longitude = result['data']['location']['longitude']
    country = result['data']['location']['country']['name']

    return latitude, longitude, country


def get_weather(given_latitude, given_longitude):
    header = {"apikey": "57d1cdd0e864865f98edf3db1fab811a"}
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={given_latitude}&lon={given_longitude}&appid=57d1cdd0e864865f98edf3db1fab811a'
    response = requests.get(url, headers=header)
    response.encoding = 'utf-8'
    result = response.json()
    city = result['name']
    weather = result['weather'][0]['main']
    temp = result['main']['temp']
    celsius = round(temp - 273.15, 1)
    return city, celsius, weather


ip_list = ['122.35.203.161', '174.217.10.111', '187.121.176.91', '176.114.85.116', '174.59.204.133', '54.209.112.174',
           '109.185.143.49', '176.114.253.216', '210.171.87.76', '24.169.250.142']

csv_filename = 'ip_data.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(['IP', 'Country', 'City', 'Temp', 'Weather'])

with open(csv_filename, 'a', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f, delimiter=';')

    for ip in ip_list:
        ip_latitude, ip_longitude, ip_country = get_location(ip)

        if ip_latitude is not None and ip_longitude is not None:
            weather_info = get_weather(ip_latitude, ip_longitude)

            if weather_info[0] is not None:
                writer.writerow([ip, ip_country, weather_info[0], weather_info[1], weather_info[2]])
                print(f'{ip}: {ip_country}, {weather_info[0]}, {weather_info[1]}°C, {weather_info[2]}')
