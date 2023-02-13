 # print("my name is ayo and i need $20")
# name =("ayo", "quadril", "city")
# name2 = "john"
# name3 = "mayowa"
# money = 50 

# print('come here')
# print("come")
# print(""" come here""")
# print (''' come here''')

# a ="Hello "
# b =" World"
# c = a + b
# d = a+""+b

# print(d)
 
# a = 3
# a = 33
# print(a==a)

# a = 5
# b = ++5
# print(b)

# a, b = 2, 3
# a,b,c = 4, 5, 6
# print(a,b,c)



# age = 36.56
# name = " my name "
# txt = "is john, i am "

# print(f"{name.upper()}{txt.upper()}{age}")

# print(name+""+txt+""+age)
# print(f"{name}{txt}{age}")



# name = input("what is your name >>")
# age = int (input("what is your age"))

# print(f"My name is {name.capitalize()} and I am {age}")


# dollar =int(input("enter the dollar amount>>")) 
# naira = 415
# print(f"the convention of {dollar} to {naira} is successful")


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




# name = input( "what is  my name >>")       

# print(len(name))

# lastname=input("what is the lastname >>")
# newval= name.replace(name, lastname)
# print(newval)
# print (f"my name is{name} and now it is {lastname}")



# List: is a collection which is ordered and changeable. 
# A list is created with a square bracket [] or list() constructor.
# from re import M
# from typing import Tuple
# from unicodedata import name


# x = [1,2,3]
# print(x*2)

# my_list= ["Shade", "energy", "cityboy", "city4life", "energy"]
# my_list2= list((12, 14, "Sunday","Charse", True, False, 5.08))
# My_list3=[1, 45, 54, 23, 67, 78, 46]
# # print(my_list)


# print(my_list2)
# print(my_list[0])
# print(My_list3)
# for name in my_list:
#   print(name)
# my_list= ["Shade", "energy", "cityboy", "city4life", "energy"]
# my_list[4]= "solar"
# print(my_list)
# print(my_list2[0])
# print(my_list2[1:6])
# print(my_list2[-3])
# print(my_list2[-4:-1])
# print(len(my_list))
# print(type(my_list2))


# if 'cityboy' in my_list2:
#     print('present')
# else:
#     print('not available')
# my_list2.append("tunde")
# print(my_list2)
# my_list2.insert(3, 'tunde')
# print(my_list2)
# my_list.extend(my_list2)
# print(my_list)
# for name in my_list2:
#     my_list.append(name)
# print(my_list)
# my_list.remove('energy')   
# print(my_list)
# my_list.pop(2)
# print(my_list)
# my_list2.pop()
# print(my_list2)
# my_list.clear()
# print(my_list)
# del my_list
# print(my_list)
# My_list3.sort()
# print(My_list3)
# My_list3.sort(reverse = True)
# print(My_list3)
# my_list.sort(reverse=True, key=str.lower)
# print(my_list)
# My_list3.reverse()
# print(My_list3)
# name = my_list2.copy()
# print(name)
# name = list(my_list2)
# print(name)
# name = my_list + my_list2 + My_list3
# print(name)
# print(my_list.count('energy'))
# print(max(My_list3))
# print(min(My_list3))
# print(my_list.index('Shade'))
# my_list4 =[my_list, my_list2, My_list3, ['Favour', 34], my_list2, 'Tunde', False]
# # print(my_list4)
# print(my_list4[3])
# print(my_list4[1][1:3])

# my_list = ["city", "cityy",]
# for i in range(6):
#     print(i)
# name= input("what is your name")
# age = input("what is your age")
# surname= input("what is your surname")
# print(surname)


# name = range(2)
# age = []
# for i in name:
#  age.append(input("what is your name>>"))
# total=[]
# for i in age:
#  total.append(i)
#  print(total)
# name= range (2)
# name2 = []
# for i in name:
#     name2.append(input("what is your name>>"))
# total= []
# for i in name2:
#     total.append(i)
# print(total)

# Tuple :  A tuple is a collection that is ordered but not changelable. A tuple is created using
# # braces i.e () or tuple ()
# from bdb import Breakpoint
# from itertools import combinations
# from math import factorial
# from re import I
# from tarfile import _Bz2ReadableFileobj


