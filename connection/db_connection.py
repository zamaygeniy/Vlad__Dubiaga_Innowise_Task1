import psycopg2


class DbConnection:
    __instance = None
    __connection = None

    def __init__(self):
        if not DbConnection.__instance:
            try:
                self.__connection = psycopg2.connect(host='localhost', dbname='dorm', user='postgres',
                                                   password='18Eligorko81')
                self.__connection.autocommit = True
            except Exception as e:
                print(e)
        else:
            print("Instance already created:", self.get_instance())

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = DbConnection()
        return cls.__instance

    @classmethod
    def get_cursor(cls):
        return cls.get_instance().__connection.cursor()
