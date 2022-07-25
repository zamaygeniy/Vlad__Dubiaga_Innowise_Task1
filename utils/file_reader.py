import json

from entity.room import Room
from entity.student import Student


def get_student_list(path: str):
    """
    Reads file and returns list of Student instances
    :param path: Path to a file
    :return: list of entity.student.Student
    """
    student_list = []
    with open(path, 'r') as file:
        student_json_array = json.load(file)
        for student in student_json_array:
            student_list.append(Student(**student))
    return student_list


def get_room_list(path: str):
    """
    Reads file and returns list of Room instances
    :param path: Path to a file
    :return: list of entity.room.Room
    """
    room_list = []
    with open(path, 'r') as file:
        room_json_array = json.load(file)
        for room in room_json_array:
            room_list.append(Room(**room))
    return room_list
