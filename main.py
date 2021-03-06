from flask import Flask, render_template, url_for
from data import queries
import math
from dotenv import load_dotenv

load_dotenv()
app = Flask('codecool_series')

SHOWS_PER_PAGE = 15

@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/design')
def design():
    return render_template('design.html')


def main():
    app.run(debug=False)

@app.route('/shows/most-rated')
@app.route('/shows/order-by-<column>')
@app.route('/shows/order-by-<column>-<order>')
@app.route('/shows/order-by-<column>/<int:page_number>')
@app.route('/shows/order-by-<column>-<order>/<int:page_number>')
def most_rated(page_number=1, column='rating', order='desc'):
    count = queries.get_show_count()
    page_count = math.ceil(count[0]['count']/SHOWS_PER_PAGE)
    shows = queries.get_shows_by_parm(column, order, SHOWS_PER_PAGE, (page_number-1)*SHOWS_PER_PAGE)

    return render_template('shows.html', shows=shows)




@app.route('/tv-show/<int:id>')
def show_page(id):
    show = queries.get_show_by_id(id)
    seasons = queries.get_show_seasons(id)
    characters = queries.get_show_characters(id)
    show['characters_str'] = ', '.join([character['name'] for character in characters])
    show['trailer_id'] = show['trailer'].split('=')[1] if show['trailer'] else ''
    show['runtime_str'] = ''
    return render_template('show.html', show = show, seasons = seasons)


if __name__ == '__main__':
    main()
