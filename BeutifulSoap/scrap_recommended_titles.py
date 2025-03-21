# Parašyti programą, kuri atspausdintu visas puslapio www.15min.lt "Redakcija rekomenduoja" skilties antraštes

from bs4 import BeautifulSoup
import requests

html = requests.get('https://www.15min.lt/').text
soup = BeautifulSoup(html, "html.parser")
block = soup.find('div', class_='widget-group-3043')
block_articles = block.find('div', class_='list-wrapper')
article_titles = block_articles.find_all('a', class_='title')

for each_title in article_titles:
    print(each_title.text)
