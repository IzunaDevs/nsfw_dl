# coding=utf-8
"""
The MIT License (MIT)

Copyright (c) 2016 AraHaan

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

__all__ = ['_yandere_random', '_yandere_search', '_konachan_random',
           '_konachan_search', '_e621_random', '_e621_search',
           '_rule34_random', '_rule34_search', '_danbooru_random',
           '_danbooru_search', '_gelbooru_random', '_gelbooru_search',
           '_tbib_random', '_tbib_search', '_xbooru_random', '_xbooru_search',
           '_furrybooru_random', '_furrybooru_search', '_drunkenpumken_random',
           '_drunkenpumken_search', '_lolibooru_random', '_lolibooru_search',
           '_nhentai_random', '_tsumino_random', '_hbrowse_random']


async def _gelbooru_random(session):
    """Returns a random image from gelbooru."""
    try:
        query = "http://www.gelbooru.com/index.php?page=post&s=random"
        page = await session.get(query)
        page = await page.text()
        soup = BeautifulSoup(page, 'html.parser')
        image = soup.find(id="image").get("src")
        return image
    except Exception as e:
        str(e)
        return None


async def _gelbooru_search(searchtags, session):
    """Returns a specific image from gelbooru."""
    if isinstance(searchtags, str):
        try:
            searchtags = encode_tag(searchtags)
            query = "http://gelbooru.com/index.php?page=dapi&s=post&q=index" \
                    "&tags=" + searchtags
            page = await session.get(query)
            page = await page.text()
            soup = BeautifulSoup(page, 'lxml')
            if int(soup.find('posts')['count']) > 0:
                imagelist = [tag.get('file_url') for tag in soup.find_all(
                    'post')]
                return imagelist
            else:
                raise NoResultsFound('No images found.')
        except Exception as e:
            str(e)
            return None
    else:
        return -1  # searchtags is not a string.


async def _tbib_random(session):
    """Returns a random image from tbib."""
    try:
        query = "http://www.tbib.org/index.php?page=post&s=random"
        page = await session.get(query)
        page = await page.text()
        soup = BeautifulSoup(page, 'html.parser')
        image = soup.find(id="image").get("src")
        return image
    except Exception as e:
        str(e)
        return None


async def _tbib_search(searchtags, session):
    """Returns a specific image from tbib."""
    if isinstance(searchtags, str):
        try:
            searchtags = encode_tag(searchtags)
            query = "http://www.tbib.org/index.php?page=dapi&s=post&q=index" \
                    "&tags=" + searchtags
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
        return -1  # searchtags is not a string.


async def _xbooru_random(session):
    """Returns a random image from xbooru."""
    try:
        query = "http://xbooru.com/index.php?page=post&s=random"
        page = await session.get(query)
        page = await page.text()
        soup = BeautifulSoup(page, 'html.parser')
        image = soup.find(id="image").get("src")
        return image
    except Exception as e:
        str(e)
        return None


async def _xbooru_search(searchtags, session):
    """Returns a specific image from xbooru."""
    if isinstance(searchtags, str):
        try:
            searchtags = encode_tag(searchtags)
            query = "http://xbooru.com/index.php?page=dapi&s=post&q=index" \
                    "&tags=" + searchtags
            page = await session.get(query)
            page = await page.text()
            soup = BeautifulSoup(page, 'lxml')
            if int(soup.find('posts')['count']) > 0:
                imagelist = [tag.get('file_url') for tag in soup.find_all(
                    'post')]
                return imagelist
            else:
                raise NoResultsFound('No images found.')
        except Exception as e:
            str(e)
            return None
    else:
        return -1  # searchtags is not a string.


async def _furrybooru_random(session):
    """Returns a random image from furrybooru."""
    try:
        query = "http://furry.booru.org/index.php?page=post&s=random"
        page = await session.get(query)
        page = await page.text()
        soup = BeautifulSoup(page, 'html.parser')
        image = soup.find(id="image").get("src")
        return image
    except Exception as e:
        str(e)
        return None


async def _furrybooru_search(searchtags, session):
    """Returns a specific image from furrybooru."""
    if isinstance(searchtags, str):
        try:
            searchtags = encode_tag(searchtags)
            query = (
                "http://furry.booru.org/index.php?page=post&s=list&tags=" +
                searchtags)
            page = await session.get(query)
            page = await page.text()
            soup = BeautifulSoup(page, 'lxml')
            if int(soup.find('posts')['count']) > 0:
                imagelist = [tag.get('file_url') for tag in soup.find_all(
                    'post')]
                return imagelist
            else:
                raise NoResultsFound('No images found.')
        except Exception as e:
            str(e)
            return None
    else:
        return -1  # searchtags is not a string.


async def _drunkenpumken_random(session):
    """Returns a specific image from drunkenpumken."""
    try:
        query = "http://drunkenpumken.booru.org/index.php?page=post&s=random"
        page = await session.get(query)
        page = await page.text()
        soup = BeautifulSoup(page, 'html.parser')
        image = soup.find(id="image").get("src")
        return image
    except Exception as e:
        str(e)
        return None


async def _drunkenpumken_search(searchtags, session):
    """Returns a specific image from drunkenpumken."""
    if isinstance(searchtags, str):
        try:
            searchtags = encode_tag(searchtags)
            query = "http://drunkenpumken.booru.org/index.php?page=dapi&s" \
                    "=post&q=index&tags=" + searchtags
            page = await session.get(query)
            page = await page.text()
            soup = BeautifulSoup(page, 'lxml')
            if int(soup.find('posts')['count']) > 0:
                imagelist = [tag.get('file_url') for tag in soup.find_all(
                    'post')]
                return imagelist
            else:
                raise NoResultsFound('No images found.')
        except Exception as e:
            str(e)
            return None
    else:
        return -1  # searchtags is not a string.


async def _lolibooru_random(session):
    """Returns a random image from lolibooru."""
    try:
        query = "https://lolibooru.moe/post/random/"
        page = await session.get(query)
        page = await page.text()
        soup = BeautifulSoup(page, 'html.parser')
        image = soup.find(id="image").get("src")
        image = image.replace(' ', '%20')
        return image
    except Exception as e:
        str(e)
        return None


async def _lolibooru_search(searchtags, session):
    """Returns a specific image from lolibooru."""
    if isinstance(searchtags, str):
        try:
            query = "https://lolibooru.moe/post/index.json?tags=" + searchtags
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
        return -1  # searchtags is not a string.
