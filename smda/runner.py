# Beispiel eines sehr simplen generischen scraping Tools
#
#
import requests
from typing import Self


class Runner:

    # Flag für "Trocken"-Lauf - ohne HTTP Requests
    # Achtung: Um zu crawlen bitte auf False setzen
    dry_run:bool = True

    # Flag für "Auto-Save"
    # 
    ato_sav:bool = True

    # Prefix für Dateinamen
    fn_pfx = 'RESP_'
    
    # Template einer zubenutzenden URI
    
    # Request Timeout  
    timeout:int = 180
    
    # HTTP Client Objekt
    client = None    
    
    # URI Template
    uri_tpl:str = ""
    
    # Liste mit URIs
    uris = []
    
    # Liste mit dynamischen Paramtetern
    dyn_par = []
    
     # Letzte Reponse als Objekt
    resp:requests.models.Response
    
    def __init__(self, uri:str, par: list = [], client=None):
        self.dyn_par = par
        self.uri_tpl = uri
        self.client = client
        

    def crawl(self):
        if len(self.dyn_par) == 0:
            raise ValueError("Keine Daten vorhanden!")
        for idx, par in enumerate(self.dyn_par):
            self.uris.append(self.uri_tpl.format(par))
            if self.dry_run:
                print(self.dyn_par[idx], self.uris[idx])
            else:
                self.resp = self.snd_req(self.dyn_par[idx], self.uris[idx])
                
    def snd_req(self, par:str, uri:str):
        self.resp = self.client.get(uri=uri)
        if(self.ato_sav):
            fn = self.fn_pfx + par + '.json'
            self.client.sv(fn=fn, dta=self.resp.text)
            # GET, POST OR whatever
        
 

   

