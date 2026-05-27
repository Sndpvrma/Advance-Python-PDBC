import pymysql

def get_connection():
    return pymysql.connect(host='localhost', port = 3306, user='root', password='root', database='module_02')

def create_table():
    connection = get_connection()
    cursor = connection.cursor()
    sql = """CREATE table if not exists FoodDelivery(
    orderId BIGINT primary key,
    customerName VARCHAR(255),
    restaurantName VARCHAR(255),
    deliveryTime INT,
    totalAmount DOUBLE(10, 2)
    )
    """
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("Table created successfully")

def insert(data = {}):
    orderId = data['orderId']
    customerName = data['customerName']
    restaurantName = data['restaurantName']
    deliveryTime = data['deliveryTime']
    totalAmount = data['totalAmount']

    connection = get_connection()
    cursor = connection.cursor()
    sql = "INSERT into FoodDelivery values(%s,%s,%s,%s,%s)"
    data = (orderId, customerName, restaurantName, deliveryTime, totalAmount)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("FoodDelivery inserted successfully")

def read(params = {}):
    orderId = params.get('orderId', 0)
    customerName = params.get('customerName', '')
    restaurantName = params.get('restaurantName', '')
    deliveryTime = params.get('deliveryTime', 0)
    totalAmount = params.get('totalAmount', 0)
    pageNo = params.get('pageNo', 0)
    pageSize = params.get('pageSize', 10)

    connection = get_connection()
    cursor = connection.cursor()

    sql = "SELECT * from FoodDelivery where 1=1"
    if orderId != 0:
        sql += " and orderId = " + str(orderId)
    if customerName != '':
        sql += " and customerName like '" + customerName + "%'"
    if restaurantName != '':
        sql += " and restaurantName like '" + restaurantName + "%'"
    if deliveryTime != 0:
        sql += " and deliveryTime = " + str(deliveryTime)
    if totalAmount != 0:
        sql += " and totalAmount = " + str(totalAmount)

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
    print("FoodDelivery table read successfully")

def update(param = {}):
    orderId = param['orderId']
    customerName = param['customerName']
    restaurantName = param['restaurantName']
    deliveryTime = param['deliveryTime']
    totalAmount = param['totalAmount']

    connection = get_connection()
    cursor = connection.cursor()
    sql = "update FoodDelivery set customerName = %s, restaurantName = %s, deliveryTime = %s, totalAmount = %s where orderId = %s"
    data = (customerName, restaurantName, deliveryTime, totalAmount, orderId)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("FoodDelivery updated successfully")

def delete(orderId):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "delete from FoodDelivery where orderId = %s"
    data = (orderId,)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("FoodDelivery deleted successfully")

# --------------------------------------------------------------------------------------


# create_table()
# data = {}
# insert(data)
params = {}
# param = {}
# update(param = {)
read(params = {})
# delete(2)