This project creates a nice gallery of your preferred movies.

movie.py is the main entry point of the application. It implements a command-line interface (CLI) that allows users to manage a personal movie database.

The file is responsible for:

Displaying an interactive menu and handling user input

Listing all stored movies with their ratings and release years

Adding new movies by retrieving data from the OMDb API

Updating and deleting movies in the database

Computing statistics such as average rating, median rating, and best/worst rated movies

Selecting and displaying a random movie

Searching movies by partial title match

Sorting movies by rating

Generating a static movie website from the stored data

movie.py orchestrates the application logic by connecting user actions to the underlying storage layer and external services, while keeping persistence and API handling modularized in separate files.