# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:


import sqlite3
conn = sqlite3.connect('teacher.db')
c = conn.cursor()
c.execute('''DROP TABLE IF EXISTS Schools''')
c.execute('''CREATE TABLE Schools (School_Id INTEGER PRIMARY KEY, School_Name TEXT)''')
c.execute("INSERT INTO Schools VALUES (1, 'Школа 1')")
c.execute("INSERT INTO Schools VALUES (2, 'Школа 2')")
c.execute("INSERT INTO Schools VALUES (3, 'Школа 3')")
c.execute("INSERT INTO Schools VALUES (4, 'Школа 4')")
conn.commit()

# Создание базы данных и таблицы
conn = sqlite3.connect('teacher.db')
c = conn.cursor()
c.execute('''DROP TABLE IF EXISTS Students''')
c.execute('''CREATE TABLE Students (Student_Id INTEGER PRIMARY KEY, Student_Name TEXT, School_Id INTEGER)''')
c.execute("INSERT INTO Students VALUES (201, 'Иван', 1)")
c.execute("INSERT INTO Students VALUES (202, 'Петр', 2)")
c.execute("INSERT INTO Students VALUES (203, 'Анастасия', 3)")
c.execute("INSERT INTO Students VALUES (204, 'Игорь', 4)")
conn.commit()

# Получение информации о студенте и школе по ID студента
def get_student_info(student_id):
    conn = sqlite3.connect('teacher.db')
    c = conn.cursor()
    c.execute(f"SELECT Student_Id, Student_Name, School_Id FROM Students WHERE Student_Id={student_id}")
    student = c.fetchone()
    if student:
        school_id = student[2]
        c.execute(f"SELECT School_Id, School_Name FROM Schools WHERE School_Id={school_id}")
        school = c.fetchone()
        if school:
            return f"ID Студента: {student[0]}\nИмя студента: {student[1]}\nID школы: {school[0]}\nНазвание школы: {school[1]}"
        else:
            return "Школа не найдена"
    else:
        return "Студент не найден"

print(get_student_info(203))


       