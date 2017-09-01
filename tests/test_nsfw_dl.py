import asyncio
import pytest

import nsfw_dl

# All test coroutines will be treated as marked.
pytestmark = pytest.mark.asyncio


async def test_fake_loader(event_loop):
    """tests the NSFWDL class."""
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    await _nsfwdl.download("fake_loader", args="test")


async def test_danbooru_random():
    """tests danbooru's random."""
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("DanbooruRandom")
    assert ret is not ""


async def test_danbooru_search(event_loop):
    """tests danbooru's search."""
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("DanbooruSearch", args="test")
    assert ret is not ""
