import webbrowser
from tmdb3 import *


class Movie():
    """A simple movie datastructure corresponding to https://api.themoviedb.org/3/
    
    Attributes:
        tmdb_id (int): The ID in themoviedb.
        title (str): The original title. 
        poster_image_url (str): The url of poster image(on tmdb site). 
        trailer_youtube_url (str): The url of youtube trailer. 

    """

    def __init__(self, tmdb_id):
        self.tmdb_id = tmdb_id
        self.title = getTitle(tmdb_id)
        self.poster_image_url = getPoster(tmdb_id)
        self.trailer_youtube_url = getVideo(tmdb_id)
