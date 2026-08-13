from bs4 import BeautifulSoup

html = """
<html>
    <body>
        <h1 class="title">Web Scraping</h1>

        <a href="https://example.com">Example Website</a>

        <a href="https://google.com">Google</a>
    </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

# Find first link
link = soup.find("a")

print("Text:", link.text)
print("URL:", link.get("href"))

# Find all links
links = soup.find_all("a")

for link in links:
    print(link.text, "->", link.get("href"))
