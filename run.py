#!/usr/bin/env python3
from demoapp import Daemon
import os
import logging
import logging.handlers


def main():
    logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))

    path = os.path.dirname(os.path.realpath(__file__))
    config_file = '{}/config/server.json'.format(path)
    
    logging.info('Loading Daemon from config file {}'.format(config_file))
    web_daemon = Daemon.load_from_config(config_file)

    logging.info('Starting Web Daemon')
    web_daemon.start()


if __name__ == '__main__':
    main()

