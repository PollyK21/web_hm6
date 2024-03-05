from datetime import datetime, timedelta
import faker
from random import randint, choice
import random
import sqlite3

NUMBER_GROUPS = 3
NUMBER_STUDENTS = 30
NUMBER_SUBJECTS = 8
NUMBER_TEACHERS = 5
NUMBER_GRADES = 100


def generate_fake_data(number_groups, number_students, number_subjects, number_teachers) -> tuple():
    fake_groups = []  # тут зберігатимемо компанії
    fake_students = []  # тут зберігатимемо співробітників
    fake_subjects = []  # тут зберігатимемо посади
    fake_teachers = [] 

    fake_data = faker.Faker()

    # Створимо набори
    for _ in range(number_groups):
        fake_groups.append(fake_data.random_number(digits=6))

    for _ in range(number_students):
        fake_students.append(fake_data.name())

    # Та number_post набір посад
    for _ in range(number_subjects):
        fake_subjects.append(fake_data.job())

    for _ in range(number_teachers):
        fake_teachers.append(fake_data.name())

    return fake_groups, fake_students, fake_subjects, fake_teachers


def prepare_data(groups, students, subjects, teachers) -> tuple():
    for_groups = []
    # Готуємо список кортежів груп
    for group in groups:
        for_groups.append((group, ))

    for_students = []  # для таблиці stugent
    for st in students:
        '''
        Для записів у таблицю співробітників нам потрібно додати посаду та id компанії. Компаній у нас було за замовчуванням
        NUMBER_COMPANIES, при створенні таблиці companies для поля id ми вказували INTEGER AUTOINCREMENT - тому кожен
        запис отримуватиме послідовне число збільшене на 1, починаючи з 1. Тому компанію вибираємо випадково
        у цьому діапазоні
        '''
        for_students.append((st, randint(1, NUMBER_GROUPS)))

    for_teachers = []
    # Готуємо список кортежів груп
    for tea in teachers:
        for_teachers.append((tea, ))

    for_subjects = []
    for sub in subjects:
        for_subjects.append((sub, randint(1, NUMBER_TEACHERS)))

    for_marks = []
    student_ids = list(range(1, NUMBER_STUDENTS + 1))
    subject_ids = list(range(1, NUMBER_SUBJECTS + 1))
    for student in student_ids:
        grades = [random.randint(1, NUMBER_GRADES) for _ in range(20)]
        end_date = datetime.now().date()
        start_date = end_date - timedelta(days=365)
        random_days = random.randint(0, 365)
        random_date = start_date + timedelta(days=random_days)
        for grade in grades:
            for_marks.append((student, choice(subject_ids), grade, random_date))

    return for_groups, for_students, for_teachers, for_subjects, for_marks

# companies, employees, posts, sub, marks = prepare_data(*generate_fake_data(NUMBER_GROUPS, NUMBER_STUDENTS, NUMBER_SUBJECTS, NUMBER_TEACHERS))
# print(companies)
# print(employees)
# print(posts)
# print(sub)
# print(marks)


def insert_data_to_db(for_groups, for_students, for_teachers, for_subjects, for_marks) -> None:
    # Створимо з'єднання з нашою БД та отримаємо об'єкт курсору для маніпуляцій з даними

    with sqlite3.connect('progress.db') as con:

        cur = con.cursor()

        '''Заповнюємо таблицю компаній. І створюємо скрипт для вставлення, де змінні, які вставлятимемо, відзначимо
        знаком заповнювача (?) '''

        sql_to_groups = """INSERT INTO groups(group_code)
                               VALUES (?)"""
        cur.executemany(sql_to_groups, for_groups)


        sql_to_students = """INSERT INTO students(name, group_id)
                               VALUES (?, ?)"""
        cur.executemany(sql_to_students, for_students)


        sql_to_teacher = """INSERT INTO teachers(name)
                              VALUES (?)"""
        cur.executemany(sql_to_teacher, for_teachers)


        sql_to_subjects = """INSERT INTO subjects(name, teacher_id)
                              VALUES (?, ?)"""
        cur.executemany(sql_to_subjects, for_subjects)

        sql_to_marks = """INSERT INTO marks(student_id, subject_id, grade, date)
                              VALUES (?, ?, ?, ?)"""
        cur.executemany(sql_to_marks, for_marks)

        # Фіксуємо наші зміни в БД

        con.commit()


if __name__ == "__main__":
    groups, students, teachers, subjects, marks = prepare_data(*generate_fake_data(NUMBER_GROUPS, NUMBER_STUDENTS, NUMBER_SUBJECTS, NUMBER_TEACHERS))
    insert_data_to_db(groups, students, teachers, subjects, marks)