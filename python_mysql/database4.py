import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="Luminar",
auth_plugin='mysql_native_password'
)
print(db)
cursor = db.cursor()

sql = """select * from Employee
         where INCOME>22000
          """
try:
    cursor.execute(sql)
    data=cursor.fetchall()
    print(data)
except Exception as e:
    print(e.args)
db.close()