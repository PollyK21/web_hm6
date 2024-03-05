import sqlite3


def query(file_number):
    # читаємо файл зі скриптом для створення БД
    file_name = f'query/query_{file_number}.sql'
    with open(file_name, 'r') as f:
        sql = f.read()

    # створюємо з'єднання з БД (якщо файлу з БД немає, він буде створений)
    with sqlite3.connect('progress.db') as con:
        cur = con.cursor()
        # виконуємо скрипт із файлу, який створить таблиці в БД
        cur.executescript(sql)
        cur.execute(sql)
        result = cur.fetchall()
        for row in result:
            print(row)

if __name__ == "__main__":
    # передаємо номер завдання
    query(1)