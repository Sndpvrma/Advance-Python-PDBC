# import pymysql
#
# connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='pymysql')
# cursor = connection.cursor()
# sql = "Delete from pymsql where sn = 6"
# cursor.execute(sql)
# connection.commit()
# connection.close()
#
# print('Data Deleted Successfully')

import pymysql
connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='pymysql')
cursor = connection.cursor()
sql = "delete from pymsql where sn = 12"
cursor.execute(sql)
connection.commit()
connection.close()

print("data deleted successfully")
