


# Python Database (Mysql)
# To download mysql connector user: pip install mysql-connector

import mysql.connector
mycon = mysql.connector.connect(host='127.0.0.1', user='root', passwd='' , database='cbtTestdb')
mycursor = mycon.cursor()

# mycursor.execute("CREATE DATABASE cbtTestdb")
# mycursor.execute("SHOW DATABASES")
# for db in mycursor:
#     print(db)

# mycursor.execute("CREATE TABLE customers (ctm_id INT(4), Ful_Name VARCHAR(20), Address VARCHAR(50), Phone VARCHAR(11), Password VARCHAR(20))")
# mycursor.execute("SHOW TABLES")

# for table in mycursor: 
#     print(table)
# mycursor.execute("ALTER TABLE customers CHANGE ctm_id ctm_id INT(4) PRIMARY KEY AUTO_INCREMENT")

# mycursor.execute("ALTER TABLE customers ADD UNIQUE(Phone);")

# myquery = "INSERT INTO customers (Ful_Name, Address, Phone, Password) VALUES(%s, %s, %s, %s)"
# val = ('paul Adesola', 'Moniya', '07067397708', '76784')
# mycursor.execute(myquery, val)
# mycon.commit()

# fulname = input('enter your name >') 
# address = input('enter your address')
# phone = input('enter your phone number')
# password = input('enter your Password')
# myquery = "INSERT INTO customers (Ful_Name, Address, Phone, Password) VALUES(%s, %s, %s, %s)"
# val = (fulname, address, phone, password)
# mycursor.execute(myquery, val)
# # mycursor.executemany((myquery, val),())
# mycon.commit()
# print(mycursor.rowcount, "records inserted successfully")

# query = "SELECT * FROM customers"
# mycursor.execute(query)
# output = mycursor.fetchall()
# print(output)
# for inf in output:
#   print(inf)

# mmm = "SELECT * FROM customers WHERE Phone = 07067397708"
# val = ("07067397708",)
# mycursor.execute(mmm)
# nm = mycursor.fetchone()
# print(nm)

# query = "SELECT * FROM customers WHERE Ful_Name LIKE '%th%'"
# query = "SELECT Ful_Name, Phone FROM customers"
# query = "SELECT * FROM customers ORDER BY ful_Name DESC"
# val = ('09013140700', val)
# number  = input("Enter your phone number ")
# pin = input("Enter your pin ")
# query = "SELECT Ful_Name, Address FROM customers WHERE Phone=%s AND Password=%s"
# val = (number, pin)
# mycursor.execute(query, val)
# # myreg = mycursor.fetchall()
# myreg = mycursor.fetchone()
# print(myreg)
# for info in myreg:
#     print(info)
# mycon.commit()
# print(mycursor.rowcount, 'selected successfuly')
# mycon.close()

# num = input("enter your number>> ")
# sql = "UPDATE customers SET  Password='2123' WHERE Phone=%s"
# val =(num,)
# mycursor.execute(sql, val)
# mycon.commit()
# print(mycursor.rowcount, 'record updated successfuly')

# sql = "DELETE FROM customers WHERE Phone=%s"
# val =('07067307758',)
# mycursor.execute(sql, val)
# mycon.commit()
# print(mycursor.rowcount, 'record deleted successfuly')

# sql = "DROP TABLE customers"
# mycursor.execute(sql)

