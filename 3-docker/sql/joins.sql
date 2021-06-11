-- joins

-- pair each row with each other row
SELECT *
FROM customers CROSS JOIN employees;

SELECT tracks.id, tracks.name AS name, genres.name AS genre
FROM tracks INNER JOIN genres ON tracks.genre_id = genres.id;

SELECT tracks.id, tracks.name AS name, genres.name AS genre, albums.title AS album
FROM tracks
    INNER JOIN genres ON tracks.genre_id = genres.id
    LEFT JOIN albums ON tracks.album_id = albums.id;

-- all rock songs
SELECT tracks.id, tracks.name
FROM tracks INNER JOIN genres
    ON tracks.genre_id = genres.id
WHERE genres.name = 'Rock';

SELECT (COALESCE(artists.name, 'n/a') || ' - ' || tracks.name) AS Song
FROM tracks
    LEFT JOIN genres ON tracks.genre_id = genres.id
    LEFT JOIN albums ON tracks.album_id = albums.id
    LEFT JOIN artists ON albums.artist_id = artists.id
WHERE genres.name = 'Rock';
