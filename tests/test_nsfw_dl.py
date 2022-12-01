import pytest

import nsfw_dl


@pytest.mark.asyncio
async def test_fake_loader():
    """tests the NSFWDL class."""
    with pytest.raises(nsfw_dl.errors.NoLoader):
        async with nsfw_dl.NSFWDL() as dl:
            await dl.download("fake_loader", args="1girl")


@pytest.mark.asyncio
async def test_danbooru_random():
    """tests danbooru's random."""
    async with nsfw_dl.NSFWDL() as dl:
        img = await dl.download("DanbooruRandom")
    assert img


@pytest.mark.asyncio
async def test_danbooru_search():
    async with nsfw_dl.NSFWDL() as dl:
        img = await dl.download("DanbooruSearch", args="1girl")
        assert img


@pytest.mark.asyncio
async def test_drunkenpumken_random():
    async with nsfw_dl.NSFWDL() as dl:
        img = await dl.download("DrunkenpumkenRandom")
        assert img


@pytest.mark.asyncio
async def test_e621_random():
    async with nsfw_dl.NSFWDL() as dl:
        img = await dl.download("E621Random")
        assert img


@pytest.mark.asyncio
async def test_e621_search():
    async with nsfw_dl.NSFWDL() as dl:
        img = await dl.download("E621Search", args="1girl")
        assert img


@pytest.mark.asyncio
@pytest.mark.xfail(reason="Broken, unknown how to fix.")
async def test_furrybooru_random():
    async with nsfw_dl.NSFWDL() as dl:
        img = await dl.download("FurrybooruRandom")
        assert img


@pytest.mark.asyncio
@pytest.mark.xfail(reason="Broken, unknown how to fix.")
async def test_furrybooru_search():
    async with nsfw_dl.NSFWDL() as dl:
        img = await dl.download("FurrybooruSearch", args="1girl")
        assert img


@pytest.mark.asyncio
async def test_gelbooru_random():
    async with nsfw_dl.NSFWDL() as dl:
        img = await dl.download("GelbooruRandom")
        assert img


@pytest.mark.asyncio
async def test_gelbooru_search():
    async with nsfw_dl.NSFWDL() as dl:
        img = await dl.download("GelbooruSearch", args="1girl")
        assert img


@pytest.mark.asyncio
async def test_hbrowse_random():
    async with nsfw_dl.NSFWDL() as dl:
        img = await dl.download("HbrowseRandom")
        assert img


@pytest.mark.asyncio
async def test_konachan_random():
    async with nsfw_dl.NSFWDL() as dl:
        img = await dl.download("KonachanRandom")
        assert img


@pytest.mark.asyncio
async def test_konachan_search():
    async with nsfw_dl.NSFWDL() as dl:
        img = await dl.download("KonachanSearch", args="2girls")
        assert img


@pytest.mark.asyncio
async def test_lolibooru_random():
    async with nsfw_dl.NSFWDL() as dl:
        img = await dl.download("LolibooruRandom")
        assert img


@pytest.mark.asyncio
async def test_lolibooru_search():
    async with nsfw_dl.NSFWDL() as dl:
        img = await dl.download("LolibooruSearch", args="1girl")
        assert img


"""
@pytest.mark.asyncio
async def test_nhentai_random():
    async with nsfw_dl.NSFWDL() as dl:
        img = await dl.download("NhentaiRandom")
        assert img
"""


@pytest.mark.asyncio
async def test_rule34_random():
    async with nsfw_dl.NSFWDL() as dl:
        img = await dl.download("Rule34Random")
        assert img


@pytest.mark.asyncio
async def test_rule34_search():
    async with nsfw_dl.NSFWDL() as dl:
        img = await dl.download("Rule34Search", args="1girl")
        assert img


@pytest.mark.asyncio
async def test_tbib_random():
    async with nsfw_dl.NSFWDL() as dl:
        img = await dl.download("TbibRandom")
        assert img


@pytest.mark.asyncio
async def test_tbib_search():
    async with nsfw_dl.NSFWDL() as dl:
        img = await dl.download("TbibSearch", args="1girl")
        assert img


@pytest.mark.asyncio
async def test_xbooru_random():
    async with nsfw_dl.NSFWDL() as dl:
        img = await dl.download("XbooruRandom")
        assert img


@pytest.mark.asyncio
async def test_xbooru_search():
    async with nsfw_dl.NSFWDL() as dl:
        img = await dl.download("XbooruSearch", args="1girl")
        assert img


@pytest.mark.asyncio
async def test_yandere_random():
    async with nsfw_dl.NSFWDL() as dl:
        img = await dl.download("YandereRandom")
        assert img


@pytest.mark.asyncio
async def test_yandere_search():
    async with nsfw_dl.NSFWDL() as dl:
        img = await dl.download("YandereSearch", args="1girl")
        assert img


def test_sync_instance():
    with pytest.raises(RuntimeError):
        with nsfw_dl.NSFWDL() as dl:
            dl.download("YandereRandom")
