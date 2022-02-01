import pdb

from models.artists import Artist
from models.albums import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository


artist_1 = Artist("Madonna", "Parlerphone")
artist_repository.save(artist_1)







# artists = artist_repository.select_all()

# for artist in artists:
#     print(artist.__dict__)

pdb.set_trace()

