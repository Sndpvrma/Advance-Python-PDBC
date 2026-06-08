import pymysql

def get_connection():
    return pymysql.connect(host='localhost', port=3306, user='root', password='root', database='module')

def create():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('drop table if exists broker')

    sql = """CREATE table if not exists broker(
    brokerId BIGINT primary key,
    brokerName VARCHAR(255),
    contactNumber VARCHAR(255),
    company VARCHAR(255)
    )
    """
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("Table created successfully")

def insert(data = {}):
    brokerId = data['brokerId']
    brokerName = data['brokerName']
    contactNumber = data['contactNumber']
    company = data['company']

    connection = get_connection()
    cursor = connection.cursor()
    sql = "INSERT into broker values(%s,%s,%s,%s)"
    data = (brokerId, brokerName, contactNumber, company)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("broker inserted successfully")

def read(params = {}):
    brokerId = params.get('brokerId', 0)
    brokerName = params.get('brokerName', '')
    contactNumber = params.get('contactNumber', '')
    company = params.get('company', '')
    pageNo = params.get('pageNo', 0)
    pageSize = params.get('pageSize', 10)

    connection = get_connection()
    cursor = connection.cursor()

    sql = "SELECT * from broker where 1=1"
    if brokerId != 0:
        sql += " and brokerId = " + str(brokerId)
    if brokerName != '':
        sql += " and brokerName like '" + brokerName + "%'"
    if contactNumber != '':
        sql += " and contactNumber like '" + contactNumber + "%'"
    if company != '':
        sql += " and company = '" + company + "%'"
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
    print("broker table read successfully")

def update(param = {}):
    brokerId = param['brokerId']
    brokerName = param['brokerName']
    contactNumber = param['contactNumber']
    company = param['company']

    connection = get_connection()
    cursor = connection.cursor()
    sql = "update broker set brokerName = %s, contactNumber = %s,  company = %s where brokerId = %s"
    data = (brokerId, brokerName, contactNumber, company)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("broker updated successfully")

def delete(brokerId):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "delete from stock where brokerId = %s"
    data = (brokerId,)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("broker deleted successfully")

#----------------------------------------------------------------------------------------

# create()
data = {
    'brokerId' : 3,
    'brokerName' : 'ravi raj',
    'contactNumber': '9754887546',
    'company' : 'upstock'
}

insert(data)

params = {
    'brokerId' : 0,
    'brokerName' : '',
    'contactNumber': '',
    'company' : '',
    'pageNo' : 1,
    'pageSize' : 10
}

param = {
    'brokerId' : 2,
    'brokerName' : 'Suresh Sharma',
    'contactNumber': '99264530068',
    'company' : 'Bhanwar Kua'
}

# update(param)
read(params)
# delete(0)