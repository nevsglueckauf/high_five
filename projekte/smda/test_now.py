from smda.httpc import HTTPClient
from smda.runner import Runner



uri_tpl = "https://www.edeka.de/marktsuche.jsp#/?searchstring={}"

# Städte im Regierungsbezirk Arnsberg
rbz_01 = [
    "Arnsberg",
    "Bochum",
    "Dortmund",
    "Ennepe-Ruhr-Kreis",
    "Hagen",
    "Hamm",
    "Herne",
    "Hochsauerlandkreis",
    "Märkischer Kreis",
    "Olpe",
    "Siegen-Wittgenstein",
    "Soest",
    "Unna",
]


rbz_02 = [
    "Bochum",
    "Hamm",
    "Soest",
]

runner = Runner(uri=uri_tpl, par=rbz_01, client=HTTPClient())
runner.dry_run = False
runner.crawl()



# for i in runner.uris:
#     print(i)

