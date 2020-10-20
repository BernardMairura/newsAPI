from app import app
import urllib.request,json
from .models import source,article
from newsapi import NewsApiClient

News = news.Newsource

# Getting api key
api_key = app.config['6fe95eb68575443aa7b95cf911941266']

# Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_source(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        source_raw_data = url.read()
        sources_response = json.loads(source_raw_data)

        articles_list = None

        if sources_response['results']:
            movie_results_list = sources_response['results']
            movie_results = process_results(movie_results_list)


    return movie_results

