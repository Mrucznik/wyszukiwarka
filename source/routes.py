# routes.py
import pathlib
from aiohttp import web
import aiohttp_jinja2
from source.searchEngine import search_for


PROJECT_ROOT = pathlib.Path(__file__).parent.parent
routes = web.RouteTableDef()


@routes.get('/')
@aiohttp_jinja2.template('index.html')
async def hello(request):
    return {}


@routes.get('/search/{text}')
async def search(request):
    search_text = request.match_info['text']
    response = ""
    for found in await search_for(search_text):
        if found['found']:
            response += "Znaleziono na pozycji {}, <a href=\"{}\">link</a><br/>".format(found['pos'], found['url'])
    return web.Response(text=response, content_type="text/html")


def setup_static_routes(app):
    app.router.add_static('/public',
                          path=PROJECT_ROOT / 'public',
                          name='public')


def setup_routes(app):
    app.add_routes(routes)
