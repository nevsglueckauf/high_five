import requests
from bs4 import BeautifulSoup



BSE_URI = 'https://filialen.aldi-sued.de/'


with open('tmp/aldi.html') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

refs = soup.find_all('a', attrs={'data-ya-track': 'todirectory'})

print(type(refs))

for item in refs:
    print(BSE_URI + item['href'])
    #print(type(item))