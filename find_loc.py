import json
import requests


class LocationFinder:
    """  Finding location related data to different objectives 
    
        E.G: loc: 'Berlin' / objective: 'supermarkt' 

    Returns:
        _type_: _description_
    """
    
    tmeot = 120
    
    
    # Anfrage an Overpass API
    def snd_req(self, cty:str, obj:str) -> requests.models.Response:
        """ Sending request to external API

        Args:
            cty (str): Village/City/Region/ etc.
            obj (str): objective of interest 

        Returns:
            requests.models.Response: 
        """
        # Aggretagor
        url = "https://overpass-api.de/api/interpreter"
        
        query = self.gen_q(cty=cty, obj=obj)
        return requests.post(url, data={"data": query}, timeout=self.tmeot)
    
    def gen_q(self, cty:str, obj:str):
        return f"""
        [out:json];
        area["name"="{cty}"]->.searchArea;
        (
        node["shop"="{obj}"](area.searchArea);
        way["shop"="{obj}"](area.searchArea);
        relation["shop"="{obj}"](area.searchArea);
        );
        out center;
        """

foo = LocationFinder()

dta = foo.snd_req(cty='Moers', obj='supermarket')

print(dta.text)

