# age = 36.56
# name = "my name "
# txt = "is john, i am "

# print(f"{name.upper()}{txt.upper()}{age}")

# print(name+""+txt+""+age)
# print(f"{name}{txt}{age}")

# result=[]
# for i in range(6):
#     inp =input(">>>")
#     result.append(inp)
# print(result)




# dollar =float(input("enter the dollar amount>>>")) 
# rate = float(input("what is the naira rate>>>>"))
# naira = dollar * rate
# print(f"The convention of ${dollar} to naira with #{rate} coversion rate is #{naira}")


# naira =float(input("enter the naira amount>>>")) 
# rate = float(input("what is the rate>>>>"))
# dollar = naira/rate
# print(f"The conversion of #{naira} to dollar is ${dollar} using {rate} conversion rate")

# principal =int(input("what is the the principal"))
# rate =float(input("what is rate"))
# time =int(input("what is time"))
# a = principal * rate * time
# print(a)

#  CompoundInterest = P(1+r/n)^nt
# principal = float(input("enter the principal amount >>"))
# time=int(input("enter the time>>"))
# rate=float(input("enter the rate >>"))
# compound_per_unit =int(input("enter the number of time interest in compound >>"))
# compound_interest = (principal * ((1 + rate/compound_per_unit)) ** (compound_per_unit * time))
# print("Compound interest =", compound_interest)


# name = range(6)
# age = []
# for i in name:
#  age.append(input("what is your name>>"))
# total=[]
# for i in age:
#  total.append(i)
# #   print(total)
# name= range (6)
# name2 = []
# for i in name:
#     name2.append(input("what is your name>>"))
# total= []
# for i in name2:
#     total.append(i)
# print(total)


# n = {}
# m = int(input('Enter the name of your nested dictionary '))
# for i in range(2):
#     dict_name = input("Name")
#     n[dict_name] = {}
#     name = input("what is the name >>")
#     level = int(input("what is the level >>"))
#     age= input("what is the age >>")
#     n[dict_name]["name"]= name
#     n[dict_name]["age"]= age
#     n[dict_name]["level"]= level
# print(n)
    
# USSD
# reg = {input("what is usernsme >>") : input("what is the password >>")}
# list= []
# list.append(reg)
# # print(list)
# i = {input("What's your username>>") : input("What's your password>>")}
# if i in list:
#     print("Login Sucessful")
# if i not in list:
#   print("incorrect login details")

# # USSD
# print("Create your account")
# username= input("create your username")
# passcode= input("create your password")
# reg=[username, passcode]
# print("Account create successful")
# print("Login into your Account")
# loguser = input("what is username >>") 
# loggpass= input("what is the password >>")


# if (loguser in reg) and (loggpass in reg):
#     print("Login Sucessful")
# elif (loguser not in reg ) and (loggpass not in reg):
#     print("Account not found")
# else:
#     print("incorrect details")

#     num = int(input("what is the number >>")) 
# y = 1

# for i  in range(1, num+1):
#     for j in range(1, i+1 ):
#         print(y, end =" ") 
#         y += 1
#     print()  
# 
# multiplication table 
# # num= 2
# for i in range(13): 

#      print(num, "x", i, "=", num*i) 
     
# num = int(input("what is the number >>"))
# for i in range (1, 13):
#     print(num, 'x', i, '=', i*num)
# 
# 
# # num=int(input("what is the number>>"))
# i = 0
# while i < 13:
#     c=num*i 
#     print(num, "*", i, '=', c) 
#     i += 1  

# ZenithBank USSD
# m =(input("what is the code >>"))
# n= ("*966#")
# menu = ("Eazybanking \n 1>Transfers \n 2>Airtime \n 3>Data \n 4>Bills Payment \n 5>Check Balance \n 6>Open Account \n 7>Card Requests \n 8>Register \n 9>Next")
# j = ("10> Self Service \n 11> Stop debit on account \n 12>Agent Banking \n 13>Insurance \n 14>EazyMoney \n 15>Back")
# if m == n:
#       print(menu)
# else:
#       print("error")
# g=(input("What is next >>"))
# if (g in menu):
#       print(j)
# else:
#       print(menu)

# class Father:
#    def __init__(self):
#       self.n= 6


# def fact(n):
#    g = 1
#    for i in range(1, n+1):
#       g *= i
#    return g
# n = 6
# r= 3
# city = fact(n)/((fact(n-r))*fact(r))
# print(city)



# Zenith USSD
# print("Create your Account >>")
# username=input("Enter your name>>")
# passcode=input("Enter your password>>")
# reg=[username, passcode]
# print("Account created successfully")
# print("Login into your Account>>")
# loguser=input("What is the your username>>")
# logpass=input("What is your password?")
# city=[loguser, logpass]
# if (loguser in reg) and (logpass in reg):
#     print("login successfully")
# elif(loguser not in reg) and (logpass not in reg):
#     print("Account not found")
# else:
#     print("incorrect informaton")
# while reg==city:
#     print()
#     reg+=city
# m =(input("Enter your ussdcode >>"))
# n= ("*966#")
# menu = ("Eazybanking \n 1>Transfers \n 2>Airtime \n 3>Data \n 4>Bills Payment \n 5>Check Balance \n  6>Open Account \n 7>Card Requests \n 8>Register \n 9>Next")
# j = ("10> Self Service \n 11> Stop debit on account \n 12>Agent Banking \n 13>Insurance \n 14>EazyMoney \n 15>Back")
# if m == n:
#     print(menu)

# g=(input("What is next >>"))
# if (g in menu):
#      print(j)  
# else:
#     print("error")


# def city(n):
#     num = 1 
#     for i in range(0, n +1 ): 
#         for j in range(1, i+1):
#             print(num, end=' ')
#             num += 1
#         print()
# city(5)


# import re
# city = input("what is your gmail?>>")
# bop = re.search("@gmail.com$", city)
# if bop:
#     print("valid Email")
# else:
#     print("invalid")

# import datetime
# import time
# city=datetime.datetime(2022, 7, 21, 2, 46)
# while True:
#  time.sleep(1)
#  if city.strftime("%I") == '2' and city.strftime("%M") =='46':
#     print("successful")
#     break
#  else:
#     print("not succ") 
#     break
 



