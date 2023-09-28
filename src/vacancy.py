class Vacancy:
    """
    Класс для работы с вакансиями.
    """

    def __init__(self, vacancie):

        self.title: str = vacancie['name']
        self.url: str = vacancie['alternate_url']

        if vacancie['salary'] is None or vacancie['salary']['from'] == 0 and vacancie['salary']['to'] == 0:
            self.salary: str = 'Заработная плата не указана, вакансия не рекомендуется к просмотру'
        elif vacancie['salary']['from'] is None or vacancie['salary']['from'] == 0:
            self.salary: int = int(vacancie['salary']['to'])
        elif vacancie['salary']['to'] is None or vacancie['salary']['to'] == 0:
            self.salary: int = int(vacancie['salary']['from'])
        else:
            self.salary: int = int((vacancie['salary']['from'] + vacancie['salary']['to']) / 2)

        if vacancie['snippet']['requirement'] is None:
            self.requirements: str = 'Требования отсутствуют'
        else:
            self.requirements: str = vacancie['snippet']['requirement']

    def __str__(self):
        return (f'Профессия: {self.title}\n'
                f'Ссылка на вакансию: {self.url}\n'
                f'Заработная плата: {self.salary}\n'
                f'Требование: {self.requirements}\n')

    def __lt__(self, other):
        return self.salary < other.salary

    def __le__(self, other):
        return self.salary <= other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __ge__(self, other):
        return self.salary >= other.salary
