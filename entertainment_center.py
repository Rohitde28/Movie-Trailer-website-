
"""Store details of movies and displays them on a website."""
import fresh_tomatoes
import media


def main():
        """Creates six Movie objects, initialising these objects with title,
        storyline, poster image link, video trailer link, release date and
        original full movie link."""
        martian = media.Movie(
            "The Martian",
            "A man is stuck on Mars",
            "https://www.shortto.com/matian",
            "https://www.youtube.com/watch?v=lQqhfq87FgY",
            "October 2, 2015",
            "https://www.youtube.com/watch?v=y62d4vNdq3Q",
            )
        Intesteller = media.Movie(
            "Intesteller",
            "Into the Future",
            "https://www.shortto.com/intes",
            "https://www.youtube.com/watch?v=0vxOhd4qlnA",
            "7 November 2014",
            "https://www.youtube.com/watch?v=vrjPsQYHU1c",
            )
        res_evil = media.Movie(
            "Resident Evil",
            "Zombie-causing virus escapes from the lab",
            "https://www.shortto.com/resident",
            "https://www.youtube.com/watch?v=kEutwdia8n0",
            "March 15, 2002",
            "https://www.youtube.com/watch?v=B9h4yYnstkA",
            )
        matrix = media.Movie(
            "The Matrix",
            "The world is a simulation",
            "https://www.shortto.com/matrix",
            "https://www.youtube.com/watch?v=vKQi3bBA1y8",
            "March 31, 1999",
            "https://www.youtube.com/watch?v=ZLdFEQoY78E",
            )
        the_dish = media.Movie(
            "The Dish",
            "A film about a radio telescope",
            "https://www.shortto.com/thedish",
            "https://www.youtube.com/watch?v=2TAqXENo1rA",
            "October 19, 2000",
            "https://www.youtube.com/watch?v=8bafhwUm7LA",
            )
        spectre = media.Movie(
            "Spectre",
            "The latest James Bond movie",
            "https://www.shortto.com/spectre",
            "https://www.youtube.com/watch?v=vBnGxAkdh_k",
            "October 26, 2015",
            "https://www.youtube.com/watch?v=26M4Eq4pswA",
            )
    # Store the Movie objects in a list.
        movies = [martian, Intesteller, res_evil, matrix, the_dish, spectre]
    # Open the movie website in the user's browser, featuring the movies above.
        fresh_tomatoes.open_movies_page(movies)
if __name__ == '__main__':
    main()
