# Beispiel eines sehr simplen scraping Tools
#
#
import requests
from typing import Self


class Scrapy:

    # Flag für "Trocken"-Layu - ohne HTTP Request
    # Achtung: Um zu crawlen bitte auf False setzen
    DRY_RUN:bool = True

    # Template einer zubenutzenden URI
    URI_TPL: str = "https://www.edeka.de/marktsuche.jsp#/?searchstring={}"

    # Liste mit Städtenamen
    cities: list = []
    
    # Letzte Reponse als Objekt
    resp:requests.models.Response
     
    tmeot:int = 180
    
    def __init__(self, dta: list = []):
        self.cities = dta

    def crawl(self):
        if len(self.cities) == 0:
            raise ValueError("Keine Daten vorhanden!")
        for item in self.cities:
            uri = self.URI_TPL.format(item)
            if self.DRY_RUN:
                print(uri)
            else:
                query = self.gen_bs_q(cty=item, obj='supermarket')
                self.resp = requests.post(uri, data={"data": query}, timeout=self.tmeot)

    def gen_bs_q(self, cty:str, obj:str) -> str:
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


# Städte im Regierungsbezirk Arnsberg
rbz_01 = [
    "Arnsberg",
    "Bochum",
    "Dortmund",
    "Ennepe-Ruhr-Kreis",
    "Hagen",
    "Hamm",
    "Herne",
    "Hochsauerlandkreis",
    "Märkischer Kreis",
    "Olpe",
    "Siegen-Wittgenstein",
    "Soest",
    "Unna",
]

scraper = Scrapy(rbz_01)

scraper.crawl()
