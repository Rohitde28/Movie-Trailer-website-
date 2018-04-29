"""File to Define the movie Class and this file initialises the contents
of the movie ."""
import webbrowser


class Movie(object):
    """This class provides a way to store movie related information.

    Attributes:title: A string to store the title of the movie.
        storyline: A string to store the basic plot of the movie.
        poster_image_url: A string to store the URL of the movie poster.
        trailer_url: A string to store the URL of  movie trailer.
        release_date: A string to store the release date of the movie
        full_movie_link: A string to store the URL of the full movie
        available on Internet
    """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, movie_release_date, full_movie_link):
        """Initialises Movie class instance variables."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date = movie_release_date
        self.full_link = full_movie_link

    def show_trailer(self):
        """Plays the movie trailer in the web browser."""
        webbrowser.open(self.trailer_youtube_url)
