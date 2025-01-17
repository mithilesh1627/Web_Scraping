import imdb
import requests
from bs4 import BeautifulSoup
import pymongo
client =pymongo.MongoClient('mongodb://localhost:27017')
url=imdb.imdbURL_top250
r =requests.get(url)
soup = BeautifulSoup(r.content,'lxml')
# print(url)
def insertInMongoDB(dictionary):
    db = client['Web_scraping_database']
    col = db['Top250Movies']
    col.insert_one(dictionary)

#Finding all the tags
Movie_details_cloumn=soup.find('tbody',class_="lister-list")
Movie_details_tag = Movie_details_cloumn.find_all('td',class_="titleColumn")
Movie_poster_tag = Movie_details_cloumn.find_all('td',class_="posterColumn")
Movie_rating_tag = Movie_details_cloumn.find_all('td',class_="ratingColumn imdbRating")



for movie_detail,movie_poster,movie_rating in zip(Movie_details_tag,Movie_poster_tag,Movie_rating_tag):
    rank = movie_detail.text.strip().split('\n')[0].strip('.')
    name = movie_detail.text.strip().split('\n')[1].strip()
    year = movie_detail.text.strip().split('\n')[2].strip('()')
    poster = movie_poster.a.img.get('src')
    rating = movie_rating.strong.text
    data ={"Movie Name":f"{name}","Movie Rank":f"{rank}","Release Year":f"{year}"
           ,"Movie poster":f"{poster}","Movie_IMDB_rating":f"{rating}"}
    print(data)
    insertInMongoDB(data)

