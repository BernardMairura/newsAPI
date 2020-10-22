import urllib.request,json
from .models import Source,Article
from maya import parse





# Getting api key
api_key = None
# Getting the news sources url
source_url = None
# Getting the news all sources url
all_sources_url = None

def configure_request(app):
    global api_key,source_url,all_sources_url
    api_key = app.config['NEWS_API_KEY']
    source_url = app.config['SOURCE_URL']
    all_sources_url = app.config['ALL_SOURCES_URL']


def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = all_sources_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        sources_raw_data  = url.read()
        sources_response = json.loads(sources_raw_data )

        sources_list = None

        if sources_response['sources']:
            new_list = []

            for source in sources_response['sources']:

                id=source['id']
                name=source['name']
                description=source ['description']

                new_sources =Source (id,name,description)
                new_list.append(new_sources)

            sources_list=new_list

    return sources_list


def get_specific_source(source_id):
    get_source_url = source_url.format(source_id, api_key)
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

    articles_list = None

    if get_source_response['articles']:
        new_list = []
        for article in get_source_response['articles']:
            title = article['title']
            author = article['author']
            description=article['description']
            image_url = article['urlToImage']
            source = article['source']
            date_published= parse(article['publishedAt']).datetime()
            article_url= article['url']

            if image_url:
                new_article = Article(author, title, description,article_url,date_published, image_url,source)
                new_list.append(new_article)

        articles_list = new_list


    return articles_list


     

