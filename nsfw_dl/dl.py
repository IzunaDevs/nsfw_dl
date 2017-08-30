"""
Read the license at:
https://github.com/AraHaan/nsfw_dl/blob/master/LICENSE
"""
import importlib
import io
import json
from urllib.parse import quote

import aiohttp
from bs4 import BeautifulSoup


from .errors import UnsupportedDataFormat, NoLoader


__all__ = ['NSFWDL']
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
    "tsumino": ["TsuminoRandom"],
    "xbooru": ["XbooruRandom", "XbooruSearch"],
    "yandere": ["YandereRandom", "YandereSearch"],
}


class NSFWDL:
    """
    Main class.
    """
    def __init__(self, session=None, loop=None, json_loader=json.loads):
        self.session = session or aiohttp.ClientSession(loop=loop)
        self.json_loader = json_loader
        self.loaders = {}

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

    def __getattr__(self, item):
        if item in self.loaders:
            return self.loaders[item]

    async def download(self, name, args="", download=False, search=False):
        """
        downloads or returns the image urls based on the loaders.
        """
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
                # transform xml to list.
                reqdata = loader.xml_to_json(reqdata)

            elif loader.data_format == "json":
                reqdata = await resp.json(loads=self.json_loader)

            # return type is an url.
            elif loader.data_format == "aiohttp/url":
                reqdata = loader.data_format
            else:
                raise UnsupportedDataFormat(loader.data_format)

        if reqdata == "aiohttp/url":
            img_url = resp.url
        else:
            img_url = loader.get_image(reqdata)

        if download:
            async with self.session.get(url) as resp:
                assert 200 <= resp.status_code < 300
                return io.BytesIO(await resp.read())

        return img_url

    def load_default(self):
        """
        loads the loaders.
        """
        for loader, names in LOADERS.items():
            lib = importlib.import_module(f".loaders.{loader}")
            for name, loader_class in [(name, getattr(lib, name))
                                       for name in names]:
                load_obj = loader_class()
                self.add_loader(name, load_obj)
