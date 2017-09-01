"""
Read the license at:
https://github.com/IzunaDevs/nsfw_dl/blob/master/LICENSE
"""
from .errors import *
from .dl import *


__title__ = 'nsfw_dl'
__author__ = 'IzunaDevs'
__license__ = 'MIT'
__copyright__ = 'Copyright 2017 IzunaDevs'
__version__ = '0.1.0a0'
__build__ = 0x000100
__all__ = (errors.__all__ + dl.__all__)
