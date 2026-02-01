from movie_storage_sql import add_movie, get_movies, delete_movie, update_movie, get_movies_for_website
from api_requests_test import retrieve_movie_data_from_api
from  movie_website_generator import create_website


# Test adding a movie
# add_movie("Inception", 2010, 8.8)
# add_movie("Wicked 2", 2025, 7.2)

# Test listing movies
# movies = get_movies()
# print(movies)

# Test listing movies for website and create website
movies = get_movies_for_website()
create_website(movies)


# Test updating a movie's rating
# update_movie("Inception", 9.0)
# print(get_movies())

# Test deleting a movie
# delete_movie("Inception")
# print(get_movies())  # Should be empty if it was the only movie

# Test deleting a movie
# delete_movie("Inception")
# print(get_movies())  # Should be empty if it was the only movie


# Test retrieving data from API
# retrieve_movie_data_from_api("Berlin")
