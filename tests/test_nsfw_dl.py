import pytest

import nsfw_dl


def test_fake_loader():
    """tests the NSFWDL class."""
    with pytest.raises(nsfw_dl.errors.NoLoader):
        with nsfw_dl.NSFWDL() as dl:
            dl.download("fake_loader", args="rating:e")


def test_danbooru_random():
    """tests danbooru's random."""
    with nsfw_dl.NSFWDL() as dl:
        img = dl.download("DanbooruRandom")
    assert img is not ""


@pytest.mark.asyncio
async def test_danbooru_async():
    """ ONLY ASYNC TEST """
    async with nsfw_dl.NSFWDL() as dl:
        img = await dl.download("DanbooruRandom")
    assert img is not ""

# TODO: Redo all of these below
"""
async def test_danbooru_search(event_loop):
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("DanbooruSearch", args="rating:e")
    assert ret is not ""


async def test_drunkenpumken_random(event_loop):
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("DrunkenpumkenRandom")
    assert ret is not ""


async def test_e621_random(event_loop):
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("E621Random")
    assert ret is not ""


async def test_e621_search(event_loop):
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("E621Search", args="rating:e")
    assert ret is not ""


async def test_furrybooru_random(event_loop):
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("FurrybooruRandom")
    assert ret is not ""


async def test_furrybooru_search(event_loop):
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("FurrybooruSearch", args="rating:e")
    assert ret is not ""


async def test_gelbooru_random(event_loop):
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("GelbooruRandom")
    assert ret is not ""


async def test_gelbooru_search(event_loop):
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("GelbooruSearch", args="rating:e")
    assert ret is not ""


async def test_hbrowse_random(event_loop):
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("HbrowseRandom")
    assert ret is not ""


async def test_konachan_random(event_loop):
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("KonachanRandom")
    assert ret is not ""


async def test_konachan_search(event_loop):
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("KonachanSearch", args="rating:e")
    assert ret is not ""


async def test_lolibooru_random(event_loop):
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("LolibooruRandom")
    assert ret is not ""


async def test_lolibooru_search(event_loop):
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("LolibooruSearch", args="rating:e")
    assert ret is not ""


async def test_nhentai_random(event_loop):
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("NhentaiRandom")
    assert ret is not ""


async def test_rule34_random(event_loop):
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("Rule34Random")
    assert ret is not ""


async def test_rule34_search(event_loop):
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("Rule34Search", args="rating:e")
    assert ret is not ""


async def test_tbib_random(event_loop):
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("TbibRandom")
    assert ret is not ""


async def test_tbib_search(event_loop):
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("TbibSearch", args="rating:e")
    assert ret is not ""


async def test_tsumino_random(event_loop):
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("TsuminoRandom")
    assert ret is not ""


async def test_xbooru_random(event_loop):
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("XbooruRandom")
    assert ret is not ""


async def test_xbooru_search(event_loop):
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("XbooruSearch", args="rating:e")
    assert ret is not ""


async def test_yandere_random(event_loop):
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("YandereRandom")
    assert ret is not ""


async def test_yandere_search(event_loop):
    _nsfwdl = nsfw_dl.NSFWDL(loop=event_loop)
    ret = await _nsfwdl.download("YandereSearch", args="rating:e")
    assert ret is not ""
"""
