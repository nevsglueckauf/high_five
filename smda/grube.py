uri = 'http://localhost:8080/foo.php?'
dta = {
    'id': 'Foo',
    'name': 'Sven',
    'Address': 'Schlumpfhausen'
}

cl = HTTPClient()

cl.get(uri=uri, dta=dta)
r= cl.lst_rsp
print([cl.lst_req ,r.headers ], sep="\n")