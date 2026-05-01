import pymysql

def get_connection():
    return pymysql.connect(host='localhost', port=3306, user='root', password='root', db='module')

def call_procedure():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.callproc('getMappingDetails')
    result = cursor.fetchall()
    for data in result:
        print(data)

    connection.commit()
    connection.close()

def procedure(m_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.callproc('getMapping', [m_id])
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4])
    connection.commit()
    connection.close()

def create_procedure():
    connection = get_connection()
    cursor = connection.cursor()
    sql = """
    CREATE PROCEDURE IF NOT EXISTS updateMappingStatus(IN p_id INT, IN p_status VARCHAR(50))
    BEGIN
         UPDATE DATA_MAPPING SET status = p_status WHERE mappingID = p_id;
    END
    """
    try:
        cursor.execute(sql)
        print("Procedure Created Successfully by Python!")
    except Exception as e:
        print("Error Creating procedure", e)
    finally:
        cursor.close()
        connection.close()

def use_procedure():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.callproc('updateMappingStatus', [3, 'Inactive'])
    connection.commit()
    print("Status Updated Using Python!")
    cursor.close()
    connection.close()



procedure(5)
create_procedure()
use_procedure()
call_procedure()
