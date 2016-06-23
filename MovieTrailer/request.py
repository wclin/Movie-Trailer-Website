#!/usr/bin/env python
from urllib2 import Request, urlopen, URLError
import json
from pprint import pprint

api_key = "4f6c1387d0935fa644b5b7a1484146ac"

#request = Request('https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc' + '&api_key=' + api_key)
#request = Request('https://api.themoviedb.org/3/movie/246655?&api_key=' + api_key)
#request = Request('https://api.themoviedb.org/3/movie/246655/images?&api_key=' + api_key)

def sendReq(request):
    try:
        response = urlopen(request)
        data = response.read()
        jdata = json.loads(data)
        return jdata
        #jdata = jdata[u'results'][0]
        #pprint(jdata)
    except URLError, e:
        print 'No data. Got an error code:', e

def getPopList():
    pop_list = []
    request = Request('https://api.themoviedb.org/3/movie/popular?' 
            + '&api_key=' + api_key)
    jdata = sendReq(request)
    for mv in jdata['results']:
        pop_list.append(mv['id'])
    return pop_list

def getImage(movie_id):
    request = Request('https://api.themoviedb.org/3/movie/' + movie_id
            + '/images?&api_key=' + api_key)
    jdata = sendReq(request)
    file_path = jdata['backdrops'][0]['file_path']
    return 'https://image.tmdb.org/t/p/w500' + file_path

def getVideo(movie_id):
    request = Request('https://api.themoviedb.org/3/movie/' + movie_id 
            + '/videos?&api_key=' + api_key)
    jdata = sendReq(request)
    key = jdata['results'][0]['key']
    return 'https://www.youtube.com/watch?v=' + key

print getPopList()
print getImage('246655')
print getVideo('246655')

