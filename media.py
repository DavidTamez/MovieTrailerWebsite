import webbrowser

class Movie():
    """ This class provides a way to store movie related information """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # Initialize a new Movie object with the corresponding information
    def __init__(self, movie_title, movie_summary, poster_image, trailer_youtube,
                 movie_rating, movie_release_date, movie_actors):
        self.title = movie_title
        self.summary = movie_summary
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = movie_rating
        self.release_date = movie_release_date
        self.actors = movie_actors

    # Open a webbroweser window of the specified trailer url for the movie instance
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
