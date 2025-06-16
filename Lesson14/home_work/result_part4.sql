from connection1 import Connect
from pathlib import Path
from typing import Optional


class Student:
    DB_FILE = Path("student.db")
    def __init__(self, student_id, first_name, last_name, email, course):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.course = course

    def __repr__(self):
        return f"Student (id = {self.student_id}, first_name {self.first_name}, last_name {self.last_name}, email {self.email}, course {self.course})"

class StudentData:
    DB_FILE = Path("student.db")

    @classmethod
    def _ensure_db_table_exists(cls):
        with Connect(cls.DB_FILE) as cursor:
            sql_create = '''
                CREATE TABLE IF NOT EXISTS students 
                (
                student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT UNIQUE,
                course TEXT DEFAULT 'Не назначен'
                );
            '''
            cursor.execute(sql_create)

    @classmethod
    def email_exist(cls, email: str) -> bool:
        cls._ensure_db_table_exists()
        sql_check = "SELECT 1 FROM students WHERE email=?"
        with Connect(cls.DB_FILE) as coursor:
            coursor.execute(sql_check, (email,))
            return coursor.fetchone() is not None

    @classmethod
    def add_student(cls, first_name: str, last_name: str, email: str, course: Optional[str] = None):
        cls._ensure_db_table_exists()
        if email is not None and cls.email_exist(email):
            print(f"Email '{email}' уже существует в базе данных. Студент не добавлен.")
            return

        sql_insert = "INSERT INTO students (first_name, last_name, email, course) VALUES(?,?,?,?)"
        with Connect(cls.DB_FILE) as cursor:
            cursor.execute(sql_insert, (first_name, last_name, email, course))

    @classmethod
    def select_student(cls, sql : str, param: tuple = ()) ->list[tuple]:
        with Connect(cls.DB_FILE) as cursor:
            cursor.execute(sql, param)
            return cursor.fetchall()

    @classmethod
    def update_student(cls, student_id: int,
                       first_name: Optional[str] = None,
                       last_name: Optional[str] = None,
                       email: Optional[str] = None,
                       course: Optional[str] = None):
        cls._ensure_db_table_exists()

        fields = []
        param = []

        if first_name is not None:
            fields.append("first_name=?")
            param.append(first_name)
        if last_name is not None:
            fields.append("last_name=?")
            param.append(last_name)
        if email is not None:
            fields.append("email=?")
            param.append(email)
        if course is not None:
            fields.append("course=?")
            param.append(course)

        if not fields:
            return

        sql_update = f'''
        UPDATE students
        SET {",".join(fields)}
        WHERE student_id=?
        '''
        param.append(student_id)

        with Connect(cls.DB_FILE) as cursor:
            cursor.execute(sql_update, tuple(param))



StudentData.add_student('Алексей', 'Воронов', 'alexey.voronov@example.com', 4)
StudentData.add_student('Елена', 'Кириллова', 'elena.kirillova@example.com', None)
StudentData.add_student('Максим', 'Зайцев', None, 2)
StudentData.add_student('Ольга', 'Новикова', None, None)
StudentData.add_student('Дмитрий', 'Соколов', 'dmitry.sokolov@example.com', 5)

all_students = StudentData.select_student("SELECT * FROM students")
names_emails = StudentData.select_student("SELECT first_name, last_name, email FROM students")
course_3_students = StudentData.select_student("SELECT * FROM students WHERE course LIKE '%Базы данных%' ORDER BY last_name ASC ")
count_by_course = StudentData.select_student("SELECT course, COUNT(*) AS student_count FROM students GROUP BY course")
student_by_part_email = StudentData.select_student("SELECT * FROM students WHERE email LIKE '%@example.com%'")

StudentData.update_student(1, course="Веб-разработка")
students = StudentData.select_student("SELECT student_id FROM students WHERE course=?", ("Не назначен",))
for student in students:
    student_id = student[0]
    StudentData.update_student(student_id, course="Введение в ИТ")

student = StudentData.select_student("SELECT student_id FROM students WHERE first_name=? AND last_name=?", ("Иван","Петров"))
if student:
    student_id = student[0][0]
    StudentData.update_student(student_id, email="ivan.petrov@newdomain.com")

student = StudentData.select_student("SELECT student_id FROM students WHERE email=?",("student3@example.com",))
if student:
    student_id = student[0][0]
    StudentData.update_student(student_id, last_name="Смирнов", course="Алгоритмы и структуры данных")

#Vladimir Ghilas
