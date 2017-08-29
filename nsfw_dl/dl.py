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

import importlib
import io
import json
from urllib.parse import quote

import aiohttp
from bs4 import BeautifulSoup


from .errors import UnsupportedDataFormat, NoLoader


LOADERS = {


}


class NSFWDL:
    def __init__(self, session=None, loop=None, json_loader=json.loads):
        self.session = session or aiohttp.ClientSession(loop=loop)
        self.json_loader = json_loader
        self.loaders = {}

    def add_loader(self, name, downloader):
        self.loaders[name] = downloader

    @staticmethod
    def parse_args(self, args):
        return quote(args)

    def __getattr__(self, item):
        if item in self.loaders:
            return self.loaders[item]
        return super().__getattr__(item)

    async def download(self, name, args="", download=False):
        if name not in self.loaders:
            raise NoLoader(f"No loader named {name!r}")

        loader = self.loaders[name]

        args = self.parse_args(args)
        url, data, headers = loader.prepare_url(args=args)
        async with getattr(self.session, loader.reqtype)(
                url, data=data, headers=headers) as resp:
            assert 200 <= resp.status_code < 300

            if loader.data_format == "bs4/html":
                reqdata = BeautifulSoup(await resp.text(), "html.parser")

            elif loader.data_format == "bs4/xml":
                reqdata = BeautifulSoup(await resp.text(), "lxml")

            elif loader.data_format == "json":
                reqdata = await resp.json(loads=self.json_loader)

            else:
                raise UnsupportedDataFormat(loader.data_format)

        img_url = loader.get_image(reqdata)

        if download:
            async with self.session.get(url) as resp:
                assert 200 <= resp.status_code < 300
                return io.BytesIO(await resp.read())

        return img_url

    def load_default(self):
        for loader, names in LOADERS.items():
            lib = importlib.import_module(loader)
            for name, loader_class in [(name, getattr(lib, name))
                                       for name in names]:
                load_obj = loader_class()
                self.add_loader(name, load_obj)
