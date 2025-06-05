import pandas as pd
import json

with open('dresd.json', 'r') as f:
    data = f.read()
    
foo = pd.DataFrame(json.loads(data)['elements'])   
print(foo)