# name = ("Shade", "energy", "cityboy", "city4life", "energy")
# name2 = tuple ((12, 14, "Sunday","Charse", True, False, 5.08))
# print (name2)
# print(name[3])
# print(name[2:4])
# print(name[-3])
# print(name[-4:-2])
# print(len(name))
# food = ('Yam',)
# print(type(food))
# print(type(name2))
# if 1 in name2:
#     print('is available')
# else:
#     print('not available')
# name[3] = "wine"
# print(name)
# name.add("tovy") tuple has no attribute add error
# print(name) 
# # name.pop() 'tuple' object has no attribute 'pop'
# del name
# print(name)
# Unpacking values of a tuple
# item = ("Yam","Sunday","Lagos", "Yam", "Sunday", "Lagos", 45)
# (food, *name, location, age) = item
# print(name)
# (food, *name, age, mymy, our) = item
# print(name)
# for city in name2:
#     print(city)
# new_name = name + name2
# # print(new_name)
# new_name = name *2
# print(new_name)
# print(name.count("energy"))
# print(name.index("cityboy"))



# Set : A set is a collection which unordered and unindexed. It is always written using curly bracket 
# # i.e {} or set()
# name = {"Shade", "energy", "cityboy", "city4life", "energy"}
# name2 = set ((12, 14, "Sunday","Charse", True, False, 5.08))
# new_name = name + name2
# print(name)
# print(len(name))

# print(type(name2))
# for top in name2:
    # print(top)
# print("cityboy" in name)
# print("cityboy" not in name)
# name.add("orange")
# print(name)
# name.update(name2)
# print(name)
# for x in new_name:
#     print(x)


# set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# set2 = {2, 4, 5, 7, 8 ,12} 

# set3 = set1.union(set2)
# print(set3)
# set1.update(set2)
# print(set1)
# intercept = set1.intersection((set2))
# # print(intercept)
# intercept = set1.intersection((set2)).intersection(set3)
# print(intercept)
# set1.intersection_update(set2)
# # print(set1)
# set3= set1.symmetric_difference(set2)
# print(set3)
# set2.symmetric_difference_update(set1)
# print(set2)
# set1.difference_update(set2)
# print(set1)
# print(set1.isdisjoint(set2))
# print(set1.issubset(set2))
# print(set3.issuperset(set1))
 
# name = {}
# for i in range(3):
#     # qud=keys
#     keys= input("enter you keys>>")
#     values = input("enter your value>>")
#     name.update({keys:values})
# print(name) 

# student_details={
#     "Tony Johnson":{ 'name':'Tony Johnson', 'level':300, 'location':'Takie', 'dept':'math'},
#     "Micheal Chan":{ 'name':'Micheal Chan', 'level':200, 'location':'General', 'dept':'computer'},
#     "Timi Joy":{ 'name':'Timi Joy', 'level':400, 'location':'Apake', 'dpt':'english'},

# }

# n = {}
# m = int(input('Enter the name of your nested dictionary '))
# for i in range(2):
#     dict_name = input("Name>>>")
#     n[dict_name] = {}
#     name = input("what is the name>>")
#     level = int(input("what is the level >>"))
#     age= input("what is the age >>")
#     n[dict_name]["name"]= name
#     n[dict_name]["age"]= age
#     n[dict_name]["level"]= level
# print(n)
    
 
# from datetime import time

# from sys import is_finalizing


# name=input("what is thr")
# m = float(input('what is the prime number'))
# if m > 1 :
#     for i in range (2, m):
#         if (m % 2 ==0):
#             print( 'it is prime')
# else:
#     print ('it is not prime')          

# if (m  % 2 == 0):
#     print ("it is even") 

# elif ():
#     print("it is prime")
# else:
#     print("odd")


# num = 13
# if num > 1:
#  for i in (2, num//2):
#     if (num % i) == 0:
#       print(num, "is not a prime number")
#     break
# elif():
#     print(num, "is a prime number")
     
# else:
#      print(num, "is not a prime number")


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


# m=[1,2,3,4,5,6,7,8,9,10]
# final=[]
# for i in m: 
#     result= m[9] * i
#     final.append(result)
# print(final)
# Or
# for i in m:
#     final.append(m[-1]*i)
# print(final)

# print(m.index(9))

# loop
# evennum=[]
# oddnum=[]
# for i in range(6):
#     num=int(input("what is the number >>"))
#     if (num % 2 == 0):
#         evennum.append(num)
#     else:
#         oddnum.append(num)
# print("even::", evennum)
# print("odd::", oddnum)

# nexted looping - loop inside loop(nexted for loop);

# m= ["name", "school", "level", "area"]
# n=["pual", " sqi", "200", "moniya"]
# for i, y in zip(m, n):
#     print({i,y})


# for i in range(6):
#     print('*'*i)


