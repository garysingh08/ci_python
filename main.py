import pandas as pd
import requests as r
url = "https://tstranchers.pythonanywhere.com/getData"

resp = r.get(url, params={"stock": "META"})
df=pd.read_json(resp.text)
df.to_csv("data.csv", index=False)
