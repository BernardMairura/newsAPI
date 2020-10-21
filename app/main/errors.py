from flask import render_template
from . import main

# Handle errors
@main.app_errorhandler(404)
def page_not_found(error):
    '''
    Renders a 404 error page
    :param e:
    :return: render template fourOwfour.html
    '''
    return render_template('fourOwfour.html'),404