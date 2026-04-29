# Subscription Usage Module

import pymysql

def get_connection():
    return pymysql.connect(host='localhost', port = 3306, user='root', password='root', db='module')

def create_table():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("Drop table if exists subscription_usage")
    sql = """CREATE TABLE IF NOT EXISTS subscription_usage (
    usageID BIGINT PRIMARY KEY,
    usageCode VARCHAR(50),
    userName VARCHAR(50),
    userCount INT,
    status VARCHAR(50)
    )"""
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("Table created successfully")

def insert_table():
    connection = get_connection()
    cursor = connection.cursor()
    sql = "INSERT INTO subscription_usage VALUES (%s, %s, %s, %s, %s)"
    data = [
    (1, 'USG-001', 'Rahul Sharma', 150, 'ACTIVE'),
    (2, 'USG-002', 'Anjali Gupta', 45, 'ACTIVE'),
    (3, 'USG-003', 'Amit Verma', 0, 'INACTIVE'),
    (4, 'USG-004', 'Suresh Raina', 200, 'EXPIRED'),
    (5, 'USG-005', 'Priya Singh', 10, 'ACTIVE'),
    (6, 'USG-006', 'Vikram Rathore', 85, 'PENDING'),
    (7, 'USG-007', 'Neha Dixit', 120, 'ACTIVE'),
    (8, 'USG-008', 'Karan Johar', 300, 'LOCKED'),
    (9, 'USG-009', 'Sonia Gandhi', 12, 'ACTIVE'),
    (10, 'USG-010', 'Modi Ji', 500, 'ACTIVE'),
]
    cursor.executemany(sql, data)
    connection.commit()
    connection.close()
    print("Table inserted successfully")

def insert_data(data = {}):
    usageID = data['usageID']
    usageCode = data['usageCode']
    userName = data['userName']
    userCount = data['userCount']
    status = data['status']
    connection = get_connection()
    cursor = connection.cursor()
    sql = "INSERT INTO subscription_usage VALUES (%s, %s, %s, %s, %s)"
    data = [usageID, usageCode, userName, userCount, status]
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("Data inserted successfully")

def view_table(param = {}):
    usageID = param.get('usageID', 0)
    usageCode = param.get('usageCode', '')
    userName = param.get('userName', '')
    userCount = param.get('userCount', 0)
    status = param.get('status', '')
    pageno = param.get('pageno', 0)
    pagesize = param.get('pagesize', 0)

    connection = get_connection()
    cursor = connection.cursor()
    sql = "SELECT * from subscription_usage WHERE 1=1"
    if usageID != 0:
        sql += " AND usageID = " + str(usageID)
    if usageCode != '':
        sql += " AND usageCode like '" + usageCode + "%'"
    if userName != '':
        sql += " AND userName like '" + userName + "%'"
    if userCount != 0:
        sql += " AND userCount = " + userCount
    if status != '':
        sql += " AND status like '" + status + "%'"

    # Pagination
    if pageno > 0:
        offset = (pageno - 1) * pagesize
        sql += " LIMIT " + str(offset) + ", " + str(pagesize)

    print("sql=>", sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    print("Data of subscription_usage:\n")
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4])
    connection.commit()
    connection.close()

def update_table(data):
    usageID = data['usageID']
    usageCode = data['usageCode']
    userName = data['userName']
    userCount = data['userCount']
    status = data['status']
    connection = get_connection()
    cursor = connection.cursor()
    sql = "update subscription_usage set uasgeID = %s, usageCode = %s, userName = %s, userCount = %s, status = %s where usageID = %s"
    data = [usageID, usageCode, userName, userCount, status, usageID]
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("Table updated successfully")

def delete_table():
    connection = get_connection()
    cursor = connection.cursor()
    sql = "delete from subscription_usage where usageID = %s"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("Table deleted successfully")

get_connection()
create_table()
insert_table()

insert_data({
    'usageID' : 11,
    'usageCode' : 'USG-011',
    'userName' : 'Yogi Ji',
    'userCount' : 103,
    'status' : 'Locked'
})

params = {
    'usageID' : 9,
    'usageCode' : 'USG-009',
    'userName' : 'Rahul Gandhi',
    'userCount' : 120,
    'status' : 'ACTIVE'
}

update_table(params)

param = {
    'usageID' : 6,
    'usageCode' : 'USG-006',
    'userName' : 'Vikram Rathore',
    'userCount' : 82,
    'status' : 'ACTIVE',
    'pageno': 2,
    'pagesize': 5
}

view_table()
delete_table()


