import pymysql

def create_table():
    connection = pymysql.connect(host = 'localhost', port = 3306, user = 'root', password = 'root', db = 'Module')
    cursor = connection.cursor()
    sql = """CREATE TABLE block_list (  blockId BIGINT PRIMARY KEY,
        blockCode VARCHAR(50),
        userName VARCHAR(100),
        reason VARCHAR(255),
        status VARCHAR(50)
        )
        """
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("Data Created Successfully")

def insert_block():
    connection = pymysql.connect(host='localhost', port = 3306,  user='root', password='root', db='Module')
    cursor = connection.cursor()
    sql = "INSERT INTO block_list VALUES(%s, %s, %s, %s, %s)"
    data = [
        (1, 'B001', 'Rahul', 'Spamming', 'ACTIVE'),
        (2, 'B002', 'Anjali', 'Policy Violation', 'BLOCKED'),
        (3, 'B003', 'Vikram', 'Fake Account', 'PENDING'),
        (4, 'B004', 'Sanya', 'Abusive Behavior', 'ACTIVE'),
        (5, 'B005', 'Amit', 'Payment Fraud', 'BLOCKED')
    ]
    cursor.executemany(sql, data)
    connection.commit()
    connection.close()
    print("Data Inserted Successfully")

def view_blocks():
    connection = pymysql.connect(host='localhost', port = 3306,  user='root', password='root', db='Module')
    cursor = connection.cursor()
    sql = "SELECT * FROM block_list"
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        print(row)
    connection.commit()
    connection.close()

def update_block_list():
    connection = pymysql.connect(host='localhost', port = 3306,  user='root', password='root', db='Module')
    cursor = connection.cursor()
    sql = "Update Block_list SET reason = 'EMAIL SPAM' where blockId = 4"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("Data Updated Successfully")

def delete_block():
    connection = pymysql.connect(host='localhost', port = 3306,  user='root', password='root', db='Module')
    cursor = connection.cursor()
    sql = "Delete From Block_list where blockId = 3"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("Data Deleted Successfully")

create_table()
insert_block()
view_blocks()
update_block_list()
delete_block()


