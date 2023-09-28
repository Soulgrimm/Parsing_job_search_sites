class ChangeAttributesSJ:
    """
    Класс меняющий ключи вакансий SJ на ключи HH.
    """

    @staticmethod
    def change_name_key(vacancies_sj: list[dict]):
        vacancies = []
        for vacansy in vacancies_sj:
            vacancies.append({
                'name': vacansy['profession'],
                'alternate_url': vacansy['link'],
                'salary': {'from': vacansy['payment_from'], 'to': vacansy['payment_to']},
                'snippet': {'requirement': vacansy['candidat']}
            })
        return vacancies
