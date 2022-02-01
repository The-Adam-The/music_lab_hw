from db.run_sql import run_sql

from models.artists import Artist


def select_all():
    artists = []

    sql = "SELECT * FROM artists"
    results = run_sql(sql)

    for row in results:
        artist = Artist(
            row['artist_name'],
            row['record_company'],
            row['id']
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


def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        artist = Artist(result['artist_name'], result['record_company'], result['id'])
    return artist


def delete_all():
    sql =  "DELETE FROM artists"
    run_sql(sql)

def delete_one(id):
    sql = "DELETE FROM artists WHERE id = %s"
    values = [id]
    run_sql(sql, values)