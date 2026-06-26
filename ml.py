# name =(input("Enter your name: "))
# print(name)
# print(name[0])
# print(name[-1])
# print(len(name))

# name = (input("enter the name: "))
# mid = len(name)//2
# output = name[mid-1:mid+2]
# output1 = name[-2:]
# print(output)
# print(output1)

# name =(input("Enter the sentence = "))
# new = (name.lower().replace(" ","_"))

# print(new)

# a = input("Write something: ")
# print(a[0])
# print(a[-1])
# print(len(a))

# a = int((input("Enter the number: ")))
# if(a>0):
#     print("The number is positive")
# elif(a==0):
#     print("The number is negative")
# else:
#     print("Thenumber is zero")
# 

# tuple = (87,64,33,95,76)
# print(max(tuple))
# print(min(tuple))

# dict = {
#     "chair": "kursi",
#     "door" : "darwaza",
#     "house": "ghar"
# }
# print(dict)

# set1 = {1,2,3,4,1,12}
# set2 = {2,3,4,1,6,5}
# print(set1.intersection(set2))

# num = set()
# print(num.add(9))
# print(num.add("nine.zero"))

# num = 1
# while num<7:
#     print("Khalid saad")
#     num = num+1

# num = 10
# while num >0:
#     print(num)
#     num -= 1

# num = 1
# while(num <=50):
#     if(num%2 ==0):
#         print(num)
#     num = num+1

# n = int(input("Enterthe number:"))
# sum = 0
# while(n>=1):
#     sum =sum+n
#     n = n-1
# print("The sumis: ",sum)

# n = 1
# while n <=4:
#     print("*" *n)
#     n =n+1

# n = 1
# while n<=5:
#     print(f"{n}Khalid Saad")
#     n += 1

# n = int(input("Enter the number: "))
# i = 1
# while i <=10:
#     print(f"{n} x {i} = {n*i}")
#     i+= 1

# for i in range(1,51):
#     if i % 5 ==0:
#         print("Khalid Saad")
#     else:
#         print(i)

# for i in range(1,11):
#     print(i**2)

# n= int(input("Enter the number: "))
# for i in range(1,11):
#     print(f"{n} x {i} = {n*i}")

# for i in range(100,0,-1):
#     print(i)

# a = "khalid saad"
# i = a.upper()
# for a in range(1,6):
#     print(i)

# a = ["knkfas","kjdf","ksjebfc","ahkhbbrfd"]

# for i in a:
#     print(i)

# for i in range(1,11):
#     if i ==5:
#         continue
#     print(i)

# import time

# t = int(input("enter the time: "))
# print("\n countdown stats now:")

# for i in range(t,0,-1):
#     print(i)
#     time.sleep(1)
# print("Happy new year")

# for i in range(1,101):
#     print(i)

# i = 100
# while i >=1:
#     print(i)
#     i -= 1

# for i in range(1,50):
#     if(i%5 == 0):
#         continue
#     print(i)

# foods = []

# for i in range(5):
#     food = input(f"Enteryour favourite food name{i+1}: ")
#     foods.append(food)

# print("\nyour favourite food is: ")
# for food in foods:
#     print(food)

# i = 10
# sum = 0
# while i>=1:
#     sum1 = sum+i
#     i -= 1
#     print(sum1)

# def ka():
#     print("My name is khalid")

# ka()
# ka()

# def sum(a,b):
#     print(f"the sum is:{a+b} ")

# sum(2,4)
# sum(3,6)
# sum(9,4)

# def intro(a,b):
#     print(f"{a}is{b}years old")
# intro("khalid","18")

# def food(a):
#     print(f"my favourite food is {a}")

# food("biryani")

# def num(a=5):
#     return a**2
# print(num(4))
# print(num(6))
# print(num())

# def conso(userinput):
#     vowels = "aeiouAEIOU"
#     covowels = 0
#     conso = 0
#     for i in userinput:
#         if(i.isalpha()):
#             if(i in vowels):
#                 covowels +=1
#             else:
#                 conso +=1

#     return covowels , conso
# vowels , consonent = conso("khalidnasir")
# print(vowels , consonent)

# def capital(name):
#     for i in name:
#         if(name.isalpha):

#     return .upper

# capital("khalid")

# def count(input):
#     vowels = "aeiouAEIOU"
#     covo = 0
#     cons0 = 0
#     for i in input:
#         if i.isalpha:
#             if (i in vowels):
#                 covo +=1
#             else:
#                 cons0 +=1
#     return covo , cons0
# vowels , consonent = count("khalid Saad")
# print(vowels, consonent)

# def name(input):
#     vowels = "aeiouAEIUO"
#     covo = 0
#     conso = 0
#     for i in input:
#         if (i.isalpha):
#             if (i in vowels):
#                 covo +=1
#             else:
#                 conso +=1
#     return covo , conso
# vowels , consonent = name("sharfa nasir")
# print(vowels , consonent)

# def upp(name):
#     print(name.upper())
# upp("khalid")

# def name(a,b):
#     print(a + b)
# name("khalid"," saad")
# def message(text):
#     print("text = ",text)
# message("keepg learnin")

# h =2
# def n():
#     global h
#     h = 10
# n()
# print(h)

# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)
# print(factorial(4))

# def factorial(n):
#     if (n==1):
#         return 1
#     return n* factorial(n-1)
# print(factorial(5))

# def rept(n):
#     i= 1
    
#     while i <=n:
#         n = n+1
#         i +=1

#     return n
# print(rept(7))
# def pas(n):
#     if n==0:
#         return
#     pas(n-1)
#     print(n)
# pas(4)
# def pas(n):
#     if n==0:
#         return
#     pas(n-1)
#     print(n)
# pas(7)

# def sent(a):
#     b = a.reverse()
# sent("khalid")

def sent(s):
    if len(s)==0:
        return ""
    return sent(s[1:]) + s[0]
print(sent("khalid"))