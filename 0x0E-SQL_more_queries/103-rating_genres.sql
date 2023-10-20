-- Lists all genres in the database hbtn_0d_tvshows_rate by their rating
-- Lists all rows of a table by the sum of a linked row
SELECT tv_genres.name, SUM(tv_show_genres.rate) 'rating'
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_genres.name
ORDER BY rating DESC;