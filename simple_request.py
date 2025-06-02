import json
import requests



base_url = "https://overpass-api.de/api/interpreter"

cty = 'Hamburg'
obj = 'supermarket'
to = 120




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

print(response.text)