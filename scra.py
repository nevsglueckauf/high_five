# 
#
import requests
from typing import Self

class Scrapy:
    
    BASE_URI  = 'https://www.edeka.de/api/market-gateway?'
    
    SUBSIDIARY_PATH = 'marketId={}'
    
    CITY_Q = 'https://www.edeka.de/marktsuche.jsp#/?searchstring={}'    
    
    def __init__(self):
        self.uri = self.BASE_URI + self.SUBSIDIARY_PATH    
    
    def get_sub(self, id:int) -> Self:
        print(self.uri.format(id))
        
        


    

with open('dta/cities.txt', 'r') as file:
    a = file.readlines()

