import httpx

client = httpx.Client()
try:
    response = httpx.get('https://www.httpbin.org/get')
finally:
    client.close()
print(response)