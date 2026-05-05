import pymysql

def get_connection():
    return pymysql.connect(host='localhost', port=3306, user='root', password='root', db='module')

def create_table():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("Drop table if exists DATA_SOURCE")
    sql = """CREATE TABLE if not exists DATA_SOURCE(
    dataSourceID BIGINT PRIMARY KEY,
    dataSourceCode VARCHAR(50),
    sourceName VARCHAR(50),
    connectionType VARCHAR(50),
    status VARCHAR(50)
    )
    """
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("Table created successfully")

def insert_data():
    connection = get_connection()
    cursor = connection.cursor()
    sql = "INSERT INTO DATA_SOURCE VALUES(%s, %s, %s, %s, %s)"
    data = [
        (1, 'SRC-1001', 'HR_Portal', 'MySQL', 'Active'),
        (2, 'SRC-1002', 'Finance_Ledger', 'Oracle', 'Active'),
        (3, 'SRC-1003', 'Inventory_DB', 'PostgreSQL', 'Inactive'),
        (4, 'SRC-1004', 'Sales_Cloud', 'REST_API', 'Active'),
        (5, 'SRC-1005', 'Marketing_Ads', 'JSON', 'Active'),
        (6, 'SRC-1006', 'Customer_Support', 'Zendesk', 'Active'),
        (7, 'SRC-1007', 'Web_Analytics', 'BigQuery', 'Maintenance'),
        (8, 'SRC-1008', 'Mobile_Logs', 'Firebase', 'Active'),
        (9, 'SRC-1009', 'Payment_Gateway', 'Stripe', 'Pending'),
        (10, 'SRC-1010', 'Shipping_API', 'FedEx_Service', 'Active')
    ]
    cursor.executemany(sql, data)
    connection.commit()
    connection.close()
    print("Data inserted successfully")

def read_data(params = {}):
    dataSourceID = params.get('dataSourceID', 0)
    dataSourceCode = params.get('dataSourceCode', '')
    sourceName = params.get('sourceName', '')
    connectionType = params.get('connectionType', '')
    status = params.get('status', '')
    pageno = params.get('pageno', 0)
    pagesize = params.get('pagesize', 0)

    connection = get_connection()
    cursor = connection.cursor()

    sql = "SELECT * FROM DATA_SOURCE WHERE 1=1"
    if dataSourceID != 0:
        sql += " AND dataSourceID = " + str(dataSourceID)
    if dataSourceCode != '':
        sql += " AND dataSourceCode like '" + dataSourceCode + "%'"
    if sourceName != '':
        sql += " AND sourceName like '" + sourceName + "%'"
    if connectionType != '':
        sql += " AND connectionType like '" + connectionType + "%'"
    if status != '':
        sql += " AND status like '" + status + "%'"

    if pageno > 0:
        offset = (pageno - 1) * pagesize
        sql += " LIMIT " + str(offset) + ", " + str(pagesize)

    print("sql=> ", sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4])
    connection.commit()
    connection.close()
    print("Data read successfully")

def update_data():
    connection = get_connection()
    connection.autocommit(False)
    cursor = connection.cursor()
    try:
        print("Start Inserting data...")
        cursor.execute("insert into DATA_SOURCE VALUES(11, 'SRC-1011', 'Backup_Server', 'FTP', 'Active')")
        print("Creating Savepoint sp1...")
        cursor.execute("Savepoint sp1")
        try:
            cursor.execute("insert into DATA_SOURCE VALUES(12, 'SRC-1012', 'Testing_Env', 'SQLite', 'Active')")
            print("Creating Savepoint sp2...")
            cursor.execute("Savepoint sp2")
            try:
                cursor.execute("insert into DATA_SOURCE VALUES(12, 'SRC-1012', 'Legacy_Archive', 'Mainframe', 'Inactive')")
                print("Creating Savepoint sp3...")
                cursor.execute("Savepoint sp3")
            except Exception as e:
                print("Error in third insert, rolling back to Savepoint sp2")
                cursor.execute("roll back to Savepoint sp2")
        except Exception as e:
            print("Error in second insert, rolling back to Savepoint sp1")
            cursor.execute("roll back to Savepoint sp1")
        print("Commiting Transaction")
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("Error in transaction", e)
    finally:
        connection.close()
    print("Table Updated Successfully")

def delete_table():
    connection = get_connection()
    cursor = connection.cursor()
    sql = "Delete from DATA_INSERT WHERE dataSourceID = 8"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("Table Deleted successfully")

get_connection()
create_table()
insert_data()

params = {
    'dataSourceID' : 7,
    'dataSourceCode' : '',
    'sourceName' : '',
    'connectionType' : '',
    'status' : '',
    'pageno' : 1,
    'pagesize' : 10,
}

update_data()
read_data(params = {})
delete_table()
