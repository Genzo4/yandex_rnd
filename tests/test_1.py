import pytest
from urllib import request
from time import sleep
import re

from ya_music_rnd import YandexMusicRnd


def test_defaults():
    ymr = YandexMusicRnd()

    assert ymr.open_url is True
    assert ymr.max_index == 10000000


def test_init_1():
    ymr = YandexMusicRnd(123)

    assert ymr.open_url is True
    assert ymr.max_index == 123


def test_init_2():
    ymr = YandexMusicRnd(23, False)

    assert ymr.open_url is False
    assert ymr.max_index == 23


def test_init_3():
    ymr = YandexMusicRnd(open_url=False, max_index=587)

    assert ymr.open_url is False
    assert ymr.max_index == 587


def test_setters_getters():
    ymr = YandexMusicRnd()

    ymr.max_index = 235
    ymr.open_url = False

    assert ymr.open_url is False
    assert ymr.max_index == 235


def test_check_clear_page():
    ymr = YandexMusicRnd()

    site = 'https://music.yandex.ru/artist/3255295'
    response = request.urlopen(site)

    assert ymr.check_clear_page(response) is False

    sleep(1)

    site = 'https://music.yandex.ru/artist/4255295'
    response = request.urlopen(site)

    assert ymr.check_clear_page(response) is True


def test_get_artist():
    ymr = YandexMusicRnd()

    site_1 = ymr.get_artist(False)

    assert len(re.findall('https://music.yandex.ru/artist/', site_1)) == 1

    site_2 = ymr.get_artist(False)

    assert site_1 != site_2

