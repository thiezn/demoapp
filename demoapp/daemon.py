"""
DemoApp Web Daemon
~~~~~~~~~~~~~~~~~~~~~

The main web daemon class for serving the DemoApp website and API
"""

try:
    import uvloop
    import asyncio
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    pass

import logging
import json
from aiohttp import web
import aiohttp_jinja2
import jinja2
from .routes import setup_web_routes
from .database import setup_db


class Daemon:
    """Class representing the DemoApp REST API HTTP Daemon"""

    def __init__(self, host, port):
        """Initialise the DemoApp REST API

        :param host (string): host/ip to listen on
        :param port (int): port number to listen on
        """
        self.host = host
        self.port = port

    @classmethod
    def load_from_config(cls, filename):
        """Initialises a :class:`Daemon` instance from configuration file

        :param filename: the JSON configuration filename
        """
        with open(filename, 'r') as f:
            config = json.load(f)[0]

        return cls(
            config['host'],
            config['port'],
        )

    def start(self):
        """Starts the REST API"""

        logging.info('Initialising aiohttp web application')
        self.app = web.Application()

        logging.info('Initialising jinja2 modules')
        aiohttp_jinja2.setup(
            self.app, loader=jinja2.PackageLoader('demoapp', 'templates')
        )

        logging.info('Registering aiohttp on_startup functions')
        self.app.on_startup.append(setup_db)

        logging.info('Initialising Web routes')
        setup_web_routes(self.app)

        logging.info('Start web daemon')
        web.run_app(self.app, host=self.host, port=self.port)
