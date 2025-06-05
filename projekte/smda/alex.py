# supermaerkte suchen in Dresden
# overpass.api benutzen.

import requests

url= "https://overpass-api.de/api/interpreter"


cty= 'Moers'
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
with (open('dresd.json', 'w')) as f:
        f.write(response.text)        
        
#print(response.json()['elements'].head(2))


<a href="nrw/bochum">Bochum</a>