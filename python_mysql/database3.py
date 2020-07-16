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

sql = """INSERT INTO Employee(
         FIRST_NAME,
         LAST_NAME,
         AGE,
         SEX,
         INCOME) values('AJU','V',25,'M',22000)"""
try:
    cursor.execute(sql)
    db.commit()  #save changes
except Exception as e:
    db.rollback()
    print(e.args)
finally:
    db.close()