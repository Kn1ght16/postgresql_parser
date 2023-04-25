import requests


class HH():
    API_HH = 'https://api.hh.ru/employers/'

    def __init__(self):
        self.params = {'area': 113, 'page': 1, 'per_page': 100, "only_with_salary": True,
                       "only_with_vacancies": True, 'text': 'python'}

    def get_vacancies(self):
        vacancies_url = f'https://api.hh.ru/vacancies/'
        response = requests.get(vacancies_url, params=self.params)
        if response.status_code == 200:
            return response.json()['items']
        else:
            return None