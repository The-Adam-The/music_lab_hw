from db.run_sql import run_sql

from models.albums import Album

import repositories.artist_repository as artist_repository


def select_all():
    albums = []

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist = artist_repository.select(row['artist_id'])
        album = Album(
            row['album_name'],
            artist,
            row['genre'],
            row['id']
        )
        albums.append(album)
    return albums

def save(album):
    sql= """INSERT INTO albums 
    (album_name, artist_id, genre)
    VALUES
    (%s, %s, %s)
    RETURNING id
    """

    values = [album.album_name, album.artist.id, album.genre]
    result = run_sql(sql, values)
    album.id = result[0]['id']
    return album


def select(id):
    album = None 
    sql = "SELECT * FROM users WHERE is = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        album = Album(result['album_name'], result['artist'], result['genre'], result['id'])
        return album


def delete_all():
    sql =  "DELETE FROM albums"
    run_sql(sql)

def delete_one(id):
    sql = "DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def album_for_artist(artist):
    albums = []

    sql  = "SELECT * FROM albums WHERE artist = %s"
    values = [artist.id]
    results = run_sql(sql, values)

    for row in results:
        album = Album(row['album_name'], artist, row['genre'], row['id'])
        albums.append(album)

    return albums

def update(album):

    sql ="""
    UPDATE albums
    SET(album_name, artist, genre)
    = (%s, %s, %s)
    WHERE id = %s
    """

    values = [
        album.album_name,
        album.artist.id,
        album.genre,
        album.id
    ]
    run_sql(sql, values)