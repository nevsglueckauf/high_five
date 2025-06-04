import requests

uri = 'http://localhost:8080/?user&id=19'


resp = requests.get(uri)

print(resp.status_code)
print(resp.headers)

print(resp.text)

