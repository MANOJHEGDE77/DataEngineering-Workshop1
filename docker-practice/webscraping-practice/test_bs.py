import requests
from bs4 import BeautifulSoup

url = "https://www.python.org/blogs/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

for heading in soup.find_all(["h1"]):
    print(heading.get_text(strip=True))
