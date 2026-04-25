# import pymysql
#
# connection = pymysql.connect(host = 'localhost', port = 3306, user = 'root', passwd = 'root', db = 'pymysql')
# cursor = connection.cursor()
# # sql = "Insert INTO pymsql VALUES (5, 'Raju', 'Yadav', 70000)" old program
# sql = "INSERT INTO pymsql VALUES (%s, %s, %s, %s)"
# data = [
#     (6, 'Amit', 'Sharma', 50000),
#     (7, 'Soniya', 'Verma', 60000),
#     (8, 'Rahul', 'Singh', 45000)
# ]
# # cursor.execute(sql) old program
# cursor.executemany(sql, data)
# connection.commit()
# connection.close()
# # print("Data Inserted Successfully")  old program
# print(f"Total {len(data)} Rows Inserted Successfully")

import pymysql

connection = pymysql.connect(host = 'localhost', port = 3306, user = 'root', passwd = 'root', db = 'pymysql')
cursor = connection.cursor()
# sql = "insert into pymsql values(9, 'ramesh', 'kumar', 89000)"
sql = "INSERT INTO pymsql VALUES (%s, %s, %s, %s)"
data = [
    (10, 'sam', 'altmen', 92000),
    (11, 'larry', 'page', 96000),
    (12, 'elon', 'musk', 88000)
]
cursor.executemany(sql, data)
connection.commit()
connection.close()
# print("data inserted successfully")
print(f"Total {len(data)} Rows Inserted Successfully")
