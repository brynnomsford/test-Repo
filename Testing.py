import requests


r = requests.get("https://hwpbc.org")
print(r.status_code)
