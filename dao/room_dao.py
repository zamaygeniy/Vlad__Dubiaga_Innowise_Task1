from connection.db_connection import DbConnection
from entity.room import Room

_INSERT = 'INSERT INTO dorm_schema.room VALUES (%s, %s)'


def insert(room: Room):
    """
    Inserts Room data into database
    :param room: Instance of entity.room.Room
    :return:
    """
    cur = DbConnection.get_cursor()
    cur.execute(_INSERT, (room.id, room.name))


def insert_all(room_list: list):
    """
    Inserts list of Room into database
    :param room_list: List of entity.room.Room
    :return:
    """
    for room in room_list:
        insert(room)
