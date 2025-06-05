import requests

resp = requests.head('https://www.schrodt.nrw')

print(resp.text)
print('\n'.join(resp.headers))
