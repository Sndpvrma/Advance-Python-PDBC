import pymysql

def create_table():
    connection = pymysql.connect(host = 'localhost', port = 3306, user = 'root', password = 'root', db = 'Module')
    cursor = connection.cursor()
    sql = """CREATE TABLE data_validation(ValidationID BIGINT PRIMARY KEY,
    ValidationCode varchar(50),
    FieldName varchar(50),
    Rule varchar(50),
    Status varchar(50)
    )
    """
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("Table created successfully")

def insert_table():
    connection = pymysql.connect(host = 'localhost', port = 3306, user = 'root', password = 'root', db = 'Module')
    cursor = connection.cursor()
    sql = "INSERT INTO data_validation VALUES(%s, %s, %s, %s, %s)"
    data = [
        (1, 'A001', 'email', 'required_and_formate', 'ACTIVE'),
        (2, 'A002', 'age', 'min_value_18', 'PENDING'),
        (3, 'A003', 'username', 'no_special_characters', 'INACTIVE'),
        (4, 'A004', 'phone', 'min_length_10', 'ACTIVE'),
        (5, 'A005', 'password', 'min_length_8', 'PENDING'),
    ]
    cursor.executemany(sql, data)
    connection.commit()
    connection.close()
    print("Data Inserted successfully")

def insert_data(data = {}):
    ValidationID = data['ValidationID']
    ValidationCode = data['ValidationCode']
    FieldName = data['FieldName']
    Rule = data['Rule']
    Status = data['Status']
    connection = pymysql.connect(host = 'localhost', port = 3306, user = 'root', password = 'root', db = 'Module')
    cursor = connection.cursor()
    sql = "INSERT INTO data_validation VALUES(%s, %s, %s, %s, %s)"
    data = [ValidationID, ValidationCode, FieldName, Rule, Status]
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("Data Inserted successfully")

def view_data(param = {}):
    ValidationID = param.get('ValidationID', 0)
    ValidationCode = param.get('ValidationCode', '')
    FieldName  = param.get('FieldName', '')
    Rule = param.get('Rule', '')
    Status = param.get('Status', '')

    connection = pymysql.connect(host = 'localhost', port = 3306, user = 'root', password = 'root', db = 'Module')
    cursor = connection.cursor()

    sql = "SELECT * FROM data_validation where 1=1"
    if ValidationID != 0:
        sql += "and ValidationID = " + str(ValidationID)
    if ValidationCode != '':
        sql += " and ValidationName like '" + ValidationCode + "%'"
    if FieldName != '':
        sql += " and FieldName = '" + FieldName + "%'"
    if Rule != '':
        sql += " and Rule = '" + Rule + "%'"
    if Status != '':
        sql += " and Status = '" + Status + "%'"

    print('sql => ', sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4], '\t')
    connection.commit()
    connection.close()

def update_data(data):
    ValidationID = data['ValidationID']
    ValidationCode = data['ValidationCode']
    FieldName = data['FieldName']
    Rule = data['Rule']
    Status = data['Status']

    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='Module')
    cursor = connection.cursor()
    sql = "update data_validation set ValidationID = %s, ValidationCode = %s, FieldName = %s, Rule = %s, Status = %s WHERE ValidationID = %s"
    data = [ValidationID, ValidationCode, FieldName, Rule, Status, ValidationID]
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("Data Update successfully")

def delete_data():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='Module')
    cursor = connection.cursor()
    sql = "delete from data_validation where ValidationID = 4"
    cursor.execute(sql)
    connection.commit()
    print("Data Delete successfully")


create_table()
insert_table()
insert_data({'ValidationID': 106,
             'ValidationCode': 'A006',
             'FieldName': 'email_password',
             'Rule': 'atlaest_one_special_charactor',
             'Status': 'ACTIVE'
             })
params = {}
params['ValidationID'] = 106
params['ValidationCode'] = 'A006'
params['FieldName'] = 'email_password'
params['Rule'] = 'Atleast_one_special_charactor'
params['Status'] = 'INACTIVE'

view_data()
update_data(params)
view_data()
delete_data()