# for i in range(5):
#     for y in range(5):
#       print(i+y)
# #   
# m =int(input("what is the input"))
# n = int(input("what is the value"))

# num= 2
# for i in range(1, 13): 

#      print(num, "x", i, "=", num*i) 
     
# num = int(input("what is the number >>"))
# for i in range (1, 13):
#     print(num, 'x', i, '=', i*num)

# num = int(input("what is the number >>")) 
# y = 1

# for i  in range(1, num+1):
#     for j in range(1, i+1 ):
#         print(y, end =" ") 
#         y = y + 1
#     print()    


# num =[1,2,3,4,5]
# for i in num:
#     print(i)
# count = 0
# while count > 5:
#      if count == 3:
#          break 
#      print(num[count])
#      count +=1
    
# else:
#     print("end of program")
 
# num=int(input("what is the number>>"))
# i = 1
# while i < 13:
#     c=num*i 
#     print(num, "*", i, '=', c) 
#     i += 1



# x = 0
# while x <= 18:
#     x =x+3
# print(x)


# m = 2
# while m < 5:
#     print("cityboy", m)
#     m+=1

# list =[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]
# m = sorted(set(list))
# # while m < list:
#   print(m)
#   m+=list

# m=[]
# for i in list:
#     if i not in m:
#         m.append(i)
# print(m)


# for i in range (10):
#     if i > 5:
#         print(">5.......", i)
#     else:
#         print("<<<<<<<<5", i)
#         if i > 3:
#          break


# A function is a block line of code(best way to aviod don't repeat yourself)
# global varaible is a variable you decline befoc


 


# def city(n):
#     num = 1 
#     for i in range(0, n): 
#         num = 1
#         for j in range(0, i+1):
#             print(num, end="")
#             num += 1
#         print()
# city(5)

# def city(n):
#     for i in range (1, n):
#         print(n, "x", i, '=', n*i )
# city(12)


# from math import factorial
# def city(n):
#   f= 1
#   for i in range(1, n+1):
#     f = f * i 
#   return f
# n = int(input('what is the number'))
# r = int(input('what is the number'))
# combination = factorial(n)/factorial*factorial(n-r)
# print(combination)

# # Zenith USSD
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
    # reg+=city
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

# object oriented programming

# class Father:
#     def __init__(self, man, woman):
#         self.name = man
#         self.age= 11
#         self.location= woman
        
    
#     def walk(self):
#          print(f"{self.name} can walk")
    
#     def leg(self):
#         print(f"{self.name} can walk to {self.location}")


# class Son(Father):
#     def __init__(self):
#         super().__init__("city", "oyo")
#         self.name ="cityboy"
#         self.age = 12
#     def play(self):
#         print(f"{self.name} can play football in {self.location}")


# ms = Son()
# ms.play()



# m= int(input("enter the number"))
# f= 1
# for i in range(1, m+1):
#     f = f * i 
# print(f)


# def city(n):
#   f= 1
#   for i in range(1, n+1):
#     f = f * i 
#   return f
# n = int(input('what is the number'))
# r = int(input('what is the number'))
# combination = city(n)/(city(r)*(city(n-r)))
# print(combination)





# class Father:
#     def __init__(self):
#         self.name = int(input("what is the num >>"))
# class Son(Father):
#     def __init__(self):
#         super().__init__()   
#     def f(self):
#         f = 1
#         for i in range(1, self.name + 1):
#             f = f * i
#         print()

        
# m = Son()
# m.f()
 

# def fact(n):
#    f = 1
#    for i in range(1, n+1):
#     f = f*i
#    print(f)
# fact(6)

 


# class Father:
#     def __init__(self):
#         self.n = int(input("enter the number>>"))
#         self.r= int(input("enter the r>>")) 
# class Son(Father):
#   def __init__(self):
#      super().__init__()
#   def fact(self):
#     f = 1
#     for  i in range (1, self.n+1):
#       f *= i
#     return f
#   fact = fact(self.n)
  

# def city(n):
#     n= int(input("enter the number>>"))
#     g = 1
#     for i in range(1, n+1):
#       g *= i
#     return g











# from time import sleep
# n = 1 
# while True: 
#     print(n)
#     n+=1
#     sleep(0.5)






# def city(n):
# n = 5
# num = 1
# for i in range(0, n): 
#  num = 1
#  for j in range(0, i+1):
#     print(num, end='')
#     num += 1 
#  print()
# # city(5)


# def city(n):
#     num = 1 
#     for i in range(1, n +1 ): 
#         for j in range(1, i+1):
#             print(num, end=' ')
#             num += 1
#         print()
# city(5)



