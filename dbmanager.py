import psycopg2
import os


class DBManager:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                host="localhost",
                dbname="vacansies",
                user="postgres",
                password=os.getenv('PSQL_pass')
            )
        except psycopg2.Error as e:
            print("Не удается подключиться к базе данных.")
            print(e)

    def get_companies_and_vacancies_count(self):
        cur = self.conn.cursor()
        cur.execute("""
            SELECT company_name, COUNT(*) AS vacancies_count 
            FROM vacancies 
            GROUP BY company_name;
        """)
        result = cur.fetchall()
        cur.close()
        return result

    def get_all_vacancies(self):
        cur = self.conn.cursor()
        cur.execute("""
            SELECT * 
            FROM vacancies;
        """)
        result = cur.fetchall()
        cur.close()
        return result

    def get_avg_salary(self):
        cur = self.conn.cursor()
        cur.execute("""
            SELECT AVG(salary) 
            FROM vacancies;
        """)
        result = cur.fetchone()[0]
        cur.close()
        return result

    def get_vacancies_with_higher_salary(self):
        avg_salary = self.get_avg_salary()
        cur = self.conn.cursor()
        cur.execute(f"""
            SELECT vacancy_name
            FROM vacancies 
            WHERE salary > (SELECT avg(salary) FROM vacancies)
        """)
        result = cur.fetchall()
        cur.close()
        return result

    def get_vacancies_with_keyword(self, keyword):
        cur = self.conn.cursor()
        cur.execute(f"""
            SELECT company_name, vacancy_name, salary
            FROM vacancies 
            WHERE vacancy_name LIKE '%{keyword}%';
        """)
        result = cur.fetchall()
        cur.close()
        return result

    def save_vacancies(self, vacancies):
        cur = self.conn.cursor()
        for vacancy in vacancies:
            cur.execute("""
                INSERT INTO companies (company_id, company_name)
                VALUES (%s, %s)
                ON CONFLICT (company_id) DO NOTHING;
            """, (
                vacancy['employer']['id'], vacancy['employer']['name']
            ))
            cur.execute("""
                INSERT INTO vacancies (vacancy_id, company_id, vacancy_name, vacancy_url, salary, city, published_date,  company_name)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (vacancy_id) DO UPDATE
                SET vacancy_id = excluded.vacancy_id, company_id = excluded.company_id,
                    vacancy_name = excluded.vacancy_name, vacancy_url = excluded.vacancy_url, 
                    salary = excluded.salary, city = excluded.city, 
                    published_date = excluded.published_date, company_name = excluded.company_name;
            """, (
                vacancy['id'], vacancy['employer']['id'], vacancy['name'], vacancy['alternate_url'], vacancy['salary']['from'],
                vacancy['area']['name'], vacancy['published_at'], vacancy['employer']['name']
            ))
        self.conn.commit()
        cur.close()