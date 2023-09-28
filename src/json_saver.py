import json


class JsonSaver:
    """
    Класс сохранения вакансий в json файл.
    """
    def json_save_file(self, vacancies):
        vacansy_list = []
        for vacancy in vacancies:
            test = {
                'Профессия': vacancy.title,
                'Ссылка на вакансию': vacancy.url,
                'Средняя заработная плата': vacancy.salary,
                'Требование': vacancy.requirements,
            }

            vacansy_list.append(test)

        with open('src/test.json', 'w', encoding='utf-8') as f:
            json.dump(vacansy_list, f, ensure_ascii=False, indent=4)

    @staticmethod
    def get_all_vac_from_json():
        with open('src/test.json', encoding='utf-8') as f:
            all_vacancies = json.load(f)
            return all_vacancies
