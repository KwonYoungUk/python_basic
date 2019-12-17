import turtle
import sys

# t = turtle.Turtle()
# t.forward(250)
# t.left(90)
# t.forward(250)
# t.left(90)
# t.forward(250)
# t.left(90)
# t.forward(250)

# # 사각형 그리기
# a = 20;
# for num1 in range(0, 30):
#     t.forward(a)
#     a += 20
#     t.left(90)

# # 별 그리기
# for num in range(5):
#     t.forward(100)
#     t.right(144)

# # 원 그리기
# t = turtle.Pen()
# t.color("blue")
# t.begin_fill()
# t.circle(50)
# t.end_fill()

# # 배경, 선그리기
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# wn.title("Hello World")
#
# tess = turtle.Turtle()
# tess.color("red")
# tess.pensize(25)
#
# tess.forward(150)
# tess.right(150)
# tess.forward(100)
#
# wn.done()
# turtle.done()

# wb = turtle.Screen()
# wb.bgcolor("lightgreen")
# wb.title("draw Test")
#
# t = turtle.Turtle()
# t.penup()
# t.goto(150, 150)
# t.pendown()
# t.right(60)
# t.forward(60)
# t.right(120)
# t.forward(60)
# t.right(120)
# t.forward(60)
#
# wb.done()
# t.done()


# wn = turtle.Screen()
# wn.bgcolor("lightblue")
#
# t = turtle.Turtle()
# t.shape("turtle")
# t.color("hotpink")
#
# t.penup()
# size = 20
#
# for i in range(50):
#     t.stamp()
#     size = size + 3
#     t.forward(size)
#     t.right(24)

# wn.done()
# t.done()

# t = turtle.Turtle()
# t.speed("fastest")
# size = 50
# for i in range(36):
#     size += 10
#     t.right(10)
#     for j in range(4):
#         t.forward(size)
#         t.right(90)

# t = turtle.Turtle()
# t.speed("fastest")
# for i in range(20):
#     t.forward(i * 30)
#     t.right(144)
#
# turtle.done()

# def hexagon():
#     for num1 in range(6):
#         turtle.forward(100)
#         turtle.left(60)
#
# turtle.color("red")
# hexagon()
#
# for i in range(6):
#     hexagon()
#     turtle.forward(100)
#     turtle.right(60)
#

# def square(t, size, color):
#     t.color(color)
#     for i in range(4):
#         t.forward(size)
#         t.right(90)
#
# t1 = turtle.Turtle()
# t1.pensize(3)
#
# colors = ["red", "orange", "yellow", "green", "blue", "violet"]
#
# i = 30
# for color in colors:
#     t1.right(90)
#     square(t1, i, color)
#     i += 30

# def drawPolygon(sideLength, numSides, color):
#     for i in range(numSides):
#         turtle.color(color)
#         turtle.forward(sideLength)
#         turtle.right(360 / numSides)
#
# turtle.penup()
# turtle.goto(0, 300)
# turtle.pendown()
#
# drawPolygon(10, 80, "red")

# for i in range(3):
#     drawPolygon(100, 5, "red")
#     turtle.forward(100)

# win = turtle.Screen()
# win.bgcolor("black")
#
# one = turtle.Turtle()
# one.speed("fastest")
# one.color("red")
# one.pensize(1)
#
# def n_one(n, size):
#     for i in range(n):
#         one.circle(size)
#         one.left(360.0 / n)
#
# n_one(200, 70)

# # Exception
# try:
#     a = 100
#     b = 0
#     print("{} / {} = {}}".format(a, b, a / b))
#
# except ZeroDivisionError:
#     print("division by zero")
#
# else:
#     print("in else")
#
# finally:
#     print("in finally")

# while True:
#     try:
#         result = int(input("Please enter an Integer : "))
#         break
#     except ValueError:
#         print("Oops! That was no valid number. Try again...")
#     else:
#         print("Integer : {}".format(result))
#     finally:
#         print("End")
from weakref import finalize

# while True:
#     a = int(input("number you wont to divide 100 : "))
#     print(a)
#     try:
#         b = 100 / a
#         print("result is {}".format(b))
#         break
#     except ZeroDivisionError as err:
#         print("Handling Runtime Error {}".format(err))
#     finally:
#         print("END")

# def chkAge(age):
#     assert(int(age) > 1 or int(age) < 100), print("ERROR")
#     return age
#
# age = input("Please Enter Age : ")
# chkAge(age)

# age = int(input("Enter Age : "))
# while age < 1 or age > 100:
#     print("Error! Please Enter Age again")
#     age = int(input("Enter Age : "))

while True:
    try:
        age = int(input("Please Enter Age : "))
        break;
    except ValueError as err:
        print("Error! {}".format(err))
    finally:
        print("end")
