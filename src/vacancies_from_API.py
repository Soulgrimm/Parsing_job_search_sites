from abc import ABC, abstractmethod
import requests
import json
import os

SJ_TOKEN: str = os.getenv('SJ_TOKEN')


class ApiJobSites(ABC):
    """
    Абстрактный класс для работы с API сайтов.
    """

    @abstractmethod
    def get_vacancy(self):
        """
        Получение вакансий с НН и SJ по API.
        :param keyword: Слово для поиска вакансий.
        :return: список вакансий.
        """
        pass


class HeadHunterAPI(ApiJobSites):
    HH_API = 'https://api.hh.ru/vacancies'

    def __init__(self, keyword: str):
        self.params: dict = {
            'text': keyword,
            'area': '1',
            'per_page': 50,
        }

    def get_vacancy(self):
        req = requests.get(self.HH_API, self.params)
        data = req.content.decode()
        json_data = json.loads(data)['items']
        return json_data


class SuperJobApi(ApiJobSites):
    SJ_API = 'https://api.superjob.ru/2.0/vacancies/'

    def __init__(self, keyword: str):
        self.params: dict = {
            'keyword': keyword,
            'count': 50,
            'town': 'Москва',
        }

    def get_vacancy(self):
        headers = {
            'X-Api-App-Id': SJ_TOKEN
        }
        req = requests.get(self.SJ_API, headers=headers, params=self.params)
        data = req.content.decode()
        json_data = json.loads(data)['objects']
        return json_data
