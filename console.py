import pdb

from models.artists import Artist
from models.albums import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist("Beatles", "Parlerphone")
artist_repository.save(artist_1)

artist_2 = Artist("Nirvana", "I don't know")
artist_repository.save(artist_2)

artist_3 = Artist("Rolling Stones", "Time Warner")
artist_repository.save(artist_3)

album_1 = Album("Revolve", artist_1, "Classic Rock")
album_repository.save(album_1)

album_2 = Album("Nevermind", artist_2, "Grunge")
album_repository.save(album_2)

album_3 = Album("Sgt Pepper's Lonely Hearts Club Band", artist_1, "Classic Rock")
album_repository.save(album_3)

albums = album_repository.select_all()

for album in albums:
    print(album.__dict__)


artists = artist_repository.select_all()

for artist in artists:
    print(artist.__dict__)

album_repository.album_for_artist(artist_1)

pdb.set_trace()

