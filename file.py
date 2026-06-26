# file = open("khan.txt" , "r")
# data = file.read()

# print(data)

# file= open("khan.txt", "r")
# data = file.read()

# data = data.upper()
# if "HUMAN" in data:
#     print("human word is in the file ")
# else:
#     print("no")

# file = open("report.txt","a")
# file.write("Khalid bhai")

# with open("report.txt", "r") as f:
#     data= f.read()
#     print(data)

# with open("khan.txt") as f:
#     # line1 = f.readline()
#     # line2 = f.readline()
#     # line3 = f.readline()
#     # data = f.read()
#     # print(line1)
#     # print(line2)
#     # print(line3)
#     # print(data)
#     line = f.readlines()
#     print(len(line))
# import shutil
# shutil.copy("khan.txt" , "report.txt")
# import os
# # os.rename("report.txt", "bhai.txt")
# os.remove("bhai.txt")
# import datetime
# with open("khan.txt" , "a") as f:
#     f.write(f"khalid opened this file at {datetime.datetime.now()}\n")
# 
# try:
#     with open("khn.txt","r") as f:
#         data = f.read()
#         words = data.split()
#         print(len(words))
# except:
#     print("file doesn't occured")

# class vehicel:
#     name = "civic"
#     color= 'black'
#     price = 10000
# c1 = vehicel()
# print(vehicel.color)

# class vehicale:
#     name = "BMW"
#     color = "black"
#     price ="1m"

# car1 = vehicale()
# car1.name = "m5"
# car1.color = "red"
# print(car1.color)

# car2 = vehicale()
# car2.name = "M4"
# car2.color = "blue" 
# print(car2.color)

# class student:
#     def __init__(self,name,grade):
#         self.name= name
#         self.grade= grade
#         print(self.name)
#         print(self.grade)
#         print("my nameis khalid")
# st1 = student("khalid",11)

# class student:
#     def __init__(self, name, marks):
#         self.name= name
#         self.marks= marks
#     def average(self):
#         sum = 0
#         for i in self.marks:
#             sum = sum+i
#         average = sum/3
#         print(average)

# st = student("khalid",[98,65,45])
# st.average()
        
class numbers:
   
    def __init__(self,num):
        
        self.num=num
    
    def numb(self):
        num = self.num
        if num/2==0:
            print("this number is even")
        else:
            print("this number is odd")
number = numbers(23)
number.numb()