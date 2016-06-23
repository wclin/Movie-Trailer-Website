#!/usr/bin/env python
# Dynamically generate popular movie trailer website.
# by using fresh_potatoes:
# https://github.com/adarsh0806/ud036_StarterCode/blob/master/fresh_tomatoes.py
# and tmdb api: https://api.themoviedb.org/3/
import fresh_potatoes as fp
import media
from tmdb3 import *

pop_list = getPopList()  # A list of tmdb_id(int)
mv_list = []

# For each movie in list, construct it from the given tmdb_id.
for tmdb_id in pop_list:
    mv_list.append(media.Movie(tmdb_id))

fp.open_movies_page(mv_list)
