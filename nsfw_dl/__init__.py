"""
Read the license at:
https://github.com/IzunaDevs/nsfw_dl/blob/master/LICENSE
"""
from . import errors
from . import dl


__title__ = 'nsfw_dl'
__author__ = 'IzunaDevs'
__license__ = 'MIT'
__copyright__ = 'Copyright 2017 IzunaDevs'
__version__ = '0.1.0a'
__build__ = 0x000100
__all__ = (errors.__all__ + dl.__all__)

NoLoader = errors.NoLoader
NoResultsFound = errors.NoResultsFound
NoXMLParser = errors.NoXMLParser
UnsupportedDataFormat = errors.UnsupportedDataFormat
NSFWDL = dl.NSFWDL
