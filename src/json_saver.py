import json


class JsonSaver:

    def json_save_file(self, data):
        with open(data, 'w', encoding='utf-8') as f:
            json.dump(data, f)

    def add_vacancy(self):
        pass

    def get_vacancy_by_salary(self):
        pass

    def delete_vacancy(self):
        pass