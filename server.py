#!/usr/bin/python3

from resources.client import app
from resources.client import api_client
from resources.client import Index
from resources.client import Function

__copyright__ = 'Copyright 2018, Juan David Arias'
__email__ = 'ariasg.juandavid@gmail.com'
__maintainer__ = 'Juan David Arias'
__author__ = 'Juan David Arias'
__status__ = 'developer'
__version__ = '1.0.1'
__license__ = 'GPL'

api_client.add_resource(Index, '/')
api_client.add_resource(Function, '/function')


if __name__ == '__main__':
    app.run(host='127.0.0.1')
