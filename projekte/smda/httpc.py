import json
import requests
import urllib.parse
from typing import Self


class HTTPClient:
    """   Einfacher HTTP Client
    
            - GET
            - POST
            
    """
    
     # Separator URI?Query String
    QRY_SEP = "?"
    
    # Timeout in Sekunden
    timeout = 180
    
    # Letze Response als Objekt
    lst_rsp:requests.models.Response = None
    
    # letzter Request als String
    lst_req:str = ""
    
    # API Base URL 
    lst_url = ""
    
    # Anfrage per HTTP senden
    def post(self, uri:str, dta:any)  -> Self:
        """ Sendet POST Request 
        Args:
            uri (str): 
            dta (str): 

        Returns:
            self
        """
        
        self.lst_rsp =  requests.post(uri, data=dta, timeout=self.timeout)
        return self
    
    
    # Anfrage per HTTP senden
    def get(self, uri:str, dta:any=[])  -> Self:
        """ Sendet POST Request 
        Args:
            uri (str): 
            dta (str): 

        Returns:
            self
        """
        if len(dta) != 0:
            uri = self.gen_uri(uri=uri, params=dta)
            
        self.lst_req =  uri
        self.lst_rsp =  requests.post(uri, data=dta, timeout=self.timeout)
        return self
    
    # URI params --> URL encoded
    def gen_uri(self, uri:str, params: dict = {}) ->str:
        return uri + self.QRY_SEP + urllib.parse.urlencode(params)
    
  
        
    
        
        
   
    # Datei lesen
    def ld(self, fn:str) -> str:
        """ Datei laden 
        Args:
            fn (str): Dateiname

        Returns:
            string: Datei-Inhalt
        """
        with (open(fn, 'r')) as f:
            tmp = f.read()
        return tmp
    
    # Datei schreiben
    def sv(self, fn:str, dta:str)->Self:
        """ String-Inhalt in Datei speichern

        Args:
            fn (str): Dateiname
            dta (str): Inhalt

        Returns:
            Self: self
        """
        with(open(fn, 'w')) as f:
            f.write(dta)
        return self
    
    