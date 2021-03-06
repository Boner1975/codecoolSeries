from data import data_manager
from psycopg2 import sql


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')

def get_shows_by_parm(column='rating', order='desc', limit=0):

    return data_manager.execute_select(
        sql.SQL("""
            SELECT shows.id, shows.title, shows.year, shows.runtime, shows.homepage, shows.trailer,
            to_char(shows.rating::float, '0.9') as rating,
            string_agg(genres.name, ', ' ORDER BY genres.name) as genres
            FROM shows
            JOIN show_genres on shows.id = show_genres.show_id
            JOIN genres on show_genres.genre_id = genres.id
            GROUP BY shows.id
            ORDER BY 
                case when %(order)s = 'asc' then {column} end ASC, 
                case when %(order)s = 'desc' then {column} end DESC 
            LIMIT %(limit)s
        """).format(column=sql.Identifier(column)),
        {'order': order, 'limit': limit}
    )
