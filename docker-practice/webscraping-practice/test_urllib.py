import urllib.request

url = "https://www.example.com"

response = urllib.request.urlopen(url)

print("Status:", response.status)
print(response.read()[:500])
