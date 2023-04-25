CREATE TABLE IF NOT EXISTS companies(
    company_id INT PRIMARY KEY,
    company_name VARCHAR UNIQUE NOT NULL)

CREATE TABLE IF NOT EXISTS vacancies(
    vacancy_id INT PRIMARY KEY,
    company_id INT NOT NULL,
    vacancy_name VARCHAR NOT NULL,
    vacancy_url VARCHAR NOT NULL,
    salary INT,
    city VARCHAR NOT NULL,
    published_date DATE NOT NULL,
    company_name VARCHAR NOT NULL)

ALTER TABLE vacancies ADD CONSTRAINT fk_company_name FOREIGN KEY(company_name) REFERENCES companies(company_name)