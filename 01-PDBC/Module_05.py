# Data Mapping Module

import pymysql

def get_connection():
    return pymysql.connect(host='localhost', port=3306, user='root', password='root', db='module')

def create_table():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("Drop table if exists DATA_MAPPING")
    sql = """CREATE TABLE DATA_MAPPING(
    mappingID BIGINT PRIMARY KEY,
    mappingCode VARCHAR(50),
    sourceField VARCHAR(50),
    targetField VARCHAR(50),
    status VARCHAR(50)
    )
    """
    cursor.execute(sql)
    connection.commit()
    cursor.close()
    connection.close()
    print("Table created successfully")

def insert_data():
    connection = get_connection()
    cursor = connection.cursor()
    sql = "INSERT INTO DATA_MAPPING VALUES(%s, %s, %s, %s, %s)"
    data = [
        (1, 'CUST_01', 'first_name', 'fname', 'Active'),
        (2, 'CUST_02', 'last_name', 'lname', 'Active'),
        (3, 'CUST_03', 'email_address', 'email', 'Active'),
        (4, 'ADDR_01', 'zip_code', 'pincode', 'Active'),
        (5, 'ADDR_02', 'street_address', 'address_line1', 'Active'),
        (6, 'PROD_01', 'product_price', 'unit_price', 'Active'),
        (7, 'PROD_02', 'sku_id', 'product_code', 'Active'),
        (8, 'ORDER_01', 'order_date', 'transaction_date', 'Active'),
        (9, 'ORDER_02', 'qty', 'quantity', 'Active'),
        (10, 'ORDER_03', 'total_amt', 'gross_amount', 'Active')
    ]
    cursor.executemany(sql, data)
    connection.commit()
    connection.close()
    print("Data inserted successfully")

def read_data(param = {}):
    mappingID = param.get('mappingID', 0)
    mappingCode = param.get('mappingCode', '')
    sourceField = param.get('sourceField', '')
    targetField = param.get('targetField', '')
    status = param.get('status', '')
    pageno = param.get('pageno', 1)
    pagesize = param.get('pagesize', 10)

    connection = get_connection()
    cursor = connection.cursor()

    sql = "Select * from DATA_MAPPING WHERE 1=1"
    if mappingID != 0:
        sql += " AND mappingID = " + str(mappingID)
    if mappingCode != '':
        sql += " AND mappingCode like '" + mappingCode + "%'"
    if sourceField != '':
        sql += " AND sourceField like '" + sourceField + "%'"
    if targetField != '':
        sql += " AND targetField like '" + targetField + "%'"
    if status != '':
        sql += " AND status like '" + status + "%'"

    if pageno > 0:
        offset  = (pageno - 1) * pagesize
        sql += " LIMIT " + str(offset) + ", " + str(pagesize)
    print("sql=> ", sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(row[0], '\t', row[1], '\t', row[2], '\t', row[3], '\t', row[4])
    connection.commit()
    cursor.close()
    connection.close()
    print("Table read successfully")

def insert_new_data():
    connection = get_connection()
    connection.autocommit(False)
    cursor = connection.cursor()
    try:
        print("Start inserting Data...")
        cursor.execute("insert into DATA_MAPPING VALUES(11, 'PAY_01', 'card_num', 'payment_token', 'Active')")
        print("Creating Savepoint sp1...")
        cursor.execute("Savepoint sp1")
        try:
            cursor.execute("insert into DATA_MAPPING VALUES(12, 'PAY_02', 'expiry_dt', 'valid_thru', 'Active')")
            print("Creating Savepoint sp2...")
            cursor.execute("Savepoint sp2")
            try:
                cursor.execute("insert into DATA_MAPPING VALUES(12, 'PAY_02_DUP', 'cvv', 'secure_code', 'Active')")
                print("Creating Savepoint sp3...")
                cursor.execute("Savepoint sp3")

            except Exception as e:
                print("Error in third insert, rolling back to Savepoint sp2...", e)
                cursor.execute("rollback to Savepoint sp2")
        except Exception as e:
            print("Error in second insert, rolling back to Savepoint sp1...", e)
            cursor.execute("rollback to Savepoint sp1")
        print("Committing Transactions...")
        connection.commit()
    except Exception as e:
        connection.rollback()
        print(" Error in transaction", e)

    cursor.close()
    connection.close()

def delete_data():
    connection = get_connection()
    cursor = connection.cursor()
    sql = "delete from DATA_MAPPING where mappingID =1"
    cursor.execute(sql)
    connection.commit()
    cursor.close()
    print("Data deleted successfully")

# ----------------------------------------------------------------------------------------------------------




get_connection()
create_table()
insert_data()

param = {
    'mappingID': 11,
    'mappingCode': '',
    'sourceField': '',
    'targetField': '',
    'status': '',
    'pageno': 1,
    'pagesize': 20

}

insert_new_data()
read_data(param = {})
delete_data()

