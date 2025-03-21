from bs4 import BeautifulSoup
import requests

html = requests.get('https://www.delfi.lt/').text
soup = BeautifulSoup(html, "html.parser")

headline_classes = [
    "block-type-102-headline__title",
    "block-type-104-headline__title",
    "block-type-18-headline__title",
    "block-type-2-headline__title"
]

headlines = []
for class_name in headline_classes:
    headline_list = soup.find_all('div', class_=class_name)
    for headline in headline_list:
        headlines.append(headline.text.strip())

print(f'Total headlines: {len(headlines)}')