
DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS artists;


CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    artist_name VARCHAR(255),
    record_company VARCHAR(255)
);

CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    album_name VARCHAR(255),
    genre VARCHAR(255),
    artist INT REFERENCES artists(id)
)