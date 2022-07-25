import os

from dao import room_dao, student_dao
from service import query_service
from utils import file_reader, file_writer


def show_interface():
    print("1. Load data to database")
    print("2. Retrieve data from database")
    opt = input("Choose option: ")
    if opt == '1':
        _load_interface()
    if opt == '2':
        _retrieve_interface()


def _load_interface():
    path_to_rooms = input("Enter path to rooms file: ")
    path_to_students = input("Enter path to students file: ")
    student_list = file_reader.get_student_list(path_to_students)
    room_list = file_reader.get_room_list(path_to_rooms)
    room_dao.insert_all(room_list)
    student_dao.insert_all(student_list)


def _retrieve_interface():
    print("1. Get number of students in each room")
    print("2. Get top 5 rooms with min average age")
    print("3. Get top 5 rooms with the highest difference in age")
    print("4. Get rooms where live students of both sexes")
    opt2 = input("Choose option: ")
    records = None
    if opt2 == '1':
        records = query_service.get_number_of_students_in_room()
    if opt2 == '2':
        records = query_service.get_top5_with_min_age_avg()
    if opt2 == '3':
        records = query_service.get_top5_with_highest_diff_in_age()
    if opt2 == '4':
        records = query_service.get_rooms_where_live_both_sexes()
    print("1. Write to JSON")
    print("2. Write to XML")
    opt3 = input("Choose option: ")
    path_to_file = input("Enter path to output file: ")
    if opt3 == '1':
        print(path_to_file)
        file_writer.write_to_json(path_to_file, records)
    if opt3 == '2':
        file_writer.write_to_xml(path_to_file, records)
