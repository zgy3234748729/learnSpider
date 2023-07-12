import httpx

client = httpx.Client(http2=True)
response = client.get('https://www.httpbin.org/get/', timeout=10)
print(response.text)
print(response.http_version)