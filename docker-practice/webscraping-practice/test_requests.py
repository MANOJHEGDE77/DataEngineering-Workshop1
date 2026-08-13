import requests

url = "https://www.example.com"

response = requests.get(url)

print("Status:", response.status_code)
print("Content type:", response.headers.get("content-type"))
print(response.text[:500])
