import random
from urllib import request, error
from time import sleep
from webbrowser import open
import re


class YandexMusicRnd:

    def __init__(self, max_int: int = 10000000, open_url: bool = True):
        self.max_int = max_int
        self.open_url = open_url

    def get_artist(self, open_url: bool = None) -> str:
        """

        :param open_url: Bool|None
        :return: Site url
        """

        if open_url is None:
            open_url = self.open_url

        found = False
        while not found:
            n = random.randint(1, self.max_int)
            site = f'https://music.yandex.ru/artist/{n}'
            # site = f'https://music.yandex.ru/artist/3255295'
            # site = f'https://music.yandex.ru/artist/4255295'
            # print(site)
            found = True
            try:
                response = request.urlopen(site)
            except error.HTTPError as e:
                print(e.code)
                if e.code == 404:
                    found = False
            else:
                if self.check_clear_page(response):
                    found = False

            sleep(1)

        if open_url:
            open(site)

        return site

    @staticmethod
    def check_clear_page(response) -> bool:
        """
        Check is music on page
        :param response:
        :return: Bool
        """
        html = response.read().decode(response.headers.get_content_charset())
        if len(re.findall('Главное', html)) < 2:
            return True

        return False

    @property
    def max_int(self) -> int:
        return self.__max_int

    @max_int.setter
    def max_int(self, max_int: int):
        self.__max_int = max_int

    @property
    def open_url(self) -> bool:
        return self.__open_url

    @open_url.setter
    def open_url(self, open_url: bool):
        self.__open_url = open_url
