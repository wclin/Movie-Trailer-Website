import webbrowser
import request

class Movie():
    """A simple movie datastructure"""
    def __init__(self, tmdb_id):
        self.tmdb_id = tmdb_id
        self.title = getTitle(tmdb_id)
        self.poster_image_url = getPoster(tmdb_id)
        self.trailer_youtube_url = getVideo(tmdb_id)
