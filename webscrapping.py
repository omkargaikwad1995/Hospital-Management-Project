
from bs4 import BeautifulSoup
import requests

def get_imd_movies(url):
    page = requests.get(url) # get the entire webpage
    soup = BeautifulSoup(page.text, "html.parser") # Converts to html
    movies = soup.find_all("td",class_="titleCloumn") # from imdb.com
    return movies
def get_imd_movie_info(movie): # seprate title and year td tag
    movie_title= movie.a.contents[0]
    movie_year=  movie.span.contents[0]
    return movie_title, movie_year

ctrl=0
print("------------------")
m=get_imd_movies("https://www.imdb.com/chart/top/")
for movies in m:
    movie_title, movie_year= get_imd_movie_info(movies)
    print(movie_title, movie_year)
    print("--------------")
    ctr=ctr+1
    if (ctr==5):
        break;