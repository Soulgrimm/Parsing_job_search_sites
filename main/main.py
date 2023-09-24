from pprint import pprint

from src.vacancies_from_API import HeadHunterAPI, SuperJobApi

# Создание экземпляра класса для работы с API
hh_api = HeadHunterAPI()
sj_api = SuperJobApi()

# Получение вакансий с HeadHunter и SuperJob
hh_vacancy = hh_api.get_vacancy()
sj_vacancy = sj_api.get_vacancy()



def main():
    pass


if __name__ == '__main__':
    main()
