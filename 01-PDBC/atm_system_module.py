import pymysql

def get_connection():
    return pymysql.connect(host='localhost', port=3306, user='root', password='root', db='module')

def createTable():
    connection = get_connection()
    cursor = connection.cursor()
    sql = """CREATE TABLE IF NOT EXISTS atm_system(
    atmId BIGINT PRIMARY KEY,
    atmName VARCHAR(255),
    location VARCHAR(255),
    cashAvailable DOUBLE(10, 2),
    securityCode INT
    )
    """
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("Table created successfully")

def insert(data = {}):
    atmId = data['atmId']
    atmName = data['atmName']
    location = data['location']
    cashAvailable = data['cashAvailable']
    securityCode = data['securityCode']

    connection = get_connection()
    cursor = connection.cursor()
    sql = "INSERT into atm_system VALUES(%s, %s, %s, %s, %s)"
    data = (atmId, atmName, location, cashAvailable, securityCode)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("Table created successfully")

def search(param = {}):
    atmId = param.get('atmId', 0)
    atmName = param.get('atmName', '')
    location = param.get('location', '')
    cashAvailable = param.get('cashAvailable', 0)
    securityCode = param.get('securityCode', 0)
    pageNo = param.get('pageNo', 0)
    pageSize = param.get('pageSize', 0)

    connection = get_connection()
    cursor = connection.cursor()

    sql = "SELECT * from atm_system where 1=1"
    if atmId != 0:
        sql += " and atmId = " + str(atmId)
    if atmName != '':
        sql += " and atmName like '" + atmName + "%'"
    if location != '':
        sql += " and location like '" + location + "'"
    if cashAvailable != 0:
        sql += " and cashAvailable like " + str(cashAvailable)
    if securityCode != 0:
        sql += " and securityCode like " + str(securityCode)

    if pageNo > 0:
        offset = (pageNo - 1) * pageSize
        sql += " LIMIT " + str(offset) + ", " + str(pageSize)

    print("sql=> ", sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4])
    connection.commit()
    connection.close()
    print("Table read successfully")

def update(params = {}):
    atmId = params['atmId']
    atmName = params['atmName']
    location = params['location']
    cashAvailable = params['cashAvailable']
    securityCode = params['securityCode']

    connection = get_connection()
    cursor = connection.cursor()

    sql = "UPDATE atm_system set atmName = %s, location = %s, cashAvailable = %s, securityCode = %s where atmId = %s"
    data = (atmName, location, cashAvailable, securityCode, atmId)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("Table updated successfully")

def delete(atmId):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "DELETE from atm_system where atmId = %s"
    data = (atmId,)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("Table deleted successfully")

#------------------------------------------------------------------------------------

createTable()
data = {
    'atmId' : 2,
    'atmName' : 'bob',
    'location' : 'vijaynagar squar',
    'cashAvailable' : 22000,
    'securityCode' : 9584
}

insert(data)

param = {
    'atmId' : 1,
    'atmName' : 'sbi',
    'location' : 'madhumilan squar',
    'cashAvailable' : 18000,
    'securityCode' : 9088,
    'pageNo' : 0,
    'pageSize' : 10
}

search(param = {})

params = {
    'atmId' : 1,
    'atmName' : 'sbi',
    'location' : 'pipliyahan squar',
    'cashAvailable' : 2500,
    'securityCode' : 9088,
}

update(params)

delete(0)