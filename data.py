import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.in/s?k=vivo&crid=2GRK2DQWV5RNP&sprefix=vivo%2Caps%2C225&ref=nb_sb_noss_1"
proxies = {
    "http": "http://149.48.147.64"
}

# Create lists to store the data
product_names = []
product_prices = []

response = requests.get(url, proxies=proxies)
soup = BeautifulSoup(response.text, "html.parser")

# Extract product names
for data in soup.find_all(class_="a-size-medium a-color-base a-text-normal"):
    product_names.append(data.text.strip())

# Extract product prices
for data in soup.find_all(class_="a-price-whole"):
    product_prices.append(data.text.strip())

# Print lengths to debug
print("Number of product names:", len(product_names))
print("Number of product prices:", len(product_prices))

# Ensure both lists are the same length
if len(product_names) == len(product_prices):
    # Create a DataFrame from the lists
    df = pd.DataFrame({
        "Product Name": product_names,
        "Price": product_prices
    })
else:
    print("Error: Number of product names and prices do not match.")
    df = pd.DataFrame()  # Create an empty DataFrame

# Save the DataFrame to a CSV file (optional)
df.to_csv("amazon_vivo_products.csv", index=False)

# Print the DataFrame
print(df)
