import pdb

from models.artists import Artist
from models.albums import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository


artist_1 = Artist("Beatles", "Parlerphone")
artist_repository.save(artist_1)

album_1 = Album("Revolve", artist_1, "Classic Rock")
album_repository.save(album_1)

albums = album_repository.select_all()

for album in albums:
    print(album.__dict__)


# artists = artist_repository.select_all()

# for artist in artists:
#     print(artist.__dict__)

pdb.set_trace()

