import requests
import json
from bs4 import BeautifulSoup


BSE_URI = 'https://filialen.aldi-sued.de/'


with open('Penny.html') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

#refs = soup.find_all('h2', attrs={'class': 'market-tile__title h4'})
#market-tile__main


#  <h2 class="market-tile__title h4">Penny Oelsnitz</h2>
#                       <div class="market-tile__address-distance">
#                         <div class="market-tile__address">
#                           <span class="">Willy-Brandt-Ring 17</span>
#                           <span class="">08606 Oelsnitz</span>
                          
                          
refs = soup.find_all('div', attrs={'class': 'market-tile__main'})

print(type(refs))
#exit()

def prse_addr(raw:str):
    tmp = raw.split('\n')
    print(tmp)
    
    ret = {}
    
    ret['street'] = tmp[0]
    foo = tmp[1].split(' ')
    ret['postal_code'] = foo[0]
    ret['city'] = foo[1]
    
    return ret
    
foo = []


for item in refs:
    marktname = item.find('h2', attrs={'class': 'market-tile__title h4'}).text
    adresse = item.find('div', attrs={'class': 'market-tile__address'}).text
    
    #print(marktname.strip(), adresse.strip())
    
    foo.append({'name': marktname, 'addr_raw': adresse, 'address': prse_addr(adresse.strip())})
    prse_addr(adresse.strip())
    #exit()
    
    
print(foo)

with open('Penny.json', 'w')  as f:
    json.dump(foo, f)
    
        