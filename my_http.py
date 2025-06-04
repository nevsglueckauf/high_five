import requests

uri = 'http://localhost:8080/?user&id=19'
uri = 'https://api.schrodt.nrw/?user&id=33'

uri = 'https://api.schrodt.nrw/?list'

resp = requests.get(uri)

#print(resp.status_code)
print(resp.headers)

print(resp.text)

