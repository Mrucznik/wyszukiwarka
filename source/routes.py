# routes.py
import pathlib
from aiohttp import web, WSMsgType
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


@routes.get('/ws/search')
async def websocket_search(request):

    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        if msg.type == WSMsgType.TEXT or msg.type == WSMsgType.CLOSE:
            if msg.data == 'close':
                await ws.close()
            else:
                await ws.send_str('Szukam...')
                for found in await search_for(msg.data):
                    if found and found['found']:
                        await ws.send_str("Znaleziono na pozycji {}, <a href=\"{}\">link</a><br/>".format(found['pos'], found['url']))
                await ws.send_str('Koniec.')
        elif msg.type == WSMsgType.ERROR:
            print('ws connection closed with exception %s' %
                  ws.exception())

    print('websocket connection closed')
    return ws


def setup_static_routes(app):
    app.router.add_static('/public',
                          path=PROJECT_ROOT / 'public',
                          name='public')


def setup_routes(app):
    app.add_routes(routes)
