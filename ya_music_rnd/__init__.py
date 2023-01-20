import random
from urllib import request, error
from time import sleep
from webbrowser import open
import re


class YandexMusicRnd:

    def __init__(self,
                 max_index: int = 10000000,
                 open_url: bool = True,
                 max_iterations: int = 60,
                 find_clear: str = 'no',
                 find_have_albom: str = 'all',
                 find_have_similar: str = 'all',
                 quiet: bool = False
                 ):
        """
        Init class
        :param max_index:
        :param open_url:
        :param max_iterations:
        :param find_clear:
        :param find_have_albom:
        :param find_have_similar:
        :param quiet:
        """

        self.max_index = max_index
        self.open_url = open_url
        self.max_iterations = max_iterations
        self.cur_iteration = 0
        self.find_clear = find_clear
        self.find_have_albom = find_have_albom
        self.find_have_similar = find_have_similar
        self.quiet = quiet

    def get_artist(self, open_url: bool = None) -> str:
        """

        :param open_url:
        :return: Site url
        """

        if open_url is None:
            open_url = self.open_url

        found = False
        while not found:
            if self.cur_iteration >= self.max_iterations:
                break

            self.cur_iteration += 1

            index = random.randint(1, self.max_index)

            site = f'https://music.yandex.ru/artist/{index}'

            self.show_progress(site)

            found = True
            try:
                response = request.urlopen(site)
            except error.HTTPError as e:
                if e.code == 404:
                    found = False
            else:
                if self.check_clear_page(response):
                    found = False

            sleep(1)

        if found:
            if open_url:
                open(site)
        else:
            print(f'За максимальное количество итераций ({self.max_iterations}) результат не найден.')
            site = ''

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

    def show_progress(self, site: str) -> None:
        """
        Show progress
        :param site: Current site url
        :return: None
        """
        print(f'{site} [{self.cur_iteration}/{self.max_iterations}]')

    @property
    def max_index(self) -> int:
        return self.__max_index

    @max_index.setter
    def max_index(self, max_index: int):
        self.__max_index = max_index

    @property
    def open_url(self) -> bool:
        return self.__open_url

    @open_url.setter
    def open_url(self, open_url: bool):
        self.__open_url = open_url

    @property
    def max_iterations(self) -> int:
        return self.__max_iterations

    @max_iterations.setter
    def max_iterations(self, max_iterations: int):
        self.__max_iterations = max_iterations

    @property
    def quiet(self) -> bool:
        return self.__quiet

    @quiet.setter
    def quiet(self, quiet: bool):
        self.__quiet = quiet

    @property
    def find_have_albom(self) -> str:
        return self.__find_have_albom

    @find_have_albom.setter
    def find_have_albom(self, find_have_albom: str):
        self.__find_have_albom = find_have_albom

    @property
    def find_have_similar(self) -> str:
        return self.__find_have_similar

    @find_have_similar.setter
    def find_have_similar(self, find_have_similar: str):
        self.__find_have_similar = find_have_similar

    @property
    def find_clear(self) -> str:
        return self.__find_clear

    @find_clear.setter
    def find_clear(self, find_clear: str):
        self.__find_clear = find_clear
