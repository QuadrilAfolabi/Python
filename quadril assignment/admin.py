import pymysql
mycon = pymysql.connect(host='127.0.0.1', user='root', passwd='' , database='mydatadb')
mycursor = mycon.cursor()

mycursor.execute("CREATE DATABASE mydatadb")
mycursor.execute("SHOW DATABASES")
for db in mycursor:
    print(db)

mycursor.execute("CREATE TABLE Admin_que(Que_ID INT(4) NOT NULL PRIMARY KEY AUTO_INCREMENT, Questions VARCHAR(100), Option1 VARCHAR(50), Option2 VARCHAR(50), Option3 VARCHAR(50), Answers VARCHAR(50))")
for table in mycursor: 
    print(table)
for i in range(10):
    que = input("what is the que?")
    opt1= input("what is the opt1>>")
    opt2=input("what is the opt2>>")
    opt3= input("what is the opt3>>")
    answer= input('what is the answer?')
    myquery = "INSERT INTO admin_que (Questions, Option1, Option2, Option3, Answers) VALUES(%s, %s, %s, %s, %s)"
    val = (que, opt1, opt2, opt3, answer)
    mycursor.execute(myquery, val)
    mycursor.executemany((myquery, val),())
    mycon.commit()
    print(mycursor.rowcount, "records inserted successfully")

sql = "DROP TABLE admin_que"
mycursor.execute(sql)

