from parse import Parser as Parser
from scraper import Scraper as Scraper
from mem_disk_usage import Mem as Mem
import sys


df = Mem()

rto = 459 / 551884.80

print(rto)
exit()
#print("hdush")
print(df.get_file_size_readable("./payload_penny.txt"))

pl = [
    ["Willy-Brandt-Ring 17", "08606 Oelsnitz"],
    ["Pforzheimer Str. 55", "71665 Vaihingen-Horrheim"],
    ["Hochfelder Landstraße 23", "24943 Flensburg"],
    ["Bahnhofstr. 32", "79400 Kandern"],
    ["Am Mühlbach 1", "61209 Echzell"],
    ["Molkenbornstr. 2-4", "63743 Aschaffenburg"],
    ["Schleissheimer Str.  267", "80809 München"],
    ["Ruppiner Chaussee 243", "13503 Berlin"],
    ["Frankenhäuser Str. 23", "06537 Kelbra"],
    ["Wismarsche Straße 152", "23936 Grevesmühlen"],
]

print(sys.getsizeof(pl))


exit()
scraper = Scraper()
parser = Parser()
dta = scraper.prc_req(uri=Scraper.BSE_URI_PENNY)  # 'https://www.penny.de/marktsuche/'
result = parser.prs_penny(dta.text)
