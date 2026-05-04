import pymysql
from datetime import datetime

def get_connection():
    return pymysql.connect(host='localhost', port=3306, user='root', password='root', db='module')

def setup_module():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("Drop table if exists Login_attempts")
    sql = """Create table Login_attempts (
    attemptID BIGINT PRIMARY KEY,
    attemptCode VARCHAR(100),
    username VARCHAR(100),
    attemptTime DATETIME,
    status VARCHAR(100)
    )
    """
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("Table created successfully")

def seed_data():
    connection = get_connection()
    cursor = connection.cursor()
    sql = "Insert into Login_attempts (attemptID, attemptCode, username, attemptTime, status) VALUES (%s, %s, %s, %s, %s)"

    data = [
            (i, 'Log_00' + str(i), 'user_' + str(i), datetime.now(), 'success')
            for i in range(1, 11)
             ]
    cursor.executemany(sql, data)
    connection.commit()
    cursor.close()
    connection.close()
    print("Data inserted successfully")

def get_attempts(username_filter = "%"):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "select * from Login_attempts where username like %s"
    cursor.execute(sql, username_filter)
    result = cursor.fetchall()
    for row in result:
        print(row)
    connection.commit()
    connection.close()

def read_attempts():
    connection = get_connection()
    cursor = connection.cursor()
    sql = "select * from Login_attempts"
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(row[0], '\t', row[1], '\t', row[2], '\t', row[3], '\t', row[4])
    connection.commit()
    connection.close()

get_connection()
setup_module()
seed_data()
get_attempts()
read_attempts()