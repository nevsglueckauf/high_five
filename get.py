import requests


uri = 'http://localhost:8080/foo.php?id=Foo&name=Sven&Address=Schlumpfhausen'


resp = requests.get(uri)

print(resp.headers)
