import requests
from bs4 import BeautifulSoup
from Get_Book_Details import Book_Detail as bd
from Export_Database_class import Export_Database as edb
dict ={}
main_url = "http://books.toscrape.com/"
r= requests.get(main_url)
soup = BeautifulSoup(r.content,'lxml')
unorder_list_tag = soup.find('ul',class_="nav nav-list").li.ul.find_all('li')
export_output_path="D:/Learnig React/myapp/src/BooksCollection"

for next_page in unorder_list_tag:
    data ={next_page.a.text.strip():main_url+next_page.a.get('href')}
    # print(data)
    dict.update(data)
# print(dict.keys())
def next_page(url,current_page,total_page):
    url_ = url.removesuffix('index.html')
    for page in range(current_page+1,total_page+1):
        # book_category_name = soup.find('div',class_="page-header action").h1.text
        next_page_tag = f"page-{page}.html"
        next_url = url_ + next_page_tag
        w = requests.get(next_url)
        next_soup = BeautifulSoup(w.content, 'lxml')
        # print(f"page_number {page} of {book_category_name} category")
        # print(next_url)
        # print(book_category_name)
        bd.get_book_details(next_url,soup=next_soup)
def get_next_page(book_category_name,url):
    r = requests.get(url)
    next_page_present=""
    soup = BeautifulSoup(r.content, 'lxml')
    # print(book_category_name)
    try:
        total_page = int(soup.find('ul', class_='pager').find('li', class_='current').text.strip().split(' ')[-1])
        current_page = int(soup.find('ul', class_='pager').find('li', class_='current').text.strip().split(' ')[1])
    except Exception as e:
        next_page_present = e.__str__().split(" ")[0]
    if next_page_present=="'NoneType'":
        bd.get_book_details(url, soup=soup)
    else:
        bd.get_book_details(url, soup=soup)
        next_page(url,current_page,total_page)
    # print(url)
file = open('log.txt','w')
for key in dict:
    book_category_name=key
    book_category_url=dict[key]
    print(f"Scraping data for {book_category_name} book category")
    get_next_page(book_category_name,book_category_url)
    number_of_document = bd.Number_of_document(book_category_name)
    # print(number_of_document)
    print(f"Scraping is completed for {book_category_name} book category")
    file.write(number_of_document)
file.close()
input =("Do you want to export the database in json file format: ")
if input.lower()=='y' or "yes":
    edb.Export_database('WebScraping_Book_Database',export_output_path)
else:
    print("program end")
    exit()