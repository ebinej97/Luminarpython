import mysql.connector
db=mysql.connector.connect(         #open database connection
    host="localhost",
    user="root",
    password="Password@123",
auth_plugin='mysql_native_password'
) #close database connection

#prepare a cursor object using cursor() method
cursor=db.cursor()

#execute SQL query usign execute() method.
cursor.execute("SELECT VERSION()")

#fetch a single row using fetchone() method.
data=cursor.fetchone()
print("Database version:",data)

#disconnect from server
db.close()