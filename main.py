import logging
import sys

import aiohttp_jinja2
import jinja2
from aiohttp import web

from source.routes import setup_routes, setup_static_routes

async def init_app(argv=None):

    # init server
    app = web.Application()

    # setup Jinja2 template renderer
    aiohttp_jinja2.setup(
        app, loader=jinja2.PackageLoader('source', 'templates'))

    # setup views and routes
    setup_static_routes(app)
    setup_routes(app)

    return app


def main(argv):
    logging.basicConfig(level=logging.DEBUG)

    app = init_app(argv)

    web.run_app(app,
                host='localhost',
                port=8080)


if __name__ == '__main__':
    main(sys.argv[1:])
