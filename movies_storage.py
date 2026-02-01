import json
import os

MOVIES_FILE = "data.json"


def get_movies():
    """
    Loads movies from a JSON file and returns them
    as a dictionary of dictionaries.
    """
    if not os.path.exists(MOVIES_FILE):
        return {}

    with open(MOVIES_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_movies(movies):
    """
    Gets all your movies as an argument and saves them to the JSON file.
    """
    with open(MOVIES_FILE, "w", encoding="utf-8") as file:
        json.dump(movies, file, indent=4)


def add_movie(title, year, rating):
    """
    Adds a movie to the movies database.
    Loads the information from the JSON file, adds the movie,
    and saves it.
    """
    movies = get_movies()

    movies[title] = {
        "rating": rating,
        "year": year
    }

    save_movies(movies)


def delete_movie(title):
    """
    Deletes a movie from the movies database.
    Loads the information from the JSON file, deletes the movie,
    and saves it.
    """
    movies = get_movies()

    if title in movies:
        del movies[title]

    save_movies(movies)


def update_movie(title, rating):
    """
    Updates a movie from the movies database.
    Loads the information from the JSON file, updates the movie,
    and saves it.
    """
    movies = get_movies()

    if title in movies:
        movies[title]["rating"] = rating

    save_movies(movies)