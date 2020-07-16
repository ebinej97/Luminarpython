import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="Luminar",
auth_plugin='mysql_native_password'
)
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

sql = """CREATE TABLE EMPLOYEE(
         FIRST_NAME CHAR(20) ,
         LAST_NAME CHAR(20),
         AGE INT,
         SEX CHAR(1),
         INCOME FLOAT)"""

cursor.execute(sql)
db.close()