"""
Read the license at:
https://github.com/IzunaDevs/nsfw_dl/blob/master/LICENSE
"""

__all__ = ['NoLoader', 'NoResultsFound', 'NoXMLParser',
           'UnsupportedDataFormat']


class BaseErrors(Exception):
    """
    Base Exception Class.
    """
    pass


class NoLoader(BaseErrors):
    """
    Thrown when there is no such loader in the NSFWDL instance
    """
    pass


class NoResultsFound(BaseErrors):
    """
    Thrown when the search found no results for the search.
    """
    pass


class NoXMLParser(BaseErrors):
    """
    Thrown when there is no xml parser.
    """
    pass

class UnsupportedDataFormat(BaseErrors):
    """
    Thrown when there is an unsupported format.
    """
    pass
