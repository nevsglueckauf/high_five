
uri = 'https://www.edeka.de/marktsuche.jsp#/?searchstring={}'

with open('city_h.txt', 'r') as file:
    a = file.readlines()

for city in a:
    cur_uri = uri.format(city.strip())
    print(cur_uri)
