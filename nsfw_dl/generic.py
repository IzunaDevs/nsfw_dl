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
import random

from .errors import NoResultsFound


__all__ = ['GenericRandom', 'GenericSearch']


class GenericRandom:
    """ generic random base class """

    @staticmethod
    def prepare_url(args):
        """
        prepares the request url.
        """
        pass

    @staticmethod
    def get_image(data):
        """
        gets an image.
        """
        image = data.find(id="highres").get("href")
        # seems all dont have highres based on my old sources.
        if image is None:
            image = data.find(id="image").get("src")
        return image


class GenericSearch:
    """ generic search base class """

    @staticmethod
    def prepare_url(args):
        """
        prepares the request url.
        """
        pass

    @staticmethod
    def get_image(data):
        """
        gets an image.
        """
        if data:
            return random.choice(data)['file_url']
        raise NoResultsFound
