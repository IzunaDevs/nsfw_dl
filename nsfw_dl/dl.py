"""
Read the license at:
https://github.com/IzunaDevs/nsfw_dl/blob/master/LICENSE
"""
import importlib
import io
import json
from urllib.parse import quote
from xml.etree import ElementTree

import aiohttp
from bs4 import BeautifulSoup

from .errors import NoLoader, UnsupportedDataFormat

LOADERS = {
    "danbooru": ["DanbooruRandom", "DanbooruSearch"],
    "drunkenpumken": ["DrunkenpumkenRandom"],
    "e621": ["E621Random", "E621Search"],
    "furrybooru": ["FurrybooruRandom", "FurrybooruSearch"],
    "gelbooru": ["GelbooruRandom", "GelbooruSearch"],
    "hbrowse": ["HbrowseRandom"],
    "konachan": ["KonachanRandom", "KonachanSearch"],
    "lolibooru": ["LolibooruRandom", "LolibooruSearch"],
    "nhentai": ["NhentaiRandom"],
    "rule34": ["Rule34Random", "Rule34Search"],
    "tbib": ["TbibRandom", "TbibSearch"],
    "xbooru": ["XbooruRandom", "XbooruSearch"],
    "yandere": ["YandereRandom", "YandereSearch"],
}


class NSFWDL:
    """
    Main class.
    """
    def __init__(self, loop=None, json_loader=json.loads):
        self.loop = loop
        self.session: aiohttp.ClientSession | None = None
        self.json_loader = json_loader
        self.loaders = {}
        self.load_default()

    def add_loader(self, name, downloader):
        """
        adds a loader to get images from.
        """
        self.loaders[name] = downloader

    @staticmethod
    def parse_args(args):
        """
        parses args.
        """
        return quote(args)

    async def __aenter__(self):
        if self.session is None:
            self.session = aiohttp.ClientSession(loop=self.loop)
        return self

    async def __aexit__(self, *exc):
        await self.session.close()
        return

    def __enter__(self):
        raise RuntimeError('Using this class outside of an async context is not supported.')

    def __exit__(self, *exc):
        return

    def __del__(self):
        self.session = None

    def __getattr__(self, item):
        if item in self.loaders:
            return self.loaders[item]

    async def get_async(self, url):
        async with self.session.get(url) as resp:
            return await resp.read()

    def get_sync(self, url):
        with self.session.get(url) as resp:
            return resp.content

    def get(self, url):
        return self.get_async(url) if self.async_ else self.get_sync(url)

    async def download(self, name, args="", download=False) -> str | io.BytesIO:
        """
        downloads or returns the image urls based on the loaders.
        """
        if name not in self.loaders:
            raise NoLoader(f"No loader named {name!r}")

        loader = self.loaders[name]

        args = self.parse_args(args)
        url, data, headers = loader.prepare_url(args=args)
        return await self._download(url, data, headers, loader, download)

    async def _download(self, url, data, headers, loader, download=False) -> str | io.BytesIO:
        """ async downloader. """
        reqtype = getattr(loader, 'reqtype', None)
        if reqtype is None:
            reqtype = "get"
        reqmeth = getattr(self.session, reqtype)

        async with reqmeth(url, data=data, headers=headers) as resp:
            assert 200 <= resp.status < 300

            if loader.data_format == "bs4/html":
                reqdata = BeautifulSoup(await resp.text(), "html.parser")

            elif loader.data_format == "xml":
                reqdata = ElementTree.fromstring(await resp.text())

            elif loader.data_format == "json":
                reqdata = await resp.json(loads=self.json_loader)

            elif loader.data_format == "url":
                reqdata = loader.data_format

            else:
                raise UnsupportedDataFormat(loader.data_format)

        if reqdata == "url":
            img_url = resp.url

        else:
            img_url = loader.get_image(reqdata)

        if download:
            async with self.session.get(img_url) as resp:
                assert 200 <= resp.status < 300
                return io.BytesIO(await resp.read())

        return img_url

    def xml_loader(self, text):
        """
        loads the xml file.
        """
        pass

    def load_default(self):
        """
        loads the loaders.
        """
        for loader, names in LOADERS.items():
            lib = importlib.import_module(f"nsfw_dl.loaders.{loader}")
            for name, loader_class in [(name, getattr(lib, name))
                                       for name in names]:
                load_obj = loader_class()
                self.add_loader(name, load_obj)
