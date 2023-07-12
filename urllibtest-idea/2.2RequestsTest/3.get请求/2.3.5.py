import requests

r = requests.get('https://scrape.center/favicon.ico')
print(r.text)
print(r.content)