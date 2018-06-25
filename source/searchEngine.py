import asyncio
from aiohttp import ClientSession

async def fetch(url, session, search_text):
    async with session.get(url) as response:
        response = await response.read()
    found = str(response).find(search_text)
    return {'text': response, 'found': found != -1, 'url': url, 'pos': found}

async def run(r, search_text):
    url = "http://www.gutenberg.org/files/{0}/{0}.txt"
    tasks = []

    # Fetch all responses within one Client session,
    # keep connection alive for all requests.
    async with ClientSession() as session:
        for i in range(r):
            task = asyncio.ensure_future(fetch(url.format(i), session, search_text))
            tasks.append(task)

        responses = asyncio.gather(*tasks)
        # you now have all response bodies in this variable
        return await responses


async def search_for(search_text):
    future = asyncio.ensure_future(run(100, search_text))
    return await future
