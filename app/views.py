from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

from .request import get_news

@app.route('/')
def news():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting trending news
    sources_news = get_news('trending')
    print(sources_news)
    title = 'Home - Trending news'
    return render_template('index.html', title = title,sources = sources_news)