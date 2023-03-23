import requests 
from bs4 import BeautifulSoup


req=requests.get("https://www.cet.ac.in/head-of-departments/") #to visit the url

source_code = req.content #content is the source code and we are taking the source code from the page

soup= BeautifulSoup(source_code,"lxml") 
#print(soup)

figure_element= soup.find("figure", class_="wp-block-table") # finding figure tag beacuse our aiming table is inside figure tag specified by the class "wp-block-table"

table = figure_element.find("table") # finding table tag from the element figure

table_rows= table.find_all("tr") #finding 'tr' tag ( table row tag) from 'table' tag

table_rows = table_rows[1:] # we doesn't need the heading row

for row in table_rows:
    tds= row.find_all("td") #finding table data (<td>) from table row (>tr<)
    name= tds[0].text
    department= tds[1].text 
    phone= tds[2].text
    print(name)
    print(department)
    print(phone)
    print("\n")
    
    
    
