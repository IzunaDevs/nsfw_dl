import asyncio
import pytest

import nsfw_dl

# All test coroutines will be treated as marked.
pytestmark = pytest.mark.asyncio


async def test_fake_loader(event_loop):
    """tests the NSFWDL class."""
    with pytest.raises(nsfw_dl.errors.NoLoader):
        _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
        await _nsfwdl.download("fake_loader", args="test")


async def test_danbooru_random(event_loop):
    """tests danbooru's random."""
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("DanbooruRandom")
    assert ret is not ""


async def test_danbooru_search(event_loop):
    """tests danbooru's search."""
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("DanbooruSearch", args="test")
    assert ret is not ""


async def test_drunkenpumken_random(event_loop):
    """tests drunkenpumken's random."""
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("DrunkenpumkenRandom")
    assert ret is not ""


async def test_e621_random(event_loop):
    """tests e621's random."""
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("E621Random")
    assert ret is not ""


async def test_e621_search(event_loop):
    """tests e621's search."""
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("E621Search", args="test")
    assert ret is not ""


async def test_furrybooru_random(event_loop):
    """tests furrybooru's random."""
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("FurrybooruRandom")
    assert ret is not ""


async def test_furrybooru_search(event_loop):
    """tests furrybooru's search."""
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("FurrybooruSearch", args="test")
    assert ret is not ""


async def test_gelbooru_random(event_loop):
    """tests gelbooru's random."""
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("GelbooruRandom")
    assert ret is not ""


async def test_gelbooru_search(event_loop):
    """tests gelbooru's search."""
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("GelbooruSearch", args="test")
    assert ret is not ""


async def test_hbrowse_random(event_loop):
    """tests hbrowse's random."""
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("HbrowseRandom")
    assert ret is not ""


async def test_konachan_random(event_loop):
    """tests konachan's random."""
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("KonachanRandom")
    assert ret is not ""


async def test_konachan_search(event_loop):
    """tests konachan's search."""
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("KonachanSearch", args="test")
    assert ret is not ""


async def test_lolibooru_random(event_loop):
    """tests lolibooru's random."""
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("LolibooruRandom")
    assert ret is not ""


async def test_lolibooru_search(event_loop):
    """tests lolibooru's search."""
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("LolibooruSearch", args="test")
    assert ret is not ""


async def test_nhentai_random(event_loop):
    """tests nhentai's random."""
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("NhentaiRandom")
    assert ret is not ""


async def test_rule34_random(event_loop):
    """tests rule34's random."""
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("Rule34Random")
    assert ret is not ""


async def test_rule34_search(event_loop):
    """tests rule34's search."""
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("Rule34Search", args="test")
    assert ret is not ""


async def test_tbib_random(event_loop):
    """tests tbib's random."""
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("TbibRandom")
    assert ret is not ""


async def test_tbib_search(event_loop):
    """tests tbib's search."""
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("TbibSearch", args="test")
    assert ret is not ""


async def test_tsumino_random(event_loop):
    """tests tsumino's random."""
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("TsuminoRandom")
    assert ret is not ""


async def test_xbooru_random(event_loop):
    """tests xbooru's random."""
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("XbooruRandom")
    assert ret is not ""


async def test_xbooru_search(event_loop):
    """tests xbooru's search."""
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("XbooruSearch", args="test")
    assert ret is not ""


async def test_yandere_random(event_loop):
    """tests yandere's random."""
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("YandereRandom")
    assert ret is not ""


async def test_yandere_search(event_loop):
    """tests yandere's search."""
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("YandereSearch", args="test")
    assert ret is not ""
