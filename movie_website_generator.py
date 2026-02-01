import json


def load_html():
    """it loads a the HTML code from the template"""
    with open("_static/index_template.html", "r", encoding="utf-8") as fname:
        source_code = fname.read()
    return source_code

def create_movie_cards(movies):
    """
    It creates all the movie cards
    """
    if len(movies) == 0:
        print("There are no movies in the database.")
    else:
        output = ''  # define an empty string
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

    with open("index.html", "w", encoding="utf-8") as f:  # Write the new html code to a file
        f.write(new_html_code)

    print("Website was successfully generated to the file index.html.")