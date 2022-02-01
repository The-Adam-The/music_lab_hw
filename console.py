import pdb

from models.artists import Artist

import repositories.artist_repository as artist_repository


artist_1 = Artist("Madonna", "Parlerphone")
artist_repository.save(artist_1)

artists = artist_repository.select_all()

# for artist in artists:
#     print(artist.__dict__)
pdb.set_trace()

