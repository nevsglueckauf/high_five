# Python source Code

## Anwendungsbeispiel
```python
from parse import Parser as Parser              
from scraper import Scraper as Scraper

scraper = Scraper()
parser = Parser()
dta = scraper.prc_req('https://www.penny.de/marktsuche/')
result = parser.prs_penny(dta)
```

```zsh
# Ausgabe:
['Willy-Brandt-Ring 17', '08606 Oelsnitz']
['Pforzheimer Str. 55', '71665 Vaihingen-Horrheim']
['Hochfelder Landstraße 23', '24943 Flensburg']
['Bahnhofstr. 32', '79400 Kandern']
['Am Mühlbach 1', '61209 Echzell']
['Molkenbornstr. 2-4', '63743 Aschaffenburg']
['Schleissheimer Str.  267', '80809 München']
['Ruppiner Chaussee 243', '13503 Berlin']
['Frankenhäuser Str. 23', '06537 Kelbra']
['Wismarsche Straße 152', '23936 Grevesmühlen']
```



```python



import requests
import json
from bs4 import BeautifulSoup


class Scraper:
    """Scraping HTTP resources
    -
    """

    BSE_URI_ALDI = "https://filialen.aldi-sued.de/"

    LST_NRW_ALDI = "https://filialen.aldi-sued.de/nordrhein-westfalen"
    
    BSE_URI_PENNY = "https://www.penny.de/marktsuche/"


    def prc_req(uri: str, mtd:str = "GET", dta: dict = {}, hds: dict = {}):
        """Prozessiert HTTP Request

        Args:
            uri (str): Endpoint
            mtd (str, optional): _description_. Defaults to 'GET'.
            dta (dict, optional): _description_. Defaults to {}.
            hds (dict, optional): _description_. Defaults to {}.

        Raises:
            ValueError: _description_

        Returns:
            _type_: _description_
        """
        print(mtd)
        exit()
        match mtd:
            case "GET":
                res = requests.get(uri=uri, data=dta, headers=hds)
            case "PUT":
                res = requests.put(uri=uri, data=dta, headers=hds)
            case "POST":
                res = requests.post(uri=uri, data=dta, headers=hds)
            case _:
                raise ValueError("Unbekannte Methode")
        
        return res

    def prc_sts_cde(cde: int):

        match cde:
            case 200:
                print("OK")
            case 400 | 403 | 404:
                print("Client Error")
            case 500:
                print("Server Error")
            case _:
                print("Unknown error")

    def walk(
        self, uris: list = [], mtd: str = "GET", dta: dict = {}, hds: dict = {}
    ) -> list:
        one_hd = False
        one_dta = False
        rts = []  # Ergibnisliste mit Responses

        if len(hds) == 1:
            one_hd = True
        if len(dta) == 1:
            one_dta = True
        i = 0
        for i, uri in enumerate(uris):
            d=dta[i]
            h=hds[i]
            rts.append(self.prc_req(uri,mtd, d, h))
            #print(uri + ' :: '+str(i))

        return rts
```

```python

from bs4 import BeautifulSoup


class Parser:
    """ Parsen der HTTTP Response nach Marktarkt:
    
    - Penny
    - Aldi

    """

    tag_soup = None

    def __init__(self):
        pass

    def prs_penny(self, html_resp: str) -> list:
        self.tag_soup = soup = BeautifulSoup(html_resp, "html.parser")
        # Umgebenden Container selektieren
        refs = soup.find_all("div", attrs={"class": "market-tile__main"})
        tmp = []

        # Children mit Name und Adresse sammeln
        for item in refs:
            marktname = item.find("h2", attrs={"class": "market-tile__title h4"}).text
            adresse = item.find("div", attrs={"class": "market-tile__address"}).text
            tmp.append(
                {
                    "name": marktname,
                    "addr_raw": adresse,
                    "address": self.prse_penny_addr(adresse.strip()),
                }
            )

        return tmp

    def prs_penny_addr(raw: str) -> str:
        tmp = raw.split("\n")
        print(tmp)

        ret = {}

        ret["street"] = tmp[0]
        foo = tmp[1].split(" ")
        ret["postal_code"] = foo[0]
        ret["city"] = foo[1]

        return ret

```

