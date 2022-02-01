from db.run_sql import run_sql

from models.artists import Artist


def select_all():
    artists = []

    sql = "SELECT * FROM artists"
    results = run_sql(sql)

    for row in results:
        artist = Artist(
            row['artist_name'],
            row['record_company']
        )
        artists.append(artist)
    return artists


def save(artist):
    sql = "INSERT INTO artists (artist_name, record_company) VALUES (%s, %s) RETURNING *"
    values = [artist.artist_name, artist.record_company]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist