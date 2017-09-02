import pytest

import nsfw_dl


def test_fake_loader():
    """tests the NSFWDL class."""
    with pytest.raises(nsfw_dl.errors.NoLoader):
        with nsfw_dl.NSFWDL() as dl:
            dl.download("fake_loader", args="1girl")


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


def test_danbooru_search():
    with nsfw_dl.NSFWDL() as dl:
        img = dl.download("DanbooruSearch", args="1girl")
        assert img is not ""


def test_drunkenpumken_random():
    with nsfw_dl.NSFWDL() as dl:
        img = dl.download("DrunkenpumkenRandom")
        assert img is not ""


def test_e621_random():
    with nsfw_dl.NSFWDL() as dl:
        img = dl.download("E621Random")
        assert img is not ""


def test_e621_search():
    with nsfw_dl.NSFWDL() as dl:
        img = dl.download("E621Search", args="1girl")
        assert img is not ""


def test_furrybooru_random():
    with nsfw_dl.NSFWDL() as dl:
        img = dl.download("FurrybooruRandom")
        assert img is not ""


def test_furrybooru_search():
    with nsfw_dl.NSFWDL() as dl:
        img = dl.download("FurrybooruSearch", args="1girl")
        assert img is not ""


def test_gelbooru_random():
    with nsfw_dl.NSFWDL() as dl:
        img = dl.download("GelbooruRandom")
        assert img is not ""


def test_gelbooru_search():
    with nsfw_dl.NSFWDL() as dl:
        img = dl.download("GelbooruSearch", args="1girl")
        assert img is not ""


def test_hbrowse_random():
    with nsfw_dl.NSFWDL() as dl:
        img = dl.download("HbrowseRandom")
        assert img is not ""


def test_konachan_random():
    with nsfw_dl.NSFWDL() as dl:
        img = dl.download("KonachanRandom")
        assert img is not ""


def test_konachan_search():
    with nsfw_dl.NSFWDL() as dl:
        img = dl.download("KonachanSearch", args="1girl")
        assert img is not ""


def test_lolibooru_random():
    with nsfw_dl.NSFWDL() as dl:
        img = dl.download("LolibooruRandom")
        assert img is not ""


def test_lolibooru_search():
    with nsfw_dl.NSFWDL() as dl:
        img = dl.download("LolibooruSearch", args="1girl")
        assert img is not ""


def test_nhentai_random():
    with nsfw_dl.NSFWDL() as dl:
        img = dl.download("NhentaiRandom")
        assert img is not ""


def test_rule34_random():
    with nsfw_dl.NSFWDL() as dl:
        img = dl.download("Rule34Random")
        assert img is not ""


def test_rule34_search():
    with nsfw_dl.NSFWDL() as dl:
        img = dl.download("Rule34Search", args="1girl")
        assert img is not ""


def test_tbib_random():
    with nsfw_dl.NSFWDL() as dl:
        img = dl.download("TbibRandom")
        assert img is not ""


def test_tbib_search():
    with nsfw_dl.NSFWDL() as dl:
        img = dl.download("TbibSearch", args="1girl")
        assert img is not ""


def test_tsumino_random():
    with nsfw_dl.NSFWDL() as dl:
        img = dl.download("TsuminoRandom")
        assert img is not ""


def test_xbooru_random():
    with nsfw_dl.NSFWDL() as dl:
        img = dl.download("XbooruRandom")
        assert img is not ""


def test_xbooru_search():
    with nsfw_dl.NSFWDL() as dl:
        img = dl.download("XbooruSearch", args="1girl")
        assert img is not ""


def test_yandere_random():
    with nsfw_dl.NSFWDL() as dl:
        img = dl.download("YandereRandom")
        assert img is not ""


def test_yandere_search():
    with nsfw_dl.NSFWDL() as dl:
        img = dl.download("YandereSearch", args="1girl")
        assert img is not ""
