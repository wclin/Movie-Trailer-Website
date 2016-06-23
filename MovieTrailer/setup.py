import fresh_potatoes as fp
import media
from request import *

pop_list = getPopList()
mv_list = []

for tmdb_id in pop_list:
    mv_list.append(media.Movie(tmdb_id))
#mv = media.Movie('Showtimes for A Hologram for the King',
#        'http://t3.gstatic.com/images?q=tbn:ANd9GcTn4cbbsC68ZyzFYf70wQKBI7ftcPFr26u2kF11ZDaI00CeuAo9',
#        'https://www.youtube.com/watch?v=eJtVctN0xIM')

fp.open_movies_page(mv_list)
