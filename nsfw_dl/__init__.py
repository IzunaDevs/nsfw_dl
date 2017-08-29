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
from ._nsfw_code import *
from . import errors

__title__ = 'nsfw_dl'
__author__ = 'Decorater'
__license__ = 'MIT'
__copyright__ = 'Copyright 2016 Decorater'
__version__ = '0.0.1'
__build__ = 0x000001

# All methods require an aiohttp Client session.

__all__ = ['yandere_random', 'yandere_search', 'konachan_random',
           'konachan_search', 'e621_random',
           'e621_search', 'rule34_random', 'rule34_search', 'danbooru_random',
           'danbooru_search', 'gelbooru_random', 'gelbooru_search',
           'tbib_random', 'tbib_search', 'xbooru_random', 'xbooru_search',
           'furrybooru_random', 'furrybooru_search', 'drunkenpumken_random',
           'drunkenpumken_search', 'lolibooru_random', 'lolibooru_search',
           'nhentai_random', 'tsumino_random', 'hbrowse_random']


async def yandere_random(session):
    """Returns a random image from yande."""
    res = await _yandere_random(session)
    return res


async def yandere_search(searchtags, session):
    """Returns a specific image from yandere."""
    res = await _yandere_search(searchtags, session)
    return res


async def konachan_random(session):
    """Returns a random image from konachan."""
    res = await _konachan_random(session)
    return res


async def konachan_search(searchtags, session):
    """Returns a specific image from konachan."""
    res = await _konachan_search(searchtags, session)
    return res


async def e621_random(session):
    """Returns a random image from e621."""
    res = await _e621_random(session)
    return res


async def e621_search(searchtags, session):
    """Returns a specific image from e621."""
    res = await _e621_search(searchtags, session)
    return res


async def rule34_random(session):
    """Returns a random image from rule34."""
    res = await _rule34_random(session)
    return res


async def rule34_search(searchtags, session):
    """Returns a specific image from rule34."""
    res = await _rule34_search(searchtags, session)
    return res


async def danbooru_random(session):
    """Returns a random image from danbooru."""
    res = await _danbooru_random(session)
    return res


async def danbooru_search(searchtags, session):
    """Returns a specific image from danbooru."""
    res = await _danbooru_search(searchtags, session)
    return res


async def gelbooru_random(session):
    """Returns a random image from gelbooru."""
    res = await _gelbooru_random(session)
    return res


async def gelbooru_search(searchtags, session):
    """Returns a specific image from gelbooru."""
    res = await _gelbooru_search(searchtags, session)
    return res


async def tbib_random(session):
    """Returns a random image from tbib."""
    res = await _tbib_random(session)
    return res


async def tbib_search(searchtags, session):
    """Returns a specific image from tbib."""
    res = await _tbib_search(searchtags, session)
    return res


async def xbooru_random(session):
    """Returns a random image from xbooru."""
    res = await _xbooru_random(session)
    return res


async def xbooru_search(searchtags, session):
    """Returns a specific image from xbooru."""
    res = await _xbooru_search(searchtags, session)
    return res


async def furrybooru_random(session):
    """Returns a random image from furrybooru."""
    res = await _furrybooru_random(session)
    return res


async def furrybooru_search(searchtags, session):
    """Returns a specific image from furrybooru."""
    res = await _furrybooru_search(searchtags, session)
    return res


async def drunkenpumken_random(session):
    """Returns a specific image from drunkenpumken."""
    res = await _drunkenpumken_random(session)
    return res


async def drunkenpumken_search(searchtags, session):
    """Returns a specific image from drunkenpumken."""
    res = await _drunkenpumken_search(searchtags, session)
    return res


async def lolibooru_random(session):
    """Returns a random image from lolibooru."""
    res = await _lolibooru_random(session)
    return res


async def lolibooru_search(searchtags, session):
    """Returns a specific image from lolibooru."""
    res = await _lolibooru_search(searchtags, session)
    return res


async def nhentai_random(session):
    """Returns a random image from nhentai."""
    res = await _nhentai_random(session)
    return res


async def tsumino_random(session):
    """Returns a random image from tsumino."""
    res = await _tsumino_random(session)
    return res


async def hbrowse_random(session):
    """Returns a random image from hbrowse."""
    res = await _hbrowse_random(session)
    return res
