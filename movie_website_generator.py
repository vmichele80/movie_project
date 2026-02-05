
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "_static")
TEMPLATE_PATH = os.path.join(STATIC_DIR, "index_template.html")
OUTPUT_HTML = os.path.join(BASE_DIR, "index.html")


def load_html():
    """it loads the HTML code from the template"""
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as fname:
        source_code = fname.read()
    return source_code


def create_movie_cards(movies):
    """
    It creates all the movie cards
    """

    output = ''  # define an empty string

    if len(movies) == 0:
        output = 'There are no movies in the database.'
    else:
        for movie in movies:
            movie_title = movie[0]
            movie_year = movie[1]
            movie_rating = movie[2]
            movie_poster_url = movie[3]

            output += '<li>'
            output += '<div class ="movie">'
            output += f'<img class ="movie-poster" src = "{movie_poster_url}" />'
            output += f'<div class ="movie-title"> {movie_title} </div>'
            output += f'<div class ="movie-year"> {movie_year} </div>'
            output += f'<div class ="movie-year"> Rating {movie_rating} </div>'
            output += '</div>'
            output += '</li>'

    return output


def create_website(movies):
    html_code = load_html()
    movies_cards = create_movie_cards(movies)

    new_html_code = html_code.replace("__TEMPLATE_MOVIE_GRID__", movies_cards)

    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:  # Write the new html code to a file
        f.write(new_html_code)

    print("Website was successfully generated to the file index.html.")