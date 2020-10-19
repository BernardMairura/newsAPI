from flask import render_template
from app import app
from newsapi import NewsApiClient

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    newsapi=NewsApiClient(api_key="6fe95eb68575443aa7b95cf911941266")

    topheadlins=newsapi.get_top_headlines(sources="abc-news-au")

    articles=topheadlins['articles']
    desc=[]
    news=[] 
    img=[]

    for i in range(len(articles)):
        myarticles=articles[i]

        news.append(myarticles(['title']))
        desc.append(myarticles(['description']))
        img.append(myarticles(['urlToImage']))

        mylist=zip(news,desc,img)

    return render_template('index.html',context=mylist)


@app.route('/movie/<movie_id>')
def movie(movie_id):

    '''
    View news page function that returns the news details page and its data
    '''
    return render_template('news.html',id = movie_id)