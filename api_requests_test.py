import requests
import os
from dotenv import load_dotenv

load_dotenv()

URL_REQUEST = "http://www.omdbapi.com/?"
API_KEY = os.getenv('API_KEY')

def retrieve_movie_data_from_api(movie_title):
    # movie_title = input("Please insert the title of the movie you are looking for: ").strip()

    print(movie_title)

    URL_REQUEST_MOVIE = f"{URL_REQUEST}t={movie_title}&apikey={API_KEY}"

    print(URL_REQUEST_MOVIE)

    movie_data = requests.get(URL_REQUEST_MOVIE)
    movie_data = movie_data.json()
    print(movie_data)
    return movie_data
