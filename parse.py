import json

with open('edeka.raw', 'r') as file:
    a = file.readlines()

for row in a:
    txt = row.split(' ').strip()
    print(txt)