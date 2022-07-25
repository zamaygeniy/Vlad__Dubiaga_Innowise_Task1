from connection.db_connection import DbConnection

_NUMBER_OF_STUDENTS_IN_ROOM = '''SELECT dorm_schema.room.name AS name, count(*) AS number_of_students
                                  FROM dorm_schema.student
                                  INNER JOIN dorm_schema.room
                                  ON dorm_schema.student.room = dorm_schema.room.id
                                  GROUP BY dorm_schema.room.name
                                  ORDER BY number_of_students DESC'''

_TOP5_WITH_MIN_AGE_AVG = '''SELECT dorm_schema.room.name AS name, avg_age
                             FROM
                                (SELECT dorm_schema.student.room AS room_number, 
                                 AVG(DATE_PART('year', CURRENT_DATE) - DATE_PART('year', dorm_schema.student.birthday)) 
                                 OVER (PARTITION BY dorm_schema.student.room) 
                                 AS avg_age
                                 FROM dorm_schema.student
                                ) AS avg_table
                             INNER JOIN dorm_schema.room
                             ON dorm_schema.room.id = avg_table.room_number
                             GROUP BY dorm_schema.room.name, avg_age
                             ORDER BY avg_age ASC
                             LIMIT 5'''

_TOP5_WITH_HIGHEST_DIFF_IN_AGE = '''SELECT dorm_schema.room.name AS name, age_diff
                                    FROM
                                        (SELECT dorm_schema.student.room AS room_number,
                                        MAX(DATE_PART('year', CURRENT_DATE) - DATE_PART('year', dorm_schema.student.birthday)) 
                                        OVER (PARTITION BY dorm_schema.student.room) -  
                                        MIN(DATE_PART('year', CURRENT_DATE) - DATE_PART('year', dorm_schema.student.birthday)) 
                                        OVER (PARTITION BY dorm_schema.student.room) AS age_diff
                                        FROM dorm_schema.student
                                        ) AS diff_table
                                    INNER JOIN dorm_schema.room
                                    ON dorm_schema.room.id = diff_table.room_number
                                    GROUP BY dorm_schema.room.name, age_diff
                                    ORDER BY age_diff DESC
                                    LIMIT 5'''

_ROOMS_WHERE_LIVE_BOTH_SEXES = '''SELECT dorm_schema.room.name AS name
                              FROM
                                    (SELECT dorm_schema.student.room AS room_number, sex,
                                    MAX(dorm_schema.student.sex) 
                                    OVER (PARTITION BY dorm_schema.student.room) AS sex1,  
                                    MIN(dorm_schema.student.sex) 
                                    OVER (PARTITION BY dorm_schema.student.room) AS sex2
                                    FROM dorm_schema.student
                                    ) AS sex_table
                              INNER JOIN dorm_schema.room
                              ON dorm_schema.room.id = sex_table.room_number
                              AND sex_table.sex1 != sex_table.sex2
                              GROUP BY dorm_schema.room.name'''


def get_number_of_students_in_room():
    """
    Gets number of students in each room from database
    :return: List of dictionaries {name, number_of_students}
    """
    cur = DbConnection.get_cursor()
    cur.execute(_NUMBER_OF_STUDENTS_IN_ROOM)
    result_set = cur.fetchall()
    keys = ('name', 'number_of_students')
    return _get_list_of_dict(keys, result_set)


def get_top5_with_min_age_avg():
    """
    Gets top 5 rooms with min average age from database
    :return: List of dictionaries {name, avg_age}
    """
    cur = DbConnection.get_cursor()
    cur.execute(_TOP5_WITH_MIN_AGE_AVG)
    result_set = cur.fetchall()
    keys = ('name', 'avg_age')
    return _get_list_of_dict(keys, result_set)


def get_top5_with_highest_diff_in_age():
    """
    Gets top 5 rooms with the highest difference in age
    :return: List of dictionaries {name, age_diff}
    """
    cur = DbConnection.get_cursor()
    cur.execute(_TOP5_WITH_HIGHEST_DIFF_IN_AGE)
    result_set = cur.fetchall()
    keys = ('name', 'age_diff')
    return _get_list_of_dict(keys, result_set)


def get_rooms_where_live_both_sexes():
    """
    Gets rooms where live students of both sexes
    :return: List of dictionaries {name}
    """
    cur = DbConnection.get_cursor()
    cur.execute(_ROOMS_WHERE_LIVE_BOTH_SEXES)
    result_set = cur.fetchall()
    keys = 'name'
    return _get_list_of_dict(keys, result_set)


def _get_list_of_dict(keys, result_set):
    """
    Transforms result set to list of dictionaries using keys
    :param keys: Keys for dictionary
    :param result_set: Result set from database
    :return: List of dictionaries
    """
    list_of_dict = [dict(zip(keys, values)) for values in result_set]
    return list_of_dict
