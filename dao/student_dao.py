from connection.db_connection import DbConnection
from entity.student import Student

_INSERT = 'INSERT INTO dorm_schema.student VALUES (%s, %s, %s, %s, %s)'


def insert(student: Student):
    """
    Inserts Student data into database
    :param student: Instance of entity.student.Student
    :return:
    """
    cur = DbConnection.get_cursor()
    cur.execute(_INSERT, (student.id, student.name, student.birthday, student.sex, student.room))


def insert_all(student_list: list):
    """
    Inserts list of Students into database
    :param student_list: List of entity.student.Student
    :return:
    """
    for student in student_list:
        insert(student)
