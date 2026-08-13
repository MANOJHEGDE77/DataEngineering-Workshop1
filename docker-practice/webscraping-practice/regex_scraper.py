import requests
from bs4 import BeautifulSoup
import re

url = "https://www.example.com"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

text = soup.get_text()

print("Webpage text:")
print(text)

print("\nNumbers found:")

numbers = re.findall(r"\d+", text)

print(numbers)
