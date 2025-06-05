# Query collection

class Query:
    
    loc_sm = """
        [out:json];
        area["name"="{}"]->.searchArea;
        (
        node["shop"="{}"](area.searchArea);
        way["shop"="{}"](area.searchArea);
        relation["shop"="{}"](area.searchArea);
        );
        out center;
        """
    


    def __init__(self):
        pass
    
    def q_sm_cty(self, cty:str, obj:str='supermarket'):
        
        return self.loc_sm.format(cty, obj, obj, obj)
    
    