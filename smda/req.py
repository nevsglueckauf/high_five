import requests

# resp = requests.get(url='http://localhost:8080/?is=999')


dta= {
    'name': 'Sven',
    'ID': 'hfugduf',
    'DEL_FOO': 'Forbidden'
}
resp = requests.get(url='http://localhost:8080/', data=dta)

print(resp.text)
print(resp.headers)
