import requests
from requests.auth import HTTPBasicAuth

r = requests.get('https://ssr3.scrape.center/', auth=('admin', 'admin'), timeout=5)
print(r.status_code)