# n = 5
# # num = "*"
# for i in range (1 , n+ 1):
#     for j in range(1, i+1):
#         print("*", end='')
        
#     print("")

# def triangle(r):
#     k = r - 1
#     for i in range (0, r):
#         for j in range (0, k):
#             print(end='')

#         k = k-1
#         for j in range(0, i+1):
#             print('*', end='')
#         print("")
# triangle(5)




  ## file handling
# open('filename', mode='r', 'a', 'w', 'x', encoding='t', 'b')
# 'r' read only and it is the default for open function. raise error if file do not exist 
# 'a' append new content to an existing file. create new file with the specific file.
# 'w'  open file for writing . create new file with specific name if not exist.
# 'x'  to create new file. raise error if file already exist


# with open("C:\\Users\\D\\Desktop\\paul\\pa.txt", mode='rt') as myFile:
    # for i in myFile:
    #     print(myFile.readline())

#   print(myFile.read(10))
# with open("C:\\USER\\Documents\\python code.txt", mode='rt') as myFile:
#   print(myFile.read())

# myFile = open("C:\\Users\\D\\Desktop\\paul\\mmm\\com.txt", 'rt') 

# myFile = open("C:\\Users\\ASUS\\Documents\\vuework.txt", mode='r')
# print(myFile.read())
# print(myFile.read(20))
# for i in range(2):
#     print(myFile.readline())

# for i in range(20):
#   print(myFile.readline())

# for i in myFile:
#   print(i)

# with  open("C:\\Users\\D\\Desktop\\paul\\mmm\\ll.txt", 'wt') as myFile:
#     # print(myFile.read())
#     myFile.write("\nthis is new content to append to the old file")

# myFile = open("C:\\USER\\Documents\\PYTHON\\code.txt", 'rt') 
# print(myFile.read())
# myFile.close()



# myFile = open("code.txt", 'w') 
# myFile.write("\n this is cnew content to append to the old file")

# with open("code2.txt", 'w') as newFile:
#   newFile.write("here i am writing to new file")


# open("C:\\Users\\ASUS\\Documents\\vuwwork4.txt", 'x') 
# myFile = open("C:\\Users\\ASUS\\Documents\\vuwwork4.txt", 'a') 
# myFile.write("\n lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum")
# myFile = open("C:\\Users\\ASUS\\Documents\\vuwwork4.txt", 'r') 
# print(myFile.read())



# with open("C:\\USER\\Documents\\python code.txt", mode='rt') as myFile:
#   print(myFile.read())


import os
# print(dir(os))
# os.remove('newfile.txt') #raise error if not exist
# if os.path.exists('mypython.py'):
#   os.remove('fun.jfif')
#   print("file deleted successfully")
# else:
#   print('file not available')


# if os.path.exists('mypython.py'):
#   with open("mypython.py") as myFile:
#     os.rmdir("nmn")
# else:
#   print("file does not exist")

# if os.path.exists("code.txt"):
#   os.remove("code.txt")
#   print("file deleted successfully")
# else:
#   print("file not available")



# os.rmdir("new folder")
# os.mkdir("new folder")
# os.mkdir("another folder")
# os.mkdir("Documents")




# with open("bankOOP.py", 'rt') as myFile:
#   print(myFile.read())



# with open("Documents", mode='rt') as inFile:
#   for files in inFile:
#     os.remove(files)

# deleting file and folder in a system
# for root, dirs, files in os.walk(" folder name"):
#   for file in files:
#       pass
#     # os.remove("new folder\\"+file)
# # os.rmdir("new folder")

# print(root)
# deleting file in folder
# for root, dirs, files in os.walk("another folder"):
#   for fil in files:
#     os.remove("another folder\\"+fil)
# os.rmdir("another folder")

# searching for  path of a file
# print(os.path.dirname(os.path.abspath("text.txt")))




# with open("Documents", mode='rt') as inFile:
#   for files in inFile:
#     os.remove(files)


# code to get username of any system(pc)
# import os.path
# homedir = os.path.expanduser("~")
# print(homedir)
# code to get system environment
# import os
# homedir = os.environ["PATH"]
# print(homedir)

# code to get the path of a file on your device
# print(os.path.dirname(os.path.abspath("mypython.py")))





























# name = {}
# for i in range(3):
#     keys= input("enter you keys>>")
#     values = input("enter your value>>")
#     name.update({keys:values})
# print(name) 



# i = 1
# while i < 6:
#     print(i)
#     i -=1