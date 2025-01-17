import requests
from bs4 import BeautifulSoup
from word2number import w2n
import pymongo
# from currency_converter import CurrencyConverter
client = pymongo.MongoClient('mongodb://localhost:27017')
class Book_Detail():
    def get_book_details(url,soup,availability=False):
        currency_ind = '\u20B9'
        main_url = 'http://books.toscrape.com/'
        r= requests.get(url)
        soup = BeautifulSoup(r.content,'lxml')
        title_tag = soup.find_all('h3')
        price_tag =soup.find_all(class_='price_color')
        product_img_tag = soup.find_all('img')
        rating_tag = soup.find_all('p',class_='star-rating')
        instock_tag= soup.find_all('p',class_='instock availability')
        book_category_name = soup.find('div', class_="page-header action").h1.text
        for products in soup.find_all(class_='product_pod'):
            for product_title,price,product_img,rating,instock in zip(title_tag,price_tag,product_img_tag,rating_tag,instock_tag):
                for title in product_title:
                    # product_price = Book_Detail.currency_converter(price.get_text()[1:])
                    product_img_url = main_url + product_img.get('src')[11:]
                    rating_num = w2n.word_to_num(rating.get('class')[1])
                    if instock.get_text()[15:23] == "In stock":
                        availability = True
                    # print(title.get('title'))
                    # print(currency_ind+product_price)
                    # print(product_img_url)
                    # print(f"Rating {rating_num} out of 5")
                    # print(f"Instock:{availability}")
                    data= {"Name_of_book": f"{title.get('title')}",
                           # "price_of_book":f"{currency_ind + product_price}",
                           "Cover_image_url":f"{product_img_url}",
                           "Rating(out of 5)":int(f"{rating_num}"),
                           "Instock":f"{availability}"}
                    # print(data)
                    Book_Detail.insertInMongoDB(data,book_category_name)



            break

    def insertInMongoDB(document, book_category_name):
        db = client['WebScrapingDB']
        col = db[f"{book_category_name} Collection"]
        x=col.insert_one(document)
        # print(f"Data inserted with Insert_id : {x.acknowledged}")

    # def currency_converter(amount):
    #     c = CurrencyConverter()
    #     # print(c.convert(26.08,'EUR','INR'))
    #     return str(round(c.convert(amount, 'EUR', 'INR'), 3))

    def Number_of_document(book_category_name):
        db = client['WebScraping_Book_Database']
        col = db[f"{book_category_name} Collection"]
        number_of_document=f"There are {col.count_documents({})} books in {book_category_name} category"
        return number_of_document
