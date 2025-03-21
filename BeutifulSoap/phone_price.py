# Parašyti programą kuri iš puslapio https://www.telia.lt/prekes/telefonai-ir-priedai/mobilieji-telefonai/samsung
# rastų pigiausią ir brangiausią telefono modelį

import requests
from bs4 import BeautifulSoup
import re

source = requests.get('https://www.telia.lt/prekes/telefonai-ir-priedai/mobilieji-telefonai/samsung').text
soup = BeautifulSoup(source, 'html.parser')
blocks = soup.find_all('div', class_='ProductCard-styles__CardWrapper-sc-c688db1f-0 dcDfys')

phones = []
for block in blocks:
    phone_name = block.find('h2').text.strip()
    phone_price = block.find('div',
                             class_='ProductCard-styles__FullPriceBlock-sc-c688db1f-16 iCaKDW').div.span.text.strip()
    reformat_price = re.sub(r'\D', '', phone_price)
    int_price = int(reformat_price)
    phones.append((phone_name, int_price))

most_expensive = phones[0]
cheapest = phones[0]
for phone in phones:
    if phone[1] > most_expensive[1]:
        most_expensive = phone
    if phone[1] < cheapest[1]:
        cheapest = phone

print(f'Cheapest: {cheapest[0]}, {cheapest[1]}€')
print(f'Most Expensive: {most_expensive[0]}, {most_expensive[1]}€')
