# import pymysql
#
# connection = pymysql.connect(host = 'localhost', port = 3306, user = 'root', passwd = 'root', db = 'pymysql')
# cursor = connection.cursor()
#
# sql = 'select * from pymsql'
# cursor.execute(sql)
# results = cursor.fetchall()
#
# for data in results:
#     print(data[0],data[1],data[2],data[3])
# connection.commit()
# connection.close()
#
# print('Data Read Successfully')
#
# import pymysql
# connection = pymysql.connect(host = 'localhost', port = 3306, user = 'root', passwd = 'root', db = 'pymysql')
# cursor = connection.cursor()
# sql = "select * from pymsql;"
# cursor.execute(sql)
# results = cursor.fetchall()
# for data in results:
#     print(data)
# connection.commit()
# connection.close()
# print("data read successfully")

import pymysql
connection = pymysql.connect(host = 'localhost', port = 3306, user = 'root', passwd = 'root', db = 'testdemo')
cursor = connection.cursor()
sql = "select * from marksheet;"
cursor.execute(sql)
results = cursor.fetchall()
for data in results:
    print(data)
connection.commit()
connection.close()
print("data read successfully")