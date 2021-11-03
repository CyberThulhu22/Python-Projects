import requests
r = requests.post(url="http://hackthebox.eu/api/invite/generate")
print(r.status_code, r.reason)
print(r.text)
