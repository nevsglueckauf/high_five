# In DataFrame
data = response.json()
elements = data.get("elements", [])
df = pd.DataFrame(elements)

# Optional: Als CSV speichern
df.to_csv("Meine Maerkte.csv", index=False, encoding="utf-8")
