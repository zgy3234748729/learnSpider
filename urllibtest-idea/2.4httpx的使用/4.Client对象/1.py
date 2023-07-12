import httpx

with httpx.Client() as client:
    response = client.get('https://www.httpbin.org/get', timeout=5)
    print(response)