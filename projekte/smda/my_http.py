import requests

uri = 'http://localhost:8080/?user&id=4'
#uri = 'https://api.schrodt.nrw/?user&id=33'

#uri = 'https://api.schrodt.nrw/?list'
uri = 'https://api.schrodt.nrw/?list/hsjdhjshd'
resp = requests.delete(uri)

print(resp.status_code)
print(resp.headers)

print(resp.text)

