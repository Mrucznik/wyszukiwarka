import asyncio
from aiohttp import ClientSession
import re

async def fetch(url, session, search_text):
    global response_id
    async with session.get(url) as response:
        text_response = await response.text()

    regexp = re.compile("\W" + search_text.replace(" ", r"(\s|(\r\n)|\n)") + "\W")
    beginning = text_response.find("Character set encoding:")+30
    book_text = text_response[beginning:]

    found = regexp.search(book_text)
    if found:
        beginning = found.start()
        end = found.end()
        title = get_title(text_response)
        author = get_author(text_response)

        output_text = book_text[get_presentence(book_text, beginning):get_postsentence(book_text, end)]
        return {
            'found': True,
            'author': author,
            'title': title,
            'text': output_text,
            'url': url,
            'pos': beginning,
            'line_number': get_line_number(text_response, beginning)
        }
    else:
        return {'found': False}


def get_line_number(text, position):
    lines = 0
    for c in text[:position]:
        if "\n" in c:
            lines += 1
    return lines


def get_postsentence(text, position):
    pos = 0
    found_newlines = 0
    for c in text[position:]:
        pos += 1
        if "\n" in c:
            found_newlines += 1
            if found_newlines == 2:
                return position+pos-2


def get_presentence(text, position):
    pos = 0
    found_newlines = 0
    for c in reversed(text[:position]):
        pos += 1
        if "\n" in c:
            found_newlines += 1
            if found_newlines == 2:
                return position-pos+1


def get_title(text):
    title_regexp = re.search(r"Title: (.*?)(\r|\n)", text)
    if title_regexp:
        return title_regexp.group(1)
    else:
        return "Unknown"


def get_author(text):
    author_regexp = re.search(r"Author: (.*?)(\r|\n)", text)
    if author_regexp:
        return author_regexp.group(1)
    else:
        return "Unknown"


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
