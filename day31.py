import requests
from lxml import html

#user_input = input("Enter the URL : ")
response = requests.get("https://www.autotrader.co.uk/car-search?sort=relevance&postcode=e113ld&radius=1500&include-delivery-option=on")


#response = requests.get('http://' +user_input, allowredirects = False)


print(response.text)