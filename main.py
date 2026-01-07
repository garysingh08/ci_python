import requests as r

resp = r.get("https://www.accountplusfinance.com/projects/user-agents/headers.php", headers={"User-Agent": "Testing-Git_Hub"})

if resp.status_code == 200:
  print(resp.text)

else:
  print("error")
