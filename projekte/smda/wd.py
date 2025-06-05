import requests

#
# 'application/json, text/json'
uri = 'https://www.wikidata.org/wiki/Q16968817'
uri = 'https://query.wikidata.org/sparql?query=%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+wd%3A+%3Chttp%3A%2F%2Fwww.wikidata.org%2Fentity%2F%3E%0APREFIX+wdt%3A+%3Chttp%3A%2F%2Fwww.wikidata.org%2Fprop%2Fdirect%2F%3E%0ASELECT+DISTINCT+%3Fname+%3Firi+WHERE+%7B%0A%3Firi+wdt%3AP106+wd%3AQ188784.%0A%3Firi+wdt%3AP1080+wd%3AQ931597.%0A%3Firi+rdfs%3Alabel+%3Fname.%0AFILTER%28lang%28%3Fname%29%3D%22en%22%29%0A%7D%0AORDER+BY+ASC%28%3Fname%29%0A'




headers={'Accept': 'application/sparql-results+json',  'Content-Type': 'application/sparql-query'}

resp = requests.get(uri, headers=headers)

print(resp.text)