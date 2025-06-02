import json
import requests
import pandas as pd


base_url = "https://overpass-api.de/api/interpreter"

cty = 'Moers'
obj = 'supermarket'
to = 120

# jaalidnwtl* - SEE https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL
query =  f"""
        [out:json];
        area["name"="{cty}"]->.searchArea;
        (
        node["shop"="{obj}"](area.searchArea);
        way["shop"="{obj}"](area.searchArea);
        relation["shop"="{obj}"](area.searchArea);
        );
        out center;
        """

response =  requests.post(base_url, data={"data": query}, timeout=to)

dta = json.loads(response.text)["elements"]
with (open('resp_Moers_20250602.json', 'w')) as f:
        f.write(response.text)


df = pd.DataFrame(data=dta)

print(dta.head())




#* Just another annoying language  I do not want to learn 