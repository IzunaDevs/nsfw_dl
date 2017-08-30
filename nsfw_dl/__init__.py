"""
Read the license at:
https://github.com/AraHaan/nsfw_dl/blob/master/LICENSE
"""
from . import errors
from . import dl
from . import generic


__title__ = 'nsfw_dl'
__author__ = 'Decorater'
__license__ = 'MIT'
__copyright__ = 'Copyright 2016 Decorater'
__version__ = '0.1.0a'
__build__ = 0x000001
__all__ = (errors.__all__ + dl.__all__ + generic.__all__)

NoLoader = errors.NoLoader
NoResultsFound = errors.NoResultsFound
NoXMLParser = errors.NoXMLParser
UnsupportedDataFormat = errors.UnsupportedDataFormat
NSFWDL = dl.NSFWDL
GenericRandom = generic.GenericRandom
GenericSearch = generic.GenericSearch
