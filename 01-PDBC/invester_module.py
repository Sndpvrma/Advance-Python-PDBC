import pymysql

def get_connection():
    return pymysql.connect(host='localhost', port=3306, user='root', password='root', database='module')

def create():
    connection = get_connection()
    cursor = connection.cursor()

    sql = """CREATE table if not exists stock(
    stockId BIGINT primary key,
    stockName VARCHAR(255),
    price DOUBLE(10, 2),
    quantity INT
    )
    """
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("Table created successfully")

def insert(data = {}):
    stockId = data['stockId']
    stockName = data['stockName']
    price = data['price']
    quantity = data['quantity']

    connection = get_connection()
    cursor = connection.cursor()
    sql = "INSERT into stock values(%s,%s,%s,%s)"
    data = (stockId, stockName, price, quantity)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("stock inserted successfully")

def read(params = {}):
    stockId = params.get('stockId', 0)
    stockName = params.get('stockName', '')
    price = params.get('price', 0)
    quantity = params.get('quantity', 0)
    pageNo = params.get('pageNo', 0)
    pageSize = params.get('pageSize', 10)

    connection = get_connection()
    cursor = connection.cursor()

    sql = "SELECT * from stock where 1=1"
    if stockId != 0:
        sql += " and stockId = " + str(stockId)
    if stockName != '':
        sql += " and stockName like '" + stockName + "%'"
    if price != 0:
        sql += " and price = " + str(price)
    if quantity != 0:
        sql += " and quantity like " + str(quantity)
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
    print("stock table read successfully")

def update(param = {}):
    stockId = param['stockId']
    stockName = param['stockName']
    price = param['price']
    quantity = param['quantity']

    connection = get_connection()
    cursor = connection.cursor()
    sql = "update stock set stockName = %s, price = %s, quantity = %s where stockId = %s"
    data = (stockId, stockName, price, quantity)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("stock updated successfully")

def delete(orderId):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "delete from stock where stockId = %s"
    data = (orderId,)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("stock deleted successfully")

#----------------------------------------------------------------------------------------

# create()
data = {
    'stockId' : 3,
    'stockName' : 'techmahindra',
    'price' : 3000,
    'quantity' : 240
}

# insert(data)

params = {
    'stockId' : 3,
    'stockName' : '',
    'price' : 0,
    'quantity' : 0,
    'pageNo' : 1,
    'pageSize' : 10
}

param = {
    'stockId' : 3,
    'stockName' : 'reliance',
    'price' : 700,
    'quantity' : 1000,
}

# update(param)
read(params)
# delete(0)