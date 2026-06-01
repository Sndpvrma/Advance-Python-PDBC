import pymysql

def get_connection():
    return pymysql.connect(host='localhost', port = 3306, user='root', password='root', database='module')

def create_table():
    connection = get_connection()
    cursor = connection.cursor()
    sql = """CREATE table if not exists college_system(
    studentId BIGINT primary key,
    studentName VARCHAR(255),
    branch VARCHAR(255),
    semester INT,
    cgpa DOUBLE(10, 2)
    )
    """
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("Table created successfully")

def insert(data = {}):
    studentId = data['studentId']
    studentName = data['studentName']
    branch = data['branch']
    semester = data['semester']
    cgpa = data['cgpa']

    connection = get_connection()
    cursor = connection.cursor()
    sql = "INSERT into college_system values(%s,%s,%s,%s,%s)"
    data = (studentId, studentName, branch, semester, cgpa)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("college_system inserted successfully")

def read(params = {}):
    studentId = params.get('studentId', 0)
    studentName = params.get('studentName', '')
    branch = params.get('branch', '')
    semester = params.get('semester', 0)
    cgpa = params.get('cgpa', 0)
    pageNo = params.get('pageNo', 0)
    pageSize = params.get('pageSize', 10)

    connection = get_connection()
    cursor = connection.cursor()

    sql = "SELECT * from college_system where 1=1"
    if studentId != 0:
        sql += " and studentId = " + str(studentId)
    if studentName != '':
        sql += " and studentName like '" + studentName + "%'"
    if branch != '':
        sql += " and branch like '" + branch + "%'"
    if semester != 0:
        sql += " and semester = " + str(semester)
    if cgpa != 0:
        sql += " and cgpa = " + str(cgpa)

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
    print("College_system table read successfully")

def update(param = {}):
    studentId = param['studentId']
    studentName = param['studentName']
    branch = param['branch']
    semester = param['semester']
    cgpa = param['cgpa']

    connection = get_connection()
    cursor = connection.cursor()
    sql = "update college_system set studentName = %s, branch = %s, semester = %s, cgpa = %s where studentId = %s"
    data = (studentId, studentName, branch, semester, cgpa)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("College_system updated successfully")

def delete(orderId):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "delete from college_system where orderId = %s"
    data = (orderId,)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("college_system deleted successfully")

#----------------------------------------------------------------------------------------------

# create_table()
data = {
    'studentId' : 2,
    'studentName' : 'rohan',
    'branch' : 'CSE',
    'semester' : 8,
    'cgpa' : 8.30
}

# insert(data)

params = {
    'studentId' : 1,
    'studentName' : 'nitin',
    'branch' : 'CS',
    'semester' : 7,
    'cgpa' : 8.2,
    'pageNo' : 1,
    'pageSize' : 10
}

param = {
    'studentId' : 1,
    'studentName' : 'nitin',
    'branch' : 'CSE',
    'semester' : 7,
    'cgpa' : 8.20,
}

# update(param)
read(params)
# delete(0)