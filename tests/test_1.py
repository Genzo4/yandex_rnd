import pytest
from urllib import request
from time import sleep
import re

from ya_music_rnd import YandexMusicRnd


def test_defaults():
    ymr = YandexMusicRnd()

    assert ymr.open_url is True
    assert ymr.max_index == 10000000
    assert ymr.max_iterations == 60
    assert ymr.find_clear == 'no'
    assert ymr.find_have_albom == 'all'
    assert ymr.find_have_similar == 'all'
    assert ymr.find_have_clips == 'all'
    assert ymr.show_progress is True
    assert ymr.quiet is False


def test_init_params():
    ymr = YandexMusicRnd(
        max_index = 123,
        open_url = False,
        max_iterations = 2,
        find_clear = 'all',
        find_have_albom = 'no',
        find_have_similar = 'yes',
        find_have_clips = 'no',
        show_progress = False,
        quiet = True
        )

    assert ymr.max_index == 123
    assert ymr.open_url is False
    assert ymr.max_iterations == 2
    assert ymr.find_clear == 'all'
    assert ymr.find_have_albom == 'no'
    assert ymr.find_have_similar == 'yes'
    assert ymr.find_have_clips == 'no'
    assert ymr.show_progress is False
    assert ymr.quiet is True


def test_check_filter_1():
    ymr = YandexMusicRnd()

    site = 'https://music.yandex.ru/artist/3255295'
    response = request.urlopen(site)
    html = response.read().decode(response.headers.get_content_charset())

    # ymr.find_clear = 'no'
    # ymr.find_have_albom = 'all'
    # ymr.find_have_similar = 'all'
    # ymr.find_have_clips = 'all'
    assert ymr.check_filter(html) is True

    test_table = [
        ['yes', 'all', 'all', 'all', False],
        ['no', 'yes', 'all', 'all', True],
        ['no', 'no', 'all', 'all', False],
        ['no', 'all', 'yes', 'all', False],
        ['no', 'all', 'no', 'all', True],
        ['no', 'yes', 'yes', 'all', False],
        ['no', 'yes', 'no', 'all', True],
        ['no', 'no', 'yes', 'all', False],
        ['no', 'no', 'no', 'all', False],
        ['no', 'all', 'all', 'yes', False],
        ['no', 'all', 'all', 'no', True],
        ['no', 'yes', 'all', 'yes', False],
        ['no', 'yes', 'all', 'no', True],
        ['no', 'no', 'all', 'yes', False],
        ['no', 'no', 'all', 'no', False],
        ['no', 'yes', 'yes', 'yes', False],
        ['no', 'yes', 'yes', 'no', False],
        ['no', 'no', 'no', 'yes', False],
        ['no', 'no', 'no', 'no', False],
        ['no', 'all', 'yes', 'yes', False],
        ['no', 'all', 'yes', 'no', False],
        ['no', 'all', 'no', 'yes', False],
        ['no', 'all', 'no', 'no', True],
        ['no', 'yes', 'no', 'yes', False],
        ['no', 'yes', 'no', 'no', True],
        ['no', 'no', 'yes', 'yes', False],
        ['no', 'no', 'yes', 'no', False],
    ]

    for t in test_table:

        ymr.find_clear = t[0]
        ymr.find_have_albom = t[1]
        ymr.find_have_similar = t[2]
        ymr.find_have_clips = t[3]

        assert ymr.check_filter(html) == t[4]

    sleep(1)


def test_check_filter_2():
    ymr = YandexMusicRnd()

    site = 'https://music.yandex.ru/artist/4255295'
    response = request.urlopen(site)
    html = response.read().decode(response.headers.get_content_charset())

    assert ymr.check_filter(html) is False

    ymr.find_clear = 'yes'
    ymr.find_have_albom = 'yes'
    ymr.find_have_similar = 'yes'
    ymr.find_have_clips = 'yes'
    assert ymr.check_filter(html) is True

    sleep(1)


