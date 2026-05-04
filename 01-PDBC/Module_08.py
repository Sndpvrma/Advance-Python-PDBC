import pymysql

def get_connection():
    return pymysql.connect(host='localhost', port = 3306, user='root', password='root', db='module')

def create_table():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("Drop table if exists Scheduler_job")
    sql = """Create Table if not exists Scheduler_job(
    jobID BIGINT PRIMARY KEY,
    jobCode VARCHAR(100),
    jobName VARCHAR(100),
    cronExpression VARCHAR(100),
    status VARCHAR(100)
    )
    """
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("Table created successfully")

def insert_table():
    connection = get_connection()
    cursor = connection.cursor()
    sql = "insert into Scheduler_job VALUES(%s, %s, %s, %s, %s)"
    data = [
        (1, 'EMAIL_SENDER', 'Daily Newsletter', '0 0 9 * * *', 'ACTIVE'),
        (2, 'DB_BACKUP', 'System Backup', '0 0 22 * * *', 'ACTIVE'),
        (3, 'LOG_CLEANUP', 'Old Log Purge', '0 0 1 * * SUN', 'ACTIVE'),
        (4, 'REPORT_GEN', 'Monthly Sales Report', '0 0 1 1 * *', 'INACTIVE'),
        (5, 'CACHE_EVICT', 'Redis Cache Refresh', '0 0/15 * * * *', 'ACTIVE'),
        (6, 'PAYMENT_RECON', 'Payment Reconciliation', '0 30 23 * * *', 'ACTIVE'),
        (7, 'USER_SYNC', 'External LDAP Sync', '0 0 4 * * *', 'ACTIVE'),
        (8, 'NOTIF_PUSH', 'Marketing Notifications', '0 0 18 * * *', 'INACTIVE'),
        (9, 'FILE_SCAN', 'Malware File Scan', '0 0 3 * * *', 'ACTIVE'),
        (10, 'SUBS_EXPIRY', 'Check Subscription Expiry', '0 0 0 * * *', 'ACTIVE')
    ]
    cursor.executemany(sql, data)
    connection.commit()
    connection.close()
    print("Table inserted successfully")

def read_table(params = {}):
    jobID = params.get('jobID', 0)
    jobCode = params.get('jobCode', '')
    jobName = params.get('jobName', '')
    cronExpression = params.get('cronExpression', '')
    status = params.get('status', '')
    pageno = params.get('pageno', 0)
    pagesize = params.get('pagesize', 10)

    connection = get_connection()
    cursor = connection.cursor()

    sql = "select * from Scheduler_job where 1=1"
    if jobID != 0:
        sql += " AND jobID = " + str(jobID)
    if jobCode != '':
        sql += " AND jobCode like '" + jobCode + "%'"
    if jobName != '':
        sql += " AND jobName like '" + jobName + "%'"
    if cronExpression != '':
        sql += " AND cronExpression like '" + cronExpression + "%'"
    if status != '':
        sql += " AND status like '" + status + "%'"

    if pageno > 0:
        offset = (pageno - 1) * pagesize
        sql += " LIMIT " + str(offset) + ", " + str(pagesize)
    print("sql=> ", sql)
    cursor.execute(sql)
    print("Data of Scheduler_job:")
    results = cursor.fetchall()
    for data in results:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4])
    connection.commit()
    connection.close()
    print("Table read successfully")


def update_table():
    connection = get_connection()
    connection.autocommit(False)
    cursor = connection.cursor()
    try:
        print("Start Inserting Data")
        cursor.execute("insert into Scheduler_job VALUES(11,'TEMP_CLEAN', 'Temporary File Cleanup', '0 0 5 * * *', 'ACTIVE')")
        print("Creating Savepoint sp1...")
        cursor.execute("Savepoint sp1")
        try:
            cursor.execute("insert into Scheduler_job VALUES(12, 'HEALTH_CHK', 'System Health Check', '0 */30 * * * *', 'ACTIVE')")
            print("Creating Savepoint sp2...")
            cursor.execute("Savepoint sp2")
            try:
                cursor.execute("insert into Scheduler_job VALUES(12, 'ERROR_JOB', 'This should fail', '* * * * * *', 'INACTIVE')")
                print("Creating Savepoint sp3...")
                cursor.execute("Savepoint sp3")
            except Exception as e:
                print("Error in third insert, rolling back to Savepoint sp2")
                cursor.execute("roll back to Savepoint sp2")
        except Exception as e:
            print("Error in second insert, rolling back to Savepoint sp1")
            cursor.execute("roll back to Savepoint sp1")
        print("Commiting transaction")
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("Error in transaction", e)
    finally:
        connection.close()
    print("Table updated successfully")

def delete_table():
    connection = get_connection()
    cursor = connection.cursor()
    sql = " delete from Scheduler_job where jobID = 9"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("Table deleted successfully")


create_table()
insert_table()

params = {
    'jobID': 9,
    'jobCode': '',
    'jobName': '',
    'cronExpression': '',
    'status': '',
    'pageno': 1,
    'pagesize': 10
}

update_table()

read_table(params = {})
# delete_table()
