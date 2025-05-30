import json
import requests


class LocationFinder:
    
    
    #exit()
    # Anfrage an Overpass API
    def snd_req(self, cty:str, what:str) -> requests.models.Response:
        
        # Aggretagor
        url = "https://overpass-api.de/api/interpreter"
        
        query = self.gen_q(cty=cty, what=what)
        return requests.post(url, data={"data": query})
    
    def gen_q(self, cty:str, what:str):
        return f"""
        [out:json];
        area["name"="{cty}"]->.searchArea;
        (
        node["shop"="{what}"](area.searchArea);
        way["shop"="{what}"](area.searchArea);
        relation["shop"="{what}"](area.searchArea);
        );
        out center;
        """

foo = LocationFinder()

dta = foo.snd_req(cty='Berlin', what='supermarket')

print(dta.text)

