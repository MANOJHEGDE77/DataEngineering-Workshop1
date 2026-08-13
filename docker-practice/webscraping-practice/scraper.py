import requests
from bs4 import BeautifulSoup

url = "https://www.example.com"

response = requests.get(url)

print("Status:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

print("\nTitle:")
print(soup.title.text)

print("\nHeadings:")
for heading in soup.find_all("h1"):
    print(heading.text)

print("\nParagraphs:")
for paragraph in soup.find_all("p"):
    print(paragraph.text)
