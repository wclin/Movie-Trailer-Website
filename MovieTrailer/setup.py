import fresh_potatoes as fp
import media
from tmdb3 import *

pop_list = getPopList()
mv_list = []

for tmdb_id in pop_list:
    mv_list.append(media.Movie(tmdb_id))

fp.open_movies_page(mv_list)
