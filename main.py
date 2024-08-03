import requests
from bs4 import BeautifulSoup
url = "https://www.flipkart.com/search?q=iphones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
proxies = {
    "http" : "http://181.10.200.154"
}
response = requests.get(url, proxies=proxies)
soup = BeautifulSoup(response.text , "html.parser")
# print(soup.find_all(class_="KzDlHZ"))
for data in soup.find_all(class_="KzDlHZ") :
    print(data.text)
for data in soup.find_all(class_="Nx9bqj _4b5DiR") :
    print(data.text)

