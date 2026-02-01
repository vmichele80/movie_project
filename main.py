import random
import sys

import movie_storage_sql as storage
from api_requests import retrieve_movie_data_from_api
from movies_menu import MENU
from  movie_website_generator import create_website


def show_menu():
    """
    Show the user menu saved in a separate file
    """
    print(MENU)
    user_choice = input("Enter choice (0-8): ")
    return user_choice


def show_list_of_movies(movies):
    """
    Print all the movies, along with their rating.
    In addition, the command prints how many movies there are in total in the database.
    """
    if len(movies) == 0:
        print("There are no movies in the database.")
    else:
        print(f"{len(movies)} movies in total.")
        for movie in movies:
            rating = movies[movie]["rating"]
            year = movies[movie]["year"]
            print(f"{movie} - Rating: {rating}, Year of Release: {year}")


def add_movie():
    """
    Ask the user to enter a movie name,
    we check if the movie not already in our db.
    If yest we retrieve data via the API and handle it over
    the data entry function in movie_storage_sql.py
    The data retrieved with the api is a list dictionary
    We will be using a dictionary of dictionaries where the the move title is the main key.
    (assume that the rating is a number between 1-10).
    """
    movies = storage.get_movies()
    movie_title = input("Enter movie name: ")
    if not movie_title.strip():
        print("Movie title cannot be empty.")
        return

    try:
        # we store the data retrieved from the api in a variable (dictionary)
        movie_data = retrieve_movie_data_from_api(movie_title)

        # note that the api might retrieve a different title e.g. 2 gives Terminator 2 as title
        if movie_data['Title'] not in movies:
                if movie_data['Response'] == 'True':
                    movie_title = movie_data['Title']
                    # handles the case the movie rating is not available
                    if movie_data['imdbRating'] == 'N/A':
                        movie_rating = float(input("There is not rating for this movie. Give a rating: "))
                    else:
                        movie_rating = movie_data['imdbRating']

                    movie_year = movie_data['Year']
                    movie_poster_url = movie_data['Poster']
                    storage.add_movie(movie_title, movie_year, movie_rating, movie_poster_url)
                else:
                    print("This movie was not found in the Open Movie Database")

        else:
            print(f"Movie {movie_data['Title']} is already in database. To update use the update option from the Menu")

    # if internet connectivity fails we show a message.
    # We do not expose the error why it would reveal the api key
    except Exception:
        print(f"Connection to the API was not possible. "
              f"\nCheck your Internet connection and try again later")



def delete_movie():
    """
    Ask the user to enter a movie name, and delete it.
    It calls the external function for persistent storage.
    If the movie doesn’t exist in the database, print an error message,
    and then print the menu again as always.
    """
    movies = storage.get_movies()
    movie_to_delete = input("Enter movie to delete: ")
    if movie_to_delete in movies:
        storage.delete_movie(movie_to_delete)
        print(f"The movie {movie_to_delete} has been deleted.")
    else:
        print("Movie not found")


def update_movie():
    """
    Ask the user to enter a movie name, and then check if it exist.
    If the movie doesn’t exist prints an error message.
    If it exist, ask the user to enter a new rating,
    and update the movie’s rating in the database.
    It calls the external function for persistent storage.
    There is no need to validate the input.
    """
    movies = storage.get_movies()
    movie_to_update = input("Enter the movie for which you want to give an updated rating: ")
    if movie_to_update in movies:
        rating = float(input("Enter new movie rating: "))
        storage.update_movie(movie_to_update, rating)
        print(f"The rating for the movie has been updated.")
    else:
        print("Movie not found")


def stats(movies):
    """
    give the Average rating in the Database. I have rounded to the last two decimals
    Average
    """
    ratings = []
    if not movies:
        print("There are no movies in the database.")
        return

    for movie in movies.values():
        if movie["rating"] != "N/A":
            ratings.append(movie["rating"])

    average = sum(ratings) / len(ratings)
    print(f"Average rating: {average:.2f}")

    # Median
    ratings.sort()
    num_ratings = len(ratings)

    if num_ratings % 2 == 1:
        median = ratings[num_ratings // 2]
    else:
        median = (ratings[num_ratings // 2 - 1] + ratings[num_ratings // 2]) / 2

    print(f"Median rating: {median:.2f}")

    sorted_list_of_movies = sorted(
        movies.items(),
        key=lambda item: item[1]["rating"],
        reverse=True
    )

    best_rating = sorted_list_of_movies[0][1]["rating"]
    for title, info in sorted_list_of_movies:
        if info["rating"] == best_rating:
            print(f"Best rated movie: {title} ({info['rating']})")

    worse_rating = sorted_list_of_movies[-1][1]["rating"]
    for title, info in sorted_list_of_movies:
        if info["rating"] == worse_rating:
            print(f"Worse rated movie: {title} ({info['rating']})")


def random_movie(movies):
    """
    Print a random movie and its rating
    I convert the dictionary in a list of tuples
    I need to generate a random number and use it as an index to retrieve the item from the list
    """
    movies_list = list(movies.items())
    movie_index = random.randint(0, len(movies_list) - 1)
    print(f"""I randomly choose the following Movie for you >>
          {movies_list[movie_index][0]} - with a rating of {movies_list[movie_index][1]['rating']} 
          released {movies_list[movie_index][1]['year']}""")


def search_movie(movies):
    """
    looks for movies already in the database
    """
    search_string = input("Enter part of a movie name you want to search: ").lower()

    found = False

    for title, info in movies.items():
        if search_string in title.lower():
            print(f"{title}: Rating {info['rating']}")
            found = True

    if not found:
        print("No movies found that match your query.")


def movies_sorted_by_rating(movies):
    """
    Print all the movies and their ratings,
    in a descending order by the rating.
    Put differently, the best movie should be printed first,
    and the worst movie should be printed last.
    """
    placement = 0
    sorted_list_of_movies  = sorted(movies.items(),
                              key=lambda item: item[1]['rating'],
                              reverse=True)
    for title, info in sorted_list_of_movies:
        placement += 1
        print(f"Place {placement} - {title} : {info['rating']}")


def press_enter_to_continue():
    """
    Makes the output more redeable giving the user time to read
    """
    input("Press Enter to continue...")

def exit_app():
    """
    Gives the user the option to exit the app
    """
    print("Bye")
    sys.exit()


def main():
    """This is the main function where the user input of the commands is interpreted"""

    while True:
        user_choice = show_menu()
        if user_choice == "1":
            show_list_of_movies(storage.get_movies())
        elif user_choice == "2":
            add_movie()
        elif user_choice == "3":
            delete_movie()
        elif user_choice == "4":
            update_movie()

        elif user_choice == "5":
            stats(storage.get_movies())
        elif user_choice == "6":
            random_movie(storage.get_movies())
        elif user_choice == "7":
            search_movie(storage.get_movies())
        elif user_choice == "8":
            movies_sorted_by_rating(storage.get_movies())
        elif user_choice == "9":
            create_website(storage.get_movies_for_website())
        elif user_choice == "0":

            exit_app()
        else:
            print("Invalid command")

        press_enter_to_continue()

if __name__ == "__main__":
    main()
