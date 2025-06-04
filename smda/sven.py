# supermaerkte suchen in Dresden
# overpass.api benutzen.

import requests

url= "https://overpass-api.de/api/interpreter"


cty= 'Bochum'
obj= 'supermarket'

query = f"""
[out:json];
        area["name"="{cty}"]->.searchArea;
        (
        node["shop"="{obj}"](area.searchArea);
        way["shop"="{obj}"](area.searchArea);
        relation["shop"="{obj}"](area.searchArea);
        );
        out center;
        """
# print(query)
# exit()
response = requests.post(url, query)
with (open(cty + 'json', 'w')) as f:
        f.write(response.text)        
        
#print(response.json()['elements'].head(2))
# https://swapi.co/api/people/1/