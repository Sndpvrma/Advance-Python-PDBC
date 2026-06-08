import pymysql

def get_connection():
    return pymysql.connect(host='localhost', port = 3306, user='root', password='root', database='module')

def create_table():
    connection = get_connection()
    cursor = connection.cursor()
    sql = """CREATE table if not exists gymManagement(
    memberId BIGINT primary key,
    memberName VARCHAR(255),
    trainerName VARCHAR(255),
    membershipFee DOUBLE(10, 2),
    workoutType VARCHAR(255)
    )
    """
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("Table created successfully")

def insert(data = {}):
    memberId = data['memberId']
    memberName = data['memberName']
    trainerName = data['trainerName']
    membershipFee = data['membershipFee']
    workoutType = data['workoutType']

    connection = get_connection()
    cursor = connection.cursor()
    sql = "INSERT into gymManagement values(%s,%s,%s,%s,%s)"
    data = (memberId, memberName, trainerName, membershipFee, workoutType)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("gymManagement inserted successfully")

def read(params = {}):
    memberId = params.get('memberId', 0)
    memberName = params.get('memberName', '')
    trainerName = params.get('trainerName', '')
    membershipFee = params.get('membershipFee', 0)
    workoutType = params.get('workoutType', 0)
    pageNo = params.get('pageNo', 0)
    pageSize = params.get('pageSize', 10)

    connection = get_connection()
    cursor = connection.cursor()

    sql = "SELECT * from gymManagement where 1=1"
    if memberId != 0:
        sql += " and memberId = " + str(memberId)
    if memberName != '':
        sql += " and memberName like '" + memberName + "%'"
    if trainerName != '':
        sql += " and trainerName like '" + trainerName + "%'"
    if membershipFee != 0:
        sql += " and membershipFee = " + str(membershipFee)
    if workoutType != 0:
        sql += " and workoutType = " + str(workoutType)

    if pageNo > 0:
        offset = (pageNo - 1) * pageSize
        sql += " LIMIT " + str(offset) + ", " + str(pageSize)

    print('sql=>', sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4])
    connection.commit()
    connection.close()
    print("gymManagement table read successfully")

def update(param = {}):
    memberId = param['memberId']
    memberName = param['memberName']
    trainerName = param['trainerName']
    membershipFee = param['membershipFee']
    workoutType = param['workoutType']

    connection = get_connection()
    cursor = connection.cursor()
    sql = "update gymManagement set memberName = %s, trainerName = %s, membershipFee = %s, workoutType = %s where memberId = %s"
    data = (memberId, memberName, trainerName, membershipFee, workoutType)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("gymManagement updated successfully")

def delete(orderId):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "delete from gymManagement where orderId = %s"
    data = (orderId,)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("gymManagement deleted successfully")

#----------------------------------------------------------------------------------------------

# create_table()
data = {
    'memberId' : 3,
    'memberName' : 'aditya',
    'trainerName' : 'Nitin',
    'membershipFee' : 800,
    'workoutType' : 'squats'
}

# insert(data)

params = {
    'memberId' : 1,
    'memberName' : 'rohan',
    'trainerName' : 'nitin',
    'membershipFee' : 700,
    'workoutType' : 'pushUp',
    'pageNo' : 1,
    'pageSize' : 10
}

param = {
    'memberId' : 1,
    'memberName' : 'raju',
    'trainerName' : 'nitin',
    'membershipFee' : 750,
    'workoutType' : 'squats',
}

# update(param)
read(params = {})
# delete(0)