def test_check_filter_3():
    ymr = YandexMusicRnd()

    site = 'https://music.yandex.ru/artist/2825481'
    response = request.urlopen(site)
    html = response.read().decode(response.headers.get_content_charset())

    # ymr.find_clear = 'no'
    # ymr.find_have_albom = 'all'
    # ymr.find_have_similar = 'all'
    # ymr.find_have_clips = 'all'
    assert ymr.check_filter(html) is True

    test_table = [
        ['yes', 'all', 'all', 'all', False],
        ['no', 'yes', 'all', 'all', True],
        ['no', 'no', 'all', 'all', False],
        ['no', 'all', 'yes', 'all', True],
        ['no', 'all', 'no', 'all', False],
        ['no', 'yes', 'yes', 'all', True],
        ['no', 'yes', 'no', 'all', False],
        ['no', 'no', 'yes', 'all', False],
        ['no', 'no', 'no', 'all', False],
        ['no', 'all', 'all', 'yes', False],
        ['no', 'all', 'all', 'no', True],
        ['no', 'yes', 'all', 'yes', False],
        ['no', 'yes', 'all', 'no', True],
        ['no', 'no', 'all', 'yes', False],
        ['no', 'no', 'all', 'no', False],
        ['no', 'yes', 'yes', 'yes', False],
        ['no', 'yes', 'yes', 'no', True],
        ['no', 'no', 'no', 'yes', False],
        ['no', 'no', 'no', 'no', False],
        ['no', 'all', 'yes', 'yes', False],
        ['no', 'all', 'yes', 'no', True],
        ['no', 'all', 'no', 'yes', False],
        ['no', 'all', 'no', 'no', False],
        ['no', 'yes', 'no', 'yes', False],
        ['no', 'yes', 'no', 'no', False],
        ['no', 'no', 'yes', 'yes', False],
        ['no', 'no', 'yes', 'no', False],
    ]

    for t in test_table:

        ymr.find_clear = t[0]
        ymr.find_have_albom = t[1]
        ymr.find_have_similar = t[2]
        ymr.find_have_clips = t[3]

        assert ymr.check_filter(html) == t[4]

    sleep(1)


def test_check_filter_4():
    ymr = YandexMusicRnd()

    site = 'https://music.yandex.ru/artist/4705290'
    response = request.urlopen(site)
    html = response.read().decode(response.headers.get_content_charset())

    # ymr.find_clear = 'no'
    # ymr.find_have_albom = 'all'
    # ymr.find_have_similar = 'all'
    # ymr.find_have_clips = 'all'
    assert ymr.check_filter(html) is True

    test_table = [
        ['yes', 'all', 'all', 'all', False],
        ['no', 'yes', 'all', 'all', False],
        ['no', 'no', 'all', 'all', True],
        ['no', 'all', 'yes', 'all', False],
        ['no', 'all', 'no', 'all', True],
        ['no', 'yes', 'yes', 'all', False],
        ['no', 'yes', 'no', 'all', False],
        ['no', 'no', 'yes', 'all', False],
        ['no', 'no', 'no', 'all', True],
        ['no', 'all', 'all', 'yes', True],
        ['no', 'all', 'all', 'no', False],
        ['no', 'yes', 'all', 'yes', False],
        ['no', 'yes', 'all', 'no', False],
        ['no', 'no', 'all', 'yes', True],
        ['no', 'no', 'all', 'no', False],
        ['no', 'yes', 'yes', 'yes', False],
        ['no', 'yes', 'yes', 'no', False],
        ['no', 'no', 'no', 'yes', True],
        ['no', 'no', 'no', 'no', False],
        ['no', 'all', 'yes', 'yes', False],
        ['no', 'all', 'yes', 'no', False],
        ['no', 'all', 'no', 'yes', True],
        ['no', 'all', 'no', 'no', False],
        ['no', 'yes', 'no', 'yes', False],
        ['no', 'yes', 'no', 'no', False],
        ['no', 'no', 'yes', 'yes', False],
        ['no', 'no', 'yes', 'no', False],
    ]

    for t in test_table:

        ymr.find_clear = t[0]
        ymr.find_have_albom = t[1]
        ymr.find_have_similar = t[2]
        ymr.find_have_clips = t[3]

        assert ymr.check_filter(html) == t[4]

    sleep(1)


def test_get_artist():
    ymr = YandexMusicRnd()

    site_1 = ymr.get_artist(False)

    assert len(re.findall('https://music.yandex.ru/artist/', site_1)) == 1

    site_2 = ymr.get_artist(False)

    assert site_1 != site_2

