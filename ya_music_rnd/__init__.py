import random
from urllib import request, error
from time import sleep
from webbrowser import open


class YandexMusicRnd:

    def __init__(self, max_int=10000000):
        self.max_int = max_int

    def get_artist(self, open_url: bool = True) -> str:
        found = False
        while not found:
            n = random.randint(1, self.max_int)
            site = f'https://music.yandex.ru/artist/{n}'
            # print(site)
            # site = f'https://music.yandex.ru/artist/3255295'
            found = True
            try:
                r = request.urlopen(site)
            except error.HTTPError as e:
                print(e.code)
                if e.code == 404:
                    found = False

            sleep(1)

        if open_url:
            open(site)

        return site

    @property
    def max_int(self) -> int:
        return self.__max_int

    @max_int.setter
    def max_int(self, max_int: int):
        self.__max_int = max_int
