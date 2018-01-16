import webbrowser


class Movie():
    """class describing the attributes of the movie"""
    def __init__(self, movie_title, movie_story,
                 poster_image, youtube_trailer):
        """Initializes the movie object from the args passed

            Args:
                movie_title (str): Movie's Title
                movie_story (str): Story of the movie
                poster_image (str): URL of the movie poster image
                youtube_trailer (str): Youtube URL of the movie trailer"""
        
        self.title = movie_title
        self.story_line = movie_story
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer

    def show_trailer(self):
        """Plays the youtube video on the browser from the trailer URL"""
        webbrowser.open(self.trailer_youtube_url)
