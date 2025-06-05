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
                    "address": self.prs_penny_addr(adresse.strip()),
                }
            )

        return tmp

    def prs_penny_addr(self, raw: str) -> str:
        tmp = raw.split("\n")
        print(tmp)

        ret = {}

        ret["street"] = tmp[0]
        foo = tmp[1].split(" ")
        ret["postal_code"] = foo[0]
        ret["city"] = foo[1]

        return ret
