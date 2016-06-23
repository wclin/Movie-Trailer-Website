#!/usr/bin/env python
# A simple python wrapper for tmdb3: https://api.themoviedb.org/3/
from urllib2 import Request, urlopen, URLError
import json
from pprint import pprint

api_key = "4f6c1387d0935fa644b5b7a1484146ac"


def sendReq(request):
    try:
        response = urlopen(request)
        data = response.read()
        jdata = json.loads(data)
        return jdata
    except URLError as e:
        print 'No data. Got an error code:', e

# Return a list of tmdb_id of popular movies
def getPopList():
    pop_list = []
    request = Request('https://api.themoviedb.org/3/movie/popular?'
                      + '&api_key=' + api_key)
    jdata = sendReq(request)
    for mv in jdata['results']:
        pop_list.append(mv['id'])
    return pop_list

# Return the url of youtube trailer
def getVideo(movie_id):
    request = Request('https://api.themoviedb.org/3/movie/' + str(movie_id)
                      + '/videos?&api_key=' + api_key)
    jdata = sendReq(request)
    key = jdata['results'][0]['key']
    return 'https://www.youtube.com/watch?v=' + key

# Return the movie title
def getTitle(movie_id):
    request = Request('https://api.themoviedb.org/3/movie/' + str(movie_id)
                      + '?&api_key=' + api_key)
    jdata = sendReq(request)
    title = jdata['original_title']
    return title

# Return the url of poster image
def getPoster(movie_id):
    request = Request('https://api.themoviedb.org/3/movie/' + str(movie_id)
                      + '?&api_key=' + api_key)
    jdata = sendReq(request)
    poster_path = jdata['poster_path']
    return 'https://image.tmdb.org/t/p/w500' + poster_path

