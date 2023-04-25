from dbmanager import DBManager
from hhclass import HH


def main():
    # Создаем экземпляр класса DBManager
    db = DBManager()

    # Создаем экземпляр класса HH и передаем ID работодателя
    hh = HH()

    # Получаем вакансии и сохраняем в базу данных
    vacancies = hh.get_vacancies()
    db.save_vacancies(vacancies)

    # Получаем список компаний и количество вакансий у каждой компании
    companies_vacancies_count = db.get_companies_and_vacancies_count()
    print("Количество вакансий у каждой компании:")
    for row in companies_vacancies_count:
        print(row[0], "-", row[1])

    # Получаем список всех вакансий
    all_vacancies = db.get_all_vacancies()
    print("Список всех вакансий:")
    for row in all_vacancies:
        print(row)

    # Получаем среднюю зарплату по всем вакансиям
    avg_salary = db.get_avg_salary()
    print("Средняя зарплата по всем вакансиям:", avg_salary)

    # Получаем список вакансий с зарплатой выше средней
    high_salary_vacancies = db.get_vacancies_with_higher_salary()
    print("Список вакансий с зарплатой выше средней:")
    for row in high_salary_vacancies:
        print(row[0])

    # Получаем список вакансий, содержащих ключевое слово
    keyword = "Python"
    vacancies_with_keyword = db.get_vacancies_with_keyword(keyword)
    print(f"Список вакансий, содержащих ключевое слово '{keyword}':")
    for row in vacancies_with_keyword:
        print(row[0], "-", row[1], "-", row[2], "-", row[3])


if __name__ == '__main__':
    main()