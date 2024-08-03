from bs4 import BeautifulSoup

with open("main.html", "r") as f: 
    html_doc = f.read()

soup = BeautifulSoup(html_doc, "html.parser")
print(soup.title.name)