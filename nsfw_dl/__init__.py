"""
Read the license at:
https://github.com/IzunaDevs/nsfw_dl/blob/master/LICENSE
"""
from .dl import *


__title__ = 'nsfw_dl'
__author__ = 'IzunaDevs'
__license__ = 'MIT'
__copyright__ = 'Copyright 2017 IzunaDevs'
__version__ = '0.1.0a'
__build__ = 0x000100


class NoLoader(Exception):
    """
    Thrown when there is no such loader in the NSFWDL instance
    """
    pass


class NoResultsFound(Exception):
    """
    Thrown when the search found no results for the search.
    """
    pass


class NoXMLParser(Exception):
    """
    Thrown when there is no xml parser.
    """
    pass


class UnsupportedDataFormat(Exception):
    """
    Thrown when there is an unsupported format.
    """
    pass


__errors__ = ['NoLoader', 'NoResultsFound', 'NoXMLParser',
              'UnsupportedDataFormat']
__all__ = (__errors__ + dl.__all__)
