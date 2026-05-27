import pymysql

def get_connection():
    return pymysql.connect(host='localhost', port = 3306, user='root', password='root', database='module_02')

def create_table():
    connection = get_connection()
    cursor = connection.cursor()
    sql = """CREATE table if not exists wallet(
    walletId BIGINT primary key,
    userName VARCHAR(255),
    balance DOUBLE(10, 2),
    transactionType VARCHAR(255),
    transactionDate DATE
    )
    """
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("Table created successfully")

def insert_wallet(data = {}):
    id = data['walletId']
    user = data['userName']
    balance = data['balance']
    transactionType = data['transactionType']
    transactionDate = data['transactionDate']

    connection = get_connection()
    cursor = connection.cursor()
    sql = "INSERT into wallet values(%s,%s,%s,%s,%s)"
    data = (id, user, balance, transactionType, transactionDate)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("Wallet inserted successfully")

def read_wallet(params = {}):
    walletId = params.get('walletId', 0)
    userName = params.get('userName', '')
    balance = params.get('balance', 0)
    transactionType = params.get('transactionType', '')
    transactionDate = params.get('transactionDate', '')
    pageNo = params.get('pageNo', 0)
    pageSize = params.get('pageSize', 10)

    connection = get_connection()
    cursor = connection.cursor()

    sql = "SELECT * from wallet where 1=1"
    if walletId != 0:
        sql += " and walletId = " + str(walletId)
    if userName != '':
        sql += " and userName like '" + userName + "%'"
    if balance != 0:
        sql += " and balance = " + str(balance)
    if transactionType != '':
        sql += " and transactionType like '" + transactionType + "%'"
    if transactionDate != '':
        sql += " and transactionDate like '" + transactionDate + "%'"

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
    print("Wallet table read successfully")

def update_wallet(param = {}):
    walletId = param['walletId']
    userName = param['userName']
    balance = param['balance']
    transactionType = param['transactionType']
    transactionDate = param['transactionDate']

    connection = get_connection()
    cursor = connection.cursor()
    sql = "update wallet set userName = %s, balance = %s, transactionType = %s, transactionDate = %s where walletId = %s"
    data = (userName, balance, transactionType, transactionDate, walletId)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("Wallet updated successfully")

def delete_wallet(walletId):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "delete from wallet where walletId = %s"
    data = (walletId,)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("Wallet deleted successfully")

# --------------------------------------------------------------------------------------


# create_table()
data = {
        'walletId': 103,
        'userName': 'Priya',
        'balance': 2500.00,
        'transactionType': 'Credit',
        'transactionDate': '2026-05-19'
    }


# insert_wallet(data)
params = {
    'walletId': 0,
    'userName': '%a%',
    'balance': 0,
    'transactionType': '',
    'transactionDate': '',
    'pageNo': 1,
    'pageSize': 5
}
param = {
    'walletId': 103,
    'userName': 'Mohan',
    'balance': 3000,
    'transactionType': 'CREDIT',
    'transactionDate': '2026-05-20'
}
# update_wallet(param)
read_wallet(params)
# delete_wallet(2)