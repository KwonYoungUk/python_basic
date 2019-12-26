# Module

# def dump(exp):
#     result = eval(exp)
#     print(exp, "->", result, type(result))

# inputVal = input("Enter String : ")
# alphaCnt = 0
# upperCnt = 0
# lowerCnt = 0
#
# for ch in inputVal:
#     alphaCnt += 1 if ch.isalpha() else 0
#     upperCnt += 1 if ch.isupper() else 0
#     lowerCnt += 1 if ch.islower() else 0
#
# print("alpha : {}, upper : {}, lower : {}".format(alphaCnt, upperCnt, lowerCnt))

# import math
# a = int(input("Enter a : "))
# b = int(input("Enter b : "))
# c = int(input("Enter c : "))
#
# result1 = (b * (-1) + math.sqrt(math.pow(b, 2) - (4 * a * c))) / (2 * a)
# result2 = (b * (-1) - math.sqrt(math.pow(b, 2) - (4 * a * c))) / (2 * a)
#
# print("result {} or {}".format(result1, result2))

# import math
# degree = int(input("Enter Degree : "))
# rad = math.radians(degree)
# print(math.sin(rad))
# print(math.cos(rad))
# print(math.tan(rad))

# import time
# from datetime import date
#
# today = date.today()
# targetYear = today.year
#
# pBirthday = input("Enter Youer Parent's Birthday(MM DD) : ")
#
#
# pList = pBirthday.split();
# if int(pList[0]) < today.month or (int(pList[0]) == today.month and int(pList[1]) < today.day):
#     targetYear += 1
#
# tBirthday = date(targetYear, int(pList[0]), int(pList[1]))
# print(tBirthday - today)

from tkinter import *

# from os import *
# system('calc')
# system('notepad')

# import os
# print("using", os.name, "...")

# import fibo
# f = fibo
# print(f.fib(11))
# print(f.ifib(11))

# recursion
# def countdown(n):
#     print(n)
#     if n > 1:
#         countdown(n - 1)
#
# countdown(5)

# def pow(i, j):
#     if j == 0:
#         return 1
#     else:
#         return i * pow(i, j - 1)
#
# print(pow(3, 2))

# def mult3(n):
#     if n == 1:
#         return 3
#     else:
#         return 3 + mult3(n - 1)
#
# def mult3_loop(n):
#     a = 0
#     for i in range(1, n+1):
#         a = a + 3
#     return a
#
# for i in range(1, 10):
#     # print(mult3(i))
#     print(mult3_loop(i))

# def pattern(n):
#     if n == 0:
#         print(0, end=' ')
#     else:
#         pattern(n - 1)
#         print(n, end=' ')
#
# pattern(5)
# print()
# pattern(11)

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# print(factorial(10))

def fibo(n1):
    if n1 == 1 or n1 == 2:
        return 1
    else:
        return fibo(n1 -1) + fibo(n1 - 2)

for i in range(1, 15):
    print(fibo(i))