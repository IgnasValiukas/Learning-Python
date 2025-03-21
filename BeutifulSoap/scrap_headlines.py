# Parašyti programą, kuri suskaičiuotų kiek šios dienos www.delfi.lt puslapyje yra antraštinių straipsnių

from bs4 import BeautifulSoup
import requests

html = requests.get('https://www.delfi.lt/').text
soup = BeautifulSoup(html, "html.parser")
headline_elements = soup.select("div[class*='headline__title']")

print(f"Total headlines: {len(headline_elements)}")

print(type(headline_elements))
# class="block-type-102-headline__title"
# class="block-type-104-headline__title"
# class="block-type-18-headline__title"
# class="block-type-2-headline__title"
