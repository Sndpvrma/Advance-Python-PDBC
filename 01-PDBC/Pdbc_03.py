# import pymysql
#
# connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='pymysql')
# cursor = connection.cursor()
# sql = "update pymsql set name = 'ramesh' where sn = 7"
# cursor.execute(sql)
# connection.commit()
# connection.close()
#
# print('Data Updated Successfully')

import pymysql
connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='pymysql')
cursor = connection.cursor()
# sql = "update pymsql set name = 'rocky' where sn = 11"
sql = "update pymsql set last_name = 'bhai' where sn = 11"
cursor.execute(sql)
connection.commit()
connection.close()
print("data updated successfully")