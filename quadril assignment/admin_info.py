import pymysql
mycon = pymysql.connect(host='127.0.0.1', user='root', passwd='' , database='mydatadb')
mycursor = mycon.cursor()

mycursor.execute("CREATE TABLE Admin_info(First_Name VARCHAR(20), Last_Name VARCHAR(20), Email VARCHAR(50), Password VARCHAR(20))")
mycursor.execute("SHOW TABLES")
for db in mycursor:
    print(db)
firstname = input('enter your first name >') 
lastname = input('enter your lastname')
email = input('enter your email>>>')
password = input('enter your Password>>>>')
mycity = "INSERT INTO admin_info (First_Name, Last_Name, Email, Password) VALUES(%s, %s, %s, %s)"
val = (firstname, lastname, email, password)
mycursor.execute(mycity, val)
mycursor.executemany((mycity, val),())
mycon.commit()
print(mycursor.rowcount, "details inserted successfully")

bp = ("SELECT * FROM admin_info WHERE Email = %s AND Password = %s ")
val = (email, password)
mycursor.execute(bp, val)
if mycursor.fetchone():
    print("yes")
else:
    print("no")

