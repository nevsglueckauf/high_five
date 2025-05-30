import requests
import pandas as pd

# Overpass API Query – suche nach "supermarket" in Bad Bramstedt
city = 'Moers'
query = f"""
[out:json];
area["name"="{city}"]->.searchArea;
(
  node["shop"="supermarket"](area.searchArea);
  way["shop"="supermarket"](area.searchArea);
  relation["shop"="supermarket"](area.searchArea);
);
out center;
"""

print(query)
#exit()
# Anfrage an Overpass API
url = "https://overpass-api.de/api/interpreter"
response = requests.post(url, data={"data": query})
data = response.json()
with open('superm.json', 'w') as f:
  f.write(response.text)

#print(response.text)


# Ergebnisse verarbeiten
results = []
for element in data["elements"]:
    tags = element.get("tags", {})
    results.append({
        "Name": tags.get("name"),
        "Kette": tags.get("brand"),
        "Straße": tags.get("addr:street"),
        "Hausnummer": tags.get("addr:housenumber"),
        "Postleitzahl": tags.get("addr:postcode"),
        "Stadt": tags.get("addr:city", "Moers"),
        "Lat": element.get("lat") or element.get("center", {}).get("lat"),
        "Lon": element.get("lon") or element.get("center", {}).get("lon")
    })

# In DataFrame
df = pd.DataFrame(results)

# Optional: als JSON speichern
df.to_json(f"{city}.json", orient="records", indent=2, force_ascii=False)

# Als Vorschau anzeigen
print(df.head())

# Optional: Als CSV speichern
#df.to_csv("supermaerkte_bad_bramstedt.csv", index=False, encoding="utf-8")