"""
Read the license at:
https://github.com/AraHaan/nsfw_dl/blob/master/LICENSE
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
    def xml_to_json(data):
        """
        Transforms xml data to a list.
        """
        if int(data.find('posts')['count']) > 0:
            imagelist = [tag.get('file_url') for tag in data.find_all('post')]
            return imagelist
        else:
            raise NoResultsFound

    @staticmethod
    def get_image(data):
        """
        gets an image.
        """
        # get random image from a list.
        if data:
            if not isinstance(data, str):
                return random.choice(data)
