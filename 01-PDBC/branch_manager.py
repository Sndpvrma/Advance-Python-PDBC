#managerId BIGINT
#managerName string
#branchName string
#contactNumber string

import pymysql

def get_connection():
    return pymysql.connect(host='localhost', port=3306, user='root', password='root', database='module')

def create():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('drop table if exists branch_manager')

    sql = """CREATE table if not exists branch_manager(
    managerId BIGINT primary key,
    managerName VARCHAR(255),
    branchName VARCHAR(255),
    contactNumber VARCHAR(255)
    )
    """
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("Table created successfully")

def insert(data = {}):
    managerId = data['managerId']
    managerName = data['managerName']
    branchName = data['branchName']
    contactNumber = data['contactNumber']

    connection = get_connection()
    cursor = connection.cursor()
    sql = "INSERT into branch_manager values(%s,%s,%s,%s)"
    data = (managerId, managerName, branchName, contactNumber)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("branch_manager inserted successfully")

def read(params = {}):
    managerId = params.get('managerId', 0)
    managerName = params.get('managerName', '')
    branchName = params.get('branchName', '')
    contactNumber = params.get('contactNumber', '')
    pageNo = params.get('pageNo', 0)
    pageSize = params.get('pageSize', 10)

    connection = get_connection()
    cursor = connection.cursor()

    sql = "SELECT * from branch_manager where 1=1"
    if managerId != 0:
        sql += " and managerId = " + str(managerId)
    if managerName != '':
        sql += " and managerName like '" + managerName + "%'"
    if branchName != '':
        sql += " and branchName = '" + branchName + "%'"
    if contactNumber != '':
        sql += " and contactNumber like '" + contactNumber + "%'"
    if pageNo > 0:
        offset = (pageNo - 1) * pageSize
        sql += " LIMIT " + str(offset) + ", " + str(pageSize)

    print('sql=>', sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3])
    connection.commit()
    connection.close()
    print("branch_manager table read successfully")

def update(param = {}):
    managerId = param['managerId']
    managerName = param['managerName']
    branchName = param['branchName']
    contactNumber = param['contactNumber']

    connection = get_connection()
    cursor = connection.cursor()
    sql = "update branch_manager set managerName = %s, branchName = %s, contactNumber = %s where managerId = %s"
    data = (managerId, managerName, branchName, contactNumber)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("branch_manager updated successfully")

def delete(orderId):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "delete from stock where branch_manager = %s"
    data = (orderId,)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("branch_manager deleted successfully")

#----------------------------------------------------------------------------------------

create()
data = {
    'managerId' : 3,
    'managerName' : 'Mohan Rathore',
    'branchName' : 'Madhumila Square',
    'contactNumber' : '9754235749'
}

insert(data)

params = {
    'managerId' : 0,
    'managerName' : '',
    'branchName' : '',
    'contactNumber' : '',
    'pageNo' : 1,
    'pageSize' : 10
}

param = {
    'managerId' : 2,
    'managerName' : 'Suresh Sharma',
    'branchName' : 'Bhanwar Kua',
    'contactNumber' : '99264530068',
}

update(param)
read(params)
delete(0)