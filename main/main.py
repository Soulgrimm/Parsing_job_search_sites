from pprint import pprint
from src.vacancies_from_api import HeadHunterAPI, SuperJobApi
from src.vacancy import Vacancy
from src.json_saver import JsonSaver
from src.change_attr_vac_sj import ChangeAttributesSJ


def main():
    vacancies = []

    while True:
        user_choice_platform = int(input(
            'Выберите платформу для поиска вакансий:\n'
            '1 - HeahHunter \n'
            '2 - SuperJob\n'
            '3 - Выход\n'))

        if user_choice_platform == 3:
            break

        user_keyword = input('Введите слово для поиска вакансий: ')

        # Создание экземпляр класса для работы с API HH, получение вакансий HH
        if user_choice_platform == 1:

            hh_api = HeadHunterAPI(user_keyword)
            hh_vacancies = hh_api.get_vacancy()

            for vacancy in hh_vacancies:
                vacancies_objects = Vacancy(vacancy)
                vacancies.append(vacancies_objects)

        # Создание экземпляр класса для работы с API JJ, получение вакансий SJ
        elif user_choice_platform == 2:

            sj_api = SuperJobApi(user_keyword)
            sj_vacancies = sj_api.get_vacancy()
            vac_sj_change_attr = ChangeAttributesSJ.change_name_key(sj_vacancies)

            for vacancy in vac_sj_change_attr:
                vacancies_objects = Vacancy(vacancy)
                vacancies.append(vacancies_objects)

        # Сохранение вакансий в файл json
        json_save = JsonSaver()
        json_save.json_save_file(vacancies=vacancies)

        # Получение вакансий из json файла
        all_vacancies = JsonSaver.get_all_vac_from_json()

        while True:
            user_choice_action = int(input('\nВыберите действие:\n'
                                           '1 - Показать все вакансии.\n'
                                           '2 - Получить все вакансии по ключевому слову.\n'
                                           '3 - Получить вакансии с заработной платой выше указанной.\n'
                                           '4 - Выход.\n'))

            if user_choice_action == 1:
                for vacancy in all_vacancies:
                    print()
                    for key, values in vacancy.items():
                        print('{}: {}'.format(key, values))

            elif user_choice_action == 2:
                user_filter_word = input('Введите ключевое слово: \n')
                for vacancy in all_vacancies:
                    print()
                    if user_filter_word in vacancy['Профессия'] or user_filter_word in vacancy['Требование']:
                        for key, values in vacancy.items():
                            print('{}: {}'.format(key, values))
                    else:
                        continue

            elif user_choice_action == 3:
                user_input_salary = int(input('Введите зарплату: '))
                for vacancy in vacancies:
                    if type(vacancy.salary) is str:
                        continue
                    if user_input_salary <= vacancy.salary:
                        print(vacancy)

            elif user_choice_action == 4:
                break


if __name__ == '__main__':
    main()
