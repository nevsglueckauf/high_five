import requests
from bs4 import BeautifulSoup
import csv
import time

headers = {
    "User-Agent": "Mozilla/5.0 (compatible; SupermarktScraper/1.0; +http://tonsite.com/contact)"
}

all_data = []
page = 1

while True:
    url = f'https://www.tiendeo.de/Filialen/hamburg/supermarkt?page={page}'
    print(f"Bearbeitung der Seite {page} ...")
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    noms = soup.find_all('p', attrs={'data-testid': 'store_item_retailer_name'})
    adresses = soup.find_all('p', attrs={'data-testid': 'store_item_address'})

    if not noms or not adresses:
        print("Kiene weitere Daten gefunden, Ende der Bearbeitung")
        break

    for nom_tag, adresse_tag in zip(noms, adresses):
        nom = nom_tag.text.strip()
        adresse = adresse_tag.text.strip()
        all_data.append({"nom": nom, "adresse": adresse})

    print(f"Seite {page} : {len(noms)} stores gefunden.")
    page += 1

    # Kurze Pause um den Server nicht zu overloaden
    time.sleep(1)

# Daten in einen CSV speichern
with open('Einkaeufsladen_hamburg.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=["nom", "adresse"])
    writer.writeheader()
    for row in all_data:
        writer.writerow(row)

print(f"Bearbeitung beendet. Gesamte uebernommene Einkaeufsladen : {len(all_data)}")