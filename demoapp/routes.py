"""
routes.py
~~~~~~~~~

Initialise the HTTP REST API routes/endpoints
"""
import os
import logging

from .webviews import home_page, about_page


def setup_web_routes(app):
    """Initialises the Web routes"""
    logging.debug('Adding route GET /')
    app.router.add_get('/', home_page)

    logging.debug('Adding route GET /about')
    app.router.add_get('/about', about_page)
