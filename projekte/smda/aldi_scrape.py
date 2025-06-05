import requests
from bs4 import BeautifulSoup

BSE_URI = 'https://filialen.aldi-sued.de/'


with open('Penny.html') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

refs = soup.find_all('h2', attrs={'class': 'market-tile'})
 
for item in refs:
    print(item.text)
    #print(type(item))