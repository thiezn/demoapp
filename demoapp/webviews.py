"""
webviews.py
~~~~~~~~

Holds all the website views
"""
import aiohttp_jinja2
from .database import list_users


@aiohttp_jinja2.template('home.html')
async def home_page(request):
    """Serving the main webpage showing backend data"""
    db = request.app['db']
    users = await list_users(db)
    return users


@aiohttp_jinja2.template('about.html')
async def about_page(request):
    return {'whoarewe_page_active': True}
