from flask import render_template
from . import main


@main.errorhandler(404)
def four_0w_four(error):
    """
    Function to renderthe 404 error page
    """
    return render_template('fourOwfour.html'),404
