#!/usr/bin/env python
# Dynamically generate popular movie trailer website.
# by using fresh_potatoes:
# https://github.com/adarsh0806/ud036_StarterCode/blob/master/fresh_tomatoes.py
# and tmdb api: https://api.themoviedb.org/3/
import fresh_potatoes as fp
import media
from tmdb3 import *
import sys
    
if len(sys.argv) > 1:
    key = str(sys.argv[1]) # Set api_key from input
else:
    try:
        file = open('api_key.txt', 'r')
        key = file.read() # Set api_key from api_key.txt
    except IOError as e:
        print 'No key. Got an error code', e
setKey(key)

pop_list = getPopList()  # A list of tmdb_id(int)
mv_list = []

# For each movie in list, construct it from the given tmdb_id.
for tmdb_id in pop_list:
    mv_list.append(media.Movie(tmdb_id))

fp.open_movies_page(mv_list)
