"""
Read the license at:
https://github.com/IzunaDevs/nsfw_dl/blob/master/LICENSE
"""
import random

from nsfw_dl.errors import NoResultsFound

# base classes for some loaders.


class BaseSearchXML:
    """ base xml search class. """
    @staticmethod
    def prepare_url(args):
        """ ... """
        pass

    @staticmethod
    def get_image(data):
        """ ... """
        if data:
            if int(data.find('posts')['count']) > 0:
                imagelist = [tag.get('file_url') for tag in data.find_all(
                    'post')]
                return random.choice(imagelist)
        raise NoResultsFound


class BaseSearchHTML:
    """ base html search class. """
    @staticmethod
    def prepare_url(args):
        """ ... """
        pass

    @staticmethod
    def get_image(data):
        """ ... """
        if data:
            images = data.find_all(attrs="thumb")
            if images:
                return random.choice(images).find("img").get("src")
        raise NoResultsFound


class BaseSearchJSON:
    """ base json search class. """
    @staticmethod
    def prepare_url(args):
        """ ... """
        pass

    @staticmethod
    def get_image(data):
        """ ... """
        if data:
            return random.choice(data)['file_url']
        raise NoResultsFound
