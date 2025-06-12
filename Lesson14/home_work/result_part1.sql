-- Тут sql для первой части задания
CREATE TABLE students
(
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    course TEXT DEFAULT 'Не назначен'
);
