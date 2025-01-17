import requests
from bs4 import BeautifulSoup
import pymongo
from currency_converter import CurrencyConverter
from word2number import w2n
#Variable defination section:
currency_ind ='\u20B9'
main_url ='http://books.toscrape.com/'
url ="http://books.toscrape.com/catalogue/category/books/travel_2/index.html"
availability= False
r= requests.get(url)
soup = BeautifulSoup(r.content,'lxml')
# print(soup.prettify())
client =pymongo.MongoClient('mongodb://localhost:27017')
# print(client)
#pymongoDB
def insertInMongoDB(dictionary):
    db = client['Web_scraping_database']
    col = db['Travel_book_collection']
    col.insert_one(dictionary)
#currency function
def currency_converter(amount):
    c= CurrencyConverter()
    # print(c.convert(26.08,'EUR','INR'))
    return str(round(c.convert(amount,'EUR','INR'),3))
#Extrack the tags
title_tag = soup.find_all('h3')
price_tag =soup.find_all(class_='price_color')
product_img_tag = soup.find_all('img')
rating_tag = soup.find_all('p',class_='star-rating')
instock_tag= soup.find_all('p',class_='instock availability')
#main Function
for products in soup.find_all(class_='product_pod'):
    for product_title,price,product_img,rating,instock in zip(title_tag,price_tag,product_img_tag,rating_tag,instock_tag):
        for title in product_title:
            titles = soup.find_all('a')
            product_price=currency_converter(price.get_text()[1:])
            product_img_url=main_url + product_img.get('src')[11:]
            rating_num = w2n.word_to_num(rating.get('class')[1])
            if instock.get_text()[15:23]=="In stock":
                availability = True
            # print(title.get('title'))
            # print(currency_ind+product_price)
            # print(product_img_url)
            # print(f"Rating {rating_num} out of 5")
            # print(f"Instock:{availability}")
            data= {"Name_of_book": f"{title.get('title')}",
                   "price_of_book":f"{currency_ind + product_price}",
                   "Cover_image_url":f"{product_img_url}",
                   "Rating(out of 5)":int(f"{rating_num}"),
                   "Instock":f"{availability}"}
            insertInMongoDB(data)
            print("data inserted in MongoDB")

    break
client.close()
