"""
Movie Database Management Module

This module provides utility functions to interact with a JSON-based movie database.
It supports operations such as retrieving, adding, updating, and deleting movies.

Functions:
- get_movies: Loads and returns all movies from the JSON file.
- save_movies: Saves the provided movies dictionary to the JSON file.
- add_movie: Adds a new movie to the database.
- delete_movie: Deletes a movie from the database by matching its title.
- update_movie: Updates the rating of an existing movie.

The module relies on external JSON processing functions (`read_json_data`, `write_json_data`)
imported from the `process_json_files` module.
"""


import os
from process_json_files import read_json_data, write_json_data


MOVIES_PATH = os.path.join("data", "movies.json")
NR_OF_DECIMALS = 3


def get_movies():
    """
    Returns a dictionary that contains
    the movies information in the database.

    The function loads the information from the JSON
    file and returns the data.
    """
    movies = read_json_data(MOVIES_PATH)
    for key, _ in movies.items():
        rating = movies[key]['rating']
        movies[key]['rating'] = round(rating, NR_OF_DECIMALS)
    return movies


def save_movies(movies):
    """
    Gets all your movies as an argument and saves them to the JSON file.
    """
    for key, _ in movies.items():
        rating = movies[key]['rating']
        movies[key]['rating'] = round(rating, NR_OF_DECIMALS)
    write_json_data(MOVIES_PATH, movies)


def add_movie(title, year, rating):
    """
    Adds a movie to the movies' database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = read_json_data(MOVIES_PATH)

    movies[title] = {"year": year, "rating": round(rating, NR_OF_DECIMALS)}

    write_json_data(MOVIES_PATH, movies)


def delete_movie(title):
    """
    Deletes a movie from the movies' database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = read_json_data(MOVIES_PATH)

    for key, _ in movies.items():
        if title.lower() in key.lower():
            del movies[key]
            write_json_data(MOVIES_PATH, movies)
            break


def update_movie(title, rating):
    """
    Updates a movie from the movies' database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = read_json_data(MOVIES_PATH)

    for key, _ in movies.items():
        if title.lower() in key.lower():
            movies[key]['rating'] = round(rating, NR_OF_DECIMALS)
            write_json_data(MOVIES_PATH, movies)
            break
