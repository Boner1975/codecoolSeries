from flask import Flask, render_template, url_for
from data import queries
import math
from dotenv import load_dotenv

load_dotenv()
app = Flask('codecool_series')

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
def most_rated(column='rating', order='desc', limit=15):
    shows = queries.get_shows_by_parm(column, order, limit)
    print(shows)
    return render_template('shows.html', shows=shows)



if __name__ == '__main__':
    main()
