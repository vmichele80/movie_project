import requests
import os
from dotenv import load_dotenv

load_dotenv()

URL_REQUEST = "http://www.omdbapi.com/?"
API_KEY = os.getenv('API_KEY')

def retrieve_movie_data_from_api(movie_title):
    """This function collect the movie data via the api call and
    returns it to the main add movie function for further
    processing"""

    URL_REQUEST_MOVIE = f"{URL_REQUEST}t={movie_title}&apikey={API_KEY}"

    # Debugging
    # print(URL_REQUEST_MOVIE)

    movie_data = requests.get(URL_REQUEST_MOVIE)
    movie_data = movie_data.json()

    # Debugging
    # print(movie_data)
    return movie_data
