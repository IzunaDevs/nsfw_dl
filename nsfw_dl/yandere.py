# coding=utf-8
"""
The MIT License (MIT)

Copyright (c) 2016-2017 AraHaan

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""
from bs4 import BeautifulSoup

from .errors import *
from .tags import *


__all__ = ['yandere_random', 'yandere_search']


async def yandere_random(session):
    """Returns a random image from yande."""
    try:
        query = "https://yande.re/post/random"
        page = await session.get(query)
        page = await page.text()
        soup = BeautifulSoup(page, 'html.parser')
        image = soup.find(id="highres").get("href")
        return image
    except Exception as e:
        str(e)
        return None


async def yandere_search(searchtags, session):
    """Returns a specific image from yandere."""
    if isinstance(searchtags, str):
        try:
            searchtags = encode_tag(searchtags)
            query = "https://yande.re/post.json?tags=" + searchtags
            page = await session.get(query)
            json = await page.json()
            if not json == []:
                return json
            else:
                raise NoResultsFound('No images found.')
        except Exception as e:
            str(e)
            return None
    else:
        return -1
