import json
import requests
import pandas as pd

with (open('resp_Moers_20250602.json', 'r')) as f:
        dta = f.read()
        
df = pd.DataFrame(json.loads(dta)['elements'])
foo = df.iloc[0]['tags']


print(foo)

