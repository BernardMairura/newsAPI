from flask import render_template
from app import app
from newsapi import NewsApiClient

# Views
@app.route('/')
def index():

