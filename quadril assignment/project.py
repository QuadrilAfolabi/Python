import pymysql
mycon = pymysql.connect(host='127.0.0.1', user='root', passwd='' , database='mydatadb')
mycursor = mycon.cursor()

# ADMIN INFORMATION

# mycursor.execute("CREATE TABLE Admin_info(First_Name VARCHAR(20), Last_Name VARCHAR(20), Email VARCHAR(50), Password VARCHAR(20))")
# mycursor.execute("SHOW TABLES")
# for db in mycursor:
    # print(db)

# firstname = input('enter your first name >') 
# lastname = input('enter your lastname')
# email = input('enter your email>>>')
# password = input('enter your Password>>>>')
# mycity = "INSERT INTO admin_info (First_Name, Last_Name, Email, Password) VALUES(%s, %s, %s, %s)"
# val = (firstname, lastname, email, password)
# mycursor.execute(mycity, val)
# mycursor.executemany((mycity, val),())
# mycon.commit()
# print(mycursor.rowcount, "details inserted successfully")

# bp = ("SELECT * FROM admin_info WHERE Email = %s AND Password = %s ")
# val = (email, password)
# mycursor.execute(bp, val)
# if mycursor.fetchone():
#     print("yes")
# else:
#     print("no")

# ADMIN QUESTIONS

# mycursor.execute("CREATE TABLE Admin_que(Que_ID INT(4) NOT NULL PRIMARY KEY AUTO_INCREMENT, Questions VARCHAR(100), Option1 VARCHAR(50), Option2 VARCHAR(50), Option3 VARCHAR(50), Answers VARCHAR(50))")
# for table in mycursor: 
#     print(table)
# for i in range(10):
#     que = input("what is the que?")
#     opt1= input("what is the opt1>>")
#     opt2=input("what is the opt2>>")
#     opt3= input("what is the opt3>>")
#     answer= input('what is the answer?')
#     myquery = "INSERT INTO admin_que (Questions, Option1, Option2, Option3, Answers) VALUES(%s, %s, %s, %s, %s)"
#     val = (que, opt1, opt2, opt3, answer)
#     mycursor.execute(myquery, val)
#     mycursor.executemany((myquery, val),())
#     mycon.commit()
#     print(mycursor.rowcount, "records inserted successfully")

# sql = "DROP TABLE admin_que"
# mycursor.execute(sql)

# USERS

# mycursor.execute("CREATE TABLE user(First_Name VARCHAR(20), Last_Name VARCHAR(20), Email VARCHAR(50), Password VARCHAR(20))")
# mycursor.execute("SHOW TABLES")
# for db in mycursor:
#     print(db)
# city = input("Are you a New User or Old User?").lower()
# if city == ("New User").lower():
#     print("Input your details to create your profile.")
#     firstname = input('Enter your first name>>>') 
#     lastname = input('Enter your lastname>>>')
#     email = input('Enter your email>>')
#     password = input('Enter your Password>>')
#     mycity = "INSERT INTO user (First_Name, Last_Name, Email, Password) VALUES(%s, %s, %s, %s)"
#     val = (firstname, lastname, email, password)
#     mycursor.execute(mycity, val)
#     mycursor.executemany((mycity, val),())
#     mycon.commit()
#     print(mycursor.rowcount, "details inserted successfully")
# else:
#     print("Login with your details.")
# def paul():
#     score = 0
#     city = input("Are you a New User or Old User?").lower()
#     if city == ("New User").lower():
#         print("Not accepting any new user. Thank You")
#     elif city == ("Old User").lower():
#         print("Login with your details.")
#         email = input('Enter your email>>')
#         password = input('Enter your Password>>')
#         bp = ("SELECT * FROM user WHERE Email = %s AND Password = %s ")
#         val = (email, password)
#         mycursor.execute(bp, val) 

#         if mycursor.fetchone():

#             print("Welcome to your computer based test")
#             print("You have question 1 to 10")

#             for i in range(3):
#                 question = input("Choose your question number>>>")
#                 query = "SELECT * FROM admin_que WHERE Que_ID = %s"
#                 val =(question, )
#                 mycursor.execute(query, val)
#                 py = mycursor.fetchone() 
#                 print(py[1])
#                 print(py[2])
#                 print(py[3])
#                 print(py[4])

#                 ans = (input(">>>")).upper()
#                 myquery="SELECT * FROM admin_que WHERE Answers = %s"
#                 val= (ans, )
#                 mycursor.execute(myquery,val)
#                 mycursor.fetchall()
#                 if py[-1] == ans:
#                     score = score + 1
#                 else:
#                     score = 0
#             print(f"you have {score} point")
#         else:
#             print("Invalid details")

#     else:
#         print("wrong input")
# paul()


