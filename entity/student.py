import re
from datetime import datetime


class Student:
    def __init__(self, birthday: str, id: int, name: str, room: int, sex: str):
        self._birthday = birthday
        self._id = id
        self._name = name
        self._room = room
        self._sex = sex

    @property
    def birthday(self):
        return self._birthday

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def room(self):
        return self._room

    @property
    def sex(self):
        return self._sex

    @birthday.setter
    def birthday(self, value):
        match = re.search(r'\d{4}-\d{2}-\d{2}', value)
        date = datetime.strptime(match.group(), '%Y-%m-%d').date()
        self._birthday = value

    @id.setter
    def id(self, value):
        self._id = int(value)

    @name.setter
    def name(self, value):
        self._name = value

    @room.setter
    def room(self, value):
        self._room = int(value)

    @sex.setter
    def sex(self, value):
        if value != 'M' and value != 'F':
            value = 'M'
        self._sex = value
