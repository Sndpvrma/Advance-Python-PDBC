import pymysql

def get_connection():
    return pymysql.connect(host='localhost', port=3306, user='root', password='root', database='module')

def create():
    connection = get_connection()
    cursor = connection.cursor()

    sql = """CREATE table if not exists car_rental(
    carId BIGINT primary key,
    customerName VARCHAR(255),
    carModel VARCHAR(255),
    rentPerDay DOUBLE(10, 2),
    fuelType VARCHAR(255)
    )
    """
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("Table created successfully")

def insert(data = {}):
    carId = data['carId']
    customerName = data['customerName']
    carModel = data['carModel']
    rentPerDay = data['rentPerDay']
    fuelType = data['fuelType']

    connection = get_connection()
    cursor = connection.cursor()
    sql = "INSERT into car_rental values(%s,%s,%s,%s,%s)"
    data = (carId, customerName, carModel, rentPerDay, fuelType)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("car_rental inserted successfully")

def read(params = {}):
    carId = params.get('carId', 0)
    customerName = params.get('customerName', '')
    carModel = params.get('carModel', '')
    rentPerDay = params.get('rentPerDay', 0)
    fuelType = params.get('fuelType', '')
    pageNo = params.get('pageNo', 0)
    pageSize = params.get('pageSize', 10)

    connection = get_connection()
    cursor = connection.cursor()

    sql = "SELECT * from car_rental where 1=1"
    if carId != 0:
        sql += " and carId = " + str(carId)
    if customerName != '':
        sql += " and customerName like '" + customerName + "%'"
    if carModel != '':
        sql += " and carModel like '" + carModel + "%'"
    if rentPerDay != 0:
        sql += " and rentPerDay = " + str(rentPerDay)
    if fuelType != 0:
        sql += " and fuelType like '" + fuelType + "%'"

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
    print("car_rental table read successfully")

def update(param = {}):
    carId = param['carId']
    customerName = param['customerName']
    carModel = param['carModel']
    rentPerDay = param['rentPerDay']
    fuelType = param['fuelType']

    connection = get_connection()
    cursor = connection.cursor()
    sql = "update car_rental set customerName = %s, carModel = %s, rentPerDay = %s, fuelType = %s where carId = %s"
    data = (carId, customerName, carModel, rentPerDay, fuelType)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("car_rental updated successfully")

def delete(orderId):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "delete from college_system where carId = %s"
    data = (orderId,)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("car_rental deleted successfully")

#----------------------------------------------------------------------------------------

# create()
data = {
    'carId' : 1,
    'customerName' : 'rohan',
    'carModel' : 'tata sierra',
    'rentPerDay' : 8000,
    'fuelType' : 'diesel'
}

insert(data)

params = {
    'carId' : 1,
    'customerName' : 'ramesh',
    'carModel' : 'mahindra thar',
    'rentPerDay' : 7000,
    'fuelType' : 'diesel',
    'pageNo' : 1,
    'pageSize' : 10
}

param = {
    'carId' : 1,
    'customerName' : 'nitin',
    'carModel' : 'CSE',
    'rentPerDay' : 7000,
    'fuelType' : 'diesel',
}

# update(param)
read(params = {})
# delete(0)