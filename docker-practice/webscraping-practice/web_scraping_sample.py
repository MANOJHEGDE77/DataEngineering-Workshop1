import requests
from bs4 import BeautifulSoup
import re

url = "https://www.example.com"

response = requests.get(url)

print("Status:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

# Get title
print("\nTitle:")
print(soup.title.text)

# Get all headings
print("\nHeadings:")
for heading in soup.find_all("h1"):
    print(heading.text.strip())

# Get all paragraphs
print("\nParagraphs:")
for paragraph in soup.find_all("p"):
    print(paragraph.text.strip())

# Get all links
print("\nLinks:")
for link in soup.find_all("a"):
    print(link.text.strip(), "->", link.get("href"))

# Get all numbers from webpage
text = soup.get_text()
numbers = re.findall(r"\d+", text)

print("\nNumbers found:")
print(numbers)
