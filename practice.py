# def fact(n):
#     if n==1:
#         return 1
#     return n* fact(n-1)
# print(fact(5))

# def rec(n):
#     if n==0:
#         return 
#     rec(n-1)
#     print(n)
# rec(8)

# def sum_n(n):
#     if n==1:
#         return 1
#     return n+sum_n(n-1)
# print(sum_n(5))

file = open("khan.txt","r")
data = file.read()
words = data.split()
print(len(words))

print("Hello")