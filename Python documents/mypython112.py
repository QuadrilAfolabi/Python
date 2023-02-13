
# Python Regular Expression
# import re
# print(dir(re))
# text = """the value of a thing will determing the capacity you put to it. 
#         the value of 2019 is what you get in 2020
#         and now you get the value of 2020 in 2021"""
# mm ="""the  get"""
# val = re.search("^the.*get$", mm)
# if val:
#     print("We have a match")
# else:
#     print("No match detected")
 
# re function
# findall() : returns list containing all matches
# search() : returns object of a match if there is a match anywhere in the string
# split() : returns a list where the string has been split at each match
# sub() : replace one or many matches  with a string

# re metacharacters
# [] : refers to set of characters to match eg "[a-m]"
# \ : can be use to escape special charactter eg "\d"
# . : any character except newline character eg 'he.o'
# ^ : starts with eg "^the"
# $ : ends with eg "world$"
# * : zero or more occurrences eg "aix*"
# + : one or more occurrences eg "aix+"
# {} : exactly specified number of occurrence eg "al{2}"
# | : either or eg "this|that"
# () : capture and group 

# re special Sequences
# \A : returns a match if the specified characters are at the begining of the string eg "\AThe"
# \b : returns a match if the specified characters are at the begining or at the end of the string eg r"\bthe" or r"the\b"
# \B : returns a match if the specified characters are present but not at the begining or at the end of the string eg r"\Bthe" or r"the\B"
# \d : returns a match where the string contains digits (number from 0-9) eg "\d"
# \D : returns a match where the string does not contains digits eg "\D"
# \s : returns a match where the string contains a white space character eg "\s"
# \S : returns a match where the string does not contains a white space character eg "\S"
# \w : returns a match where the string contains characters from letter A-Z and digits from 0-9 and underscore eg "\w"
# \W : returns a match where the string does not contains any word characters 
# \Z : returns a match if the specified characters are at the end of the string

# re sets
# [arn] : returns a match where one of the specified characters (a or r or n ) are present
# [a-n] : returns a match for any lower case character alphabetically between a and n
# [^arn] : returns a match for any character except a, r and n
# [0123] : returns a match where any of the specified digits (0, 1, 2, 3) are present
# [0-9] : returns a match for any digits between 0 and 9
# [0-5][0-9] : returns a match for any two digits between 00 and 59
# [a-zA-Z] : returns a match for any character alphabetically between a and z lower case or upper case
# [+] : returns a match for any character in the string


text = """the value of a thing will determing the capacity you put to it. the value of 2019 is what you get in 2020 
          and now you get the value of 2020 in 2021"""
# x = re.findall(r'the', text)
# print(x)
# txt = "the value of a thing"
# x = re.search(r'you', text)
# print(x)
# print(x.span())
# print(x.group())
# print(x.string)
# z = re.split(r'\s', text)
# print(z)
# z = re.split(r'\s', text, 5)
# print(z)
# tx = re.sub(r'\d', '[]', text)
# print(tx)
# tx = re.sub(r'capacity', 'ability', text)
# print(tx)
# tx = re.sub(r'\d', '[]', text, 5)
# print(tx)






# Python DateTime
# import datetime
# import time
# # print(dir(time))
# tim = datetime.datetime(2022, 6, 7, 11, 12 ,12,12)
# # print(tim)

# def paul():
#     print("hello world")

# while True:
#     if tim.strftime("%I") == "11" and tim.strftime("%p") == "PM" and tim.strftime("%M") =="12":
#         paul()
#         break
#     else:
#         print("okay")
#         break
# while True:
#     print("hello")
#     time.sleep(5)


# tim = datetime.datetime(2022, 6, 7, 11, 12 ,12,12)
# print(tim)
# print(help(datetime))
# tim = datetime.datetime.now()
# print(tim)
# print(tim.year)
# print(tim.day)
# print(tim.strftime("%j"))
# tm = datetime.datetime(2021, 4, 10)
# print(tm)
# print(tm.month)
# tm = datetime.datetime.now()
# print(tm)
# strftime() method - use to format datetime object into readable string
# print(tm.strftime("%U"))
# # strftime format codes
# %a : returns weekday in short version eg wed
# %A : returns weekday in full version eg wednesday
# %w : returns weekday in number version from 0-6 where 0 means sunday eg web is 3 
# %W : returns week in number version from 1-52
# %d : returns day of the month in number version from 01-31
# %D : returns day, month and year in  07/20/22 = /mm/dd/yy format
# %b : returns month name in short version eg Dec
# %B : returns month name in full version eg December
# %m : returns month in number formart from 01-12 
# %M : returns min in number formart from 00-59
# %y : returns year in short version eg 2021 is 21
# %Y : returns year in full version eg 2021
# %H : returns hour in 24hrs format from 00-23
# %I : returns hour in 12hrs format from 00-12
# %p : returns AM or PM of time
# %M : returns minute of time from 00-59
# %S : returns seconds of time from 00-59
# %X : returns time 13:06:38
# %f : returns microseconds of time form 000000-999999
# %Z : for timezone
# %j : days number of the year from 001-366
# %U : return week number of the year from 00-54 


# import os
# import sys

# import vlc

# os.add_dll_directory(os.getcwd())
# os.add_dll_directory(r'C:\\ProgramData\\Anaconda3\\lib\\site-packages\\vlc.py')
# os.add_dll_directory(r'C:\\Users\\D\\Desktop\\paul\\mmm\\tw\\libvlc.dll')
# print(dir(vlc))
# import time
# # print(help(vlc.AudioSetVolumeCb))
# # print(help(vlc.MediaPlayer))

# while True:
#     time.sleep(5)
#     tm = datetime.datetime.now()
#     if tm.strftime("%I") == "9" or tm.strftime("%M") == "59" or tm.strftime("%S") == "04" and tm.strftime("%p") == "AM":
#         # if tm.strftime("%M") == "51":  
#         print("it's time for break")
#         break
#         p = vlc.MediaPlayer("01 Merciful God.mp3")
#         p.play()
#         time.sleep(170)
#         p.stop()
        # break
#     else:
#         print("lecture continues") 
#         p = vlc.MediaPlayer("01 Merciful God.mp3")
#         p.play()
#         time.sleep(170)
#         p.stop()
#         break      
        
        

# import datetime
# check = int(datetime.datetime.now().strftime("%M")) 
# # print(check)
# rang =[]
# [rang.append(rn) for rn in range(0,60)]

# while True:
#     time =datetime.datetime.now() 
#     nexttime = time.strftime('%M')
# #     print(nexttime)
#     if int(nexttime) in rang and check == int(nexttime):   
#         for i in range(1):
#             print("i am going to class today")
#     check = int(nexttime )+ 1

# hour = hour[0]+str(int(hour[1]) + 2)
# print(hour)




# Python Math 
# import math
# print(dir(math))

# print(help(math.ceil))
# l = [2, 4, 5, 7, 3]
# print(min(l))
# print(max(l))
# print(abs(-5.34))
# print(pow(3, 3))
# print(math.sqrt(9))
# print(math.ceil(8.3492))
# print(math.floor(5.6732))
# print(math.pi)
# print(math.pi * 1000 + 25)



 

