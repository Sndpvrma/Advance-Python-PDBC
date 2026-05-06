import pymysql

def get_connection():
    return pymysql.connect(host='localhost', port=3306, user='root', password='root', db='module')

def create_table():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF exists USER_SETTINGS")
    sql = """CREATE TABLE IF NOT exists USER_SETTINGS(
    settingsID BIGINT PRIMARY KEY,
    settingCode VARCHAR(50),
    userName VARCHAR(50),
    preference VARCHAR(50),
    status VARCHAR(50)
    )
    """
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("Table created successfully")

def insert_table():
    connection = get_connection()
    cursor = connection.cursor()
    sql = "Insert into USER_SETTINGS VALUES (%s, %s, %s, %s, %s)"
    data = [
        (1, 'SET_001', 'Rahul', 'Dark Mode', 'Active'),
        (2, 'SET_002', 'Anjali', 'Hindi', 'Active'),
        (3, 'SET_003', 'Amit', 'Email', 'Inactive'),
        (4, 'SET_004', 'Suresh', 'Medium Font', 'Active'),
        (5, 'SET_005', 'Priya', 'Private', 'Active'),
        (6, 'SET_006', 'Vikram', 'Light Mode', 'Active'),
        (7, 'SET_007', 'Sneha', 'English', 'Active'),
        (8, 'SET_008', 'Rohit', 'Push Notif', 'Active'),
        (9, 'SET_009', 'Karan', 'IST Time', 'Active'),
        (10, 'SET_010', 'Neha', 'Weekly Backup', 'Inactive')
    ]
    cursor.executemany(sql, data)
    connection.commit()
    connection.close()
    print("Table inserted successfully")

def read_table(params = {}):
    settingID = params.get('settingID', 0)
    settingCode = params.get('settingCode', '')
    userName = params.get('userName', '')
    preference = params.get('preference', '')
    status = params.get('status', '')
    pageno = params.get('pageno', 0)
    pagesize = params.get('pagesize', 10)

    connection = get_connection()
    cursor = connection.cursor()

    sql = "select * from USER_SETTINGS where 1=1"
    if settingID != 0:
        sql += " AND settingId = " + str(settingID)
    if settingCode != '':
        sql += " AND settingCode like '" + settingCode + "%'"
    if userName != '':
        sql += " AND userName like '" + userName + "%'"
    if preference != '':
        sql += " AND preference like '" + preference + "%'"
    if status != '':
        sql += " AND status like '" + status + "%'"

    if pageno > 0:
        offset = (pageno - 1) * pagesize
        sql += " LIMIT " + str(offset) + ", " + str(pagesize)

    print("sal=> ", sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4])
    connection.commit()
    connection.close()
    print("Table read successfully")

def update_table():
    connection = get_connection()
    connection.autocommit(False)
    cursor = connection.cursor()
    try:
        print("Start Inserting Data...")
        cursor.execute("insert into USER_SETTINGS values (11, 'SET_011', 'Rohan', 'Two-Factor', 'Active')")
        print("Creating Savepoint sp1...")
        cursor.execute("Savepoint sp1")
        try:
            cursor.execute("insert into USER_SETTINGS values (12, 'SET_012', 'Aditi', 'High Contrast', 'Active')")
            print("Creating Savepoint sp2...")
            cursor.execute("Savepoint sp2")
            try:
                cursor.execute("insert into USER_SETTINGS values (12, 'SET_013', 'Test', 'Error', 'Active')")
                print("Creating Savepoint sp3...")
                cursor.execute("Savepoint sp3")
            except Exception as e:
                print("Error in third insert, rolling back to Savepoint sp2")
                cursor.execute("roll back to Savepoint sp2")
        except Exception as e:
            print("Error in second insert, rolling back to Savepoint sp1")
            cursor.execute("roll back to Savepoint sp1")
        print("Committing Transaction...")
        connection.commit()
    except Exception as e:
        print("Error in transaction", e)
        connection.rollback()
    finally:
        connection.close()
    print("Table updated successfully")

def delete_table():
    connection = get_connection()
    cursor = connection.cursor()
    sql = "delete from USER_SETTINGS where settingsID = 1"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("Table deleted successfully")

get_connection()
create_table()
insert_table()

params = {
    'settingsID': 1,
    'settingCode': '',
    'userName': '',
    'preference': '',
    'status': '',
    'pageno': 0,
    'pagesize': 10
}

update_table()
delete_table()
read_table(params = {})