import requests
from bs4 import BeautifulSoup

req=requests.get("https://books.toscrape.com/")

source_code= req.content

soup= BeautifulSoup(source_code,"lxml")

articles= soup.find_all("article", class_="product_pod")

for article in articles:
    title= article.find("h3")
    a_tag = title.find("a")
    title= a_tag['title'] # to get the attribute in a tag. (full name of book)
    price=article.find("p", class_="price_color")
    price=price.text
    print("Name: {} , Price of the book: {} \n" .format(title,price))
    
    
