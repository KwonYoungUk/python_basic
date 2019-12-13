# a = input()
# b = input()
# print (int(a) / int(b))

# print("{}, {}".format("더존", "권영욱"))
# print(34 + 123)
# print(12 * 12)

# # if ~ elif 테스트
# age = 15
# if age > 65:
#     print("senior")
# elif age > 20:
#     print("adult")
# else:
#     print("young")
#
# # while test
# step = 0
# while step < 1000:
#     print(step)
#     step += 100

# fred = 100

# price = input("가격을 입력하세요: ")
# print(float(price) * 4)

# name = input("Enter your Name : ")
# age = int(input("Enter your Age : "))
# print("My name is {}, and {}-years old.".format(name, age))
#
# affiliation = input("Enter your Company : ")
# year = int(input("Enter your Year : "))
# print("나는 {}년도에 {}에 입학했습니다.".format(year, affiliation))

# float1 = float(input('float 1 : '))
# float2 = float(input('float 2 : '))
# print(float1 + float2)

count = int(input("Enter Count : "))
print("*" * count)
for num1 in range(0, count):
    print("*", end="")