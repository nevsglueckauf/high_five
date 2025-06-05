from parse import Parser as Parser
from scraper import Scraper as Scraper

scraper = Scraper()
parser = Parser()
dta = scraper.prc_req(uri='https://www.penny.de/marktsuche/')
result = parser.prs_penny(dta.text)


