import json
import requests
from typing import Self


class LocationFinder:
    """  Lokations- / Geoinformation zu verschiedenen Themen (Objectives) finden
    
        Z.B: cty: 'Berlin' / obj: 'supermarkt' 

        Unter Benutzung der Overpass API (Aggregator verschiedener Datenquellen)
        SEE https://overpass-api.de/
    """
    # Timeout in Sekunden
    tmeot = 120
    # Letze Response als Objekt
    lst_rsp:requests.models.Response = None
    # API Base URL 
    base_url = "https://overpass-api.de/api/interpreter"
    
    # Anfrage an Overpass API senden
    def snd_req(self, cty:str, obj:str)  -> Self:
        """ Sendet POST Request (mit JSON Payload) zur API

        Args:
            cty (str): Gemeinde/ Stadt / Region/ etc.
            obj (str): objective of interest 

        Returns:
            requests.models.Response
        """
        
        query = self.gen_bs_q(cty=cty, obj=obj)
        self.lst_rsp =  requests.post(self.base_url, data={"data": query}, timeout=self.tmeot)
        return self
    
    # Query generieren
    def gen_bs_q(self, cty:str, obj:str):
        """ Generiert die Anfrage für die Basis-Suche nach :
            
            - Ort (cty)  und 
            - Sachgebiet (obj)
            
            als Overpass API/Overpass QL in der Pyload
            
            SEE https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Recurse_down_(%3E)
        """
        
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

    # Datei lesen
    def ld(self, fn:str) -> str:
        """ Datei laden 
        Args:
            fn (str): Dateiname

        Returns:
            string: Datei-Inhalt
        """
        with (open(fn, 'r')) as f:
            tmp = f.read()
        return tmp
    
    # Datei schreiben
    def sv(self, fn:str, dta:str)->Self:
        """ String-Inhalt in Datei speichern

        Args:
            fn (str): Dateiname
            dta (str): Inhalt

        Returns:
            Self: self
        """
        with(open(fn, 'w')) as f:
            f.write(dta)
        return self
    
    