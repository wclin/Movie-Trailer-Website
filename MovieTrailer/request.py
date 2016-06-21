#!/usr/bin/env python
from urllib2 import Request, urlopen, URLError
import json
from pprint import pprint

api_key = "4f6c1387d0935fa644b5b7a1484146ac"

request = Request('https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc' + '&api_key=' + api_key)

try:
    response = urlopen(request)
    data = response.read()
    jdata = json.loads(data)
    jdata = jdata[u'results'][0]
    pprint(jdata)
except URLError, e:
    print 'No data. Got an error code:', e
