import mysql.connector

conn=mysql.connector.connect(host="localhost", user="root", passwd="Mysql123#", database="Python")

mycursor=conn.cursor()

mycursor.execute("show databases")

for i in mycursor:
    print(i)

mycursor.execute("select * from emp")

for i in mycursor:
    print(i)

#to store data in cursor
mycursor.execute("select * from emp")
record=mycursor.fetchall()

for i in record:
    print(i)

mycursor.execute("select * from emp")
record=mycursor.fetchone() #to fetch one record
print(record)