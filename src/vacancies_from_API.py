from abc import ABC, abstractmethod
import requests
import json
import os


class ApiJobSites(ABC):

    @abstractmethod
    def get_vacancy(self):
        pass


class HeadHunterAPI(ApiJobSites):
    HH_API = 'https://api.hh.ru/vacancies'

    def __init__(self):
        self.params = {
            'text': 'NAME:Python',
            'area': '1',
            'per_page': 50,
        }

    def get_vacancy(self):
        req = requests.get(self.HH_API, self.params)
        data = req.content.decode()
        json_ = json.loads(data)['items']
        return json_


class SuperJobApi(ApiJobSites):
    SJ_TOKEN = 'v3.r.137842005.f44f0a409ab4258b573222ef0f012d62aa7e8944.0880308108dd4c9628b6133b5499382d1c338a6e'
    # SJ_TOKEN: str = os.getenv('YT_API_KEY')
    SJ_API = 'https://api.superjob.ru/2.0/vacancies/'

    def __init__(self):
        self.params = {
            'keyword': 'python',
            'count': 50,
            'town': 'Москва',
        }

    def get_vacancy(self):
        headers = {
            'X-Api-App-Id': self.SJ_TOKEN
        }
        req = requests.get(self.SJ_API, headers=headers, params=self.params)
        data = req.content.decode()
        json_ = json.loads(data)
        return json_
