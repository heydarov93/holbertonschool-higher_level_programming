-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT g.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres g INNER JOIN tv_show_genres
ON g.id = tv_show_genres.genre_id
GROUP BY g.name ORDER BY number_of_shows DESC;
