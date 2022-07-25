class Room:
    def __init__(self, id, name):
        self._id = id
        self._name = name

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @id.setter
    def id(self, value):
        self._id = int(value)

    @name.setter
    def name(self, value):
        self._name = value

