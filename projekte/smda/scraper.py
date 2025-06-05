import requests
import json
from bs4 import BeautifulSoup


class Scraper:
    """Scraping HTTP resources
    -
    """

    BSE_URI_ALDI = "https://filialen.aldi-sued.de/"

    LST_NRW_ALSI = "https://filialen.aldi-sued.de/nordrhein-westfalen"

    def prc_req(uri: str, mtd: str = "GET", dta: dict = {}, hds: dict = {}):
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

        match mtd:
            case "GET":
                return requests.get(uri=uri, data=dta, headers=hds)
            case "PUT":
                return requests.put(uri=uri, data=dta, headers=hds)
            case "POST":
                return requests.post(uri=uri, data=dta, headers=hds)
            case _:
                raise ValueError("Unbekannte Methode")

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
            # d=dta[i]
            # h=hds[i]
            # rts.append(self.prc_req(uri,mtd, d, h))
            print(uri + ' :: '+str(i))

        return rts


s = Scraper()
s.walk(
    [
        "https://filialen.aldi-sued.de/",
        "https://filialen.aldi-sued.de/nordrhein-westfalen",
        "https://foo.example.org/bar",
    ]
)
