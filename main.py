import pandas as pd
import requests as r
url = ""

resp = r.get(url, params={"stock": ""})
df=pd.read_json(resp.text)
df.to_csv("data.csv", index=False)
