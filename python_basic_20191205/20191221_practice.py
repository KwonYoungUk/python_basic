# def print_script():
#     print("Blessed are the ppr in script")
#
# def repeat_script():
#     print_script()
#     print_script()
#
# repeat_script()

# def print_chr(times):
#     for i in range(times):
#         print("*")
#
# print_chr(10)

# def plus(num1, num2):
#     return num1 + num2
#
# print(plus(3, 5))

# def user_pow(num1, num2):
#     result = 1
#     if num2 == 0:
#         return 1
#     else:
#         for i in range(num2):
#             result *= num1
#
#     return result
#
# print(user_pow(2, 5))

# def user_max(num1, num2, num3):
#     if num1 > num2 and num1 > num3:
#         return num1
#     elif num2 > num1 and num2 > num3:
#         return num2
#     elif num3 > num1 and num3 > num2:
#         return num3
#
# print(user_max(1, 3, 5))

# # python의 경우 여러개의 변수를 return 가능함

# def fahr(calc):
#     return (calc * 9 / 5) + 32
#
# print(fahr(30))

# def multiply(num1, num2):
#     return num1 * num2
#
# print(multiply(100, 2))

# import turtle
# t = turtle.Turtle()
#
# def drawPolygon(length, sides, color):
#     t.color = color
#     angle = 360 / sides
#     for i in range(sides):
#         t.forward(length)
#         t.right(angle)
#
# for i in range(3):
#     drawPolygon(200, 6, "green")

# import random
#
# randomList = []
# for i in range(3):
#     randomList.append(random.randint(1, 10))
#
# print(randomList)
#
# for i in range(5):
#     randomList.append(random.randint(1, 100))
#
# print(randomList)
# random.shuffle(randomList)
# print(randomList)
#
# print(random.choice(randomList))
#
# print(random.sample(randomList, 4))

import random

# def random_pick(list, number):
#     for i in range(number):
#         print(random.choice(list))
#
# numList = [3, 1, 7, 11, 25, 5, 4, 9]
#
# random_pick(numList, 3)

def printA(num1, num2):
    randNumber = random.randint(num1, num2)
    print("A" + str(randNumber))

for i in range(10):
    printA(3, 10)