# s = 'apple'
# t = list(s)
# print(t)

# s = 'every morning you greet to me'
# t = s.split()
# delemiter = ' '
# print(delemiter.join(t))
from csv import excel

# myStr = input("Please Enter String : ")
# myList = myStr.split()
# exceptStr = input("Please Enter Except String : ")
# addStr = input("Please Enter Add String : ")
# myList.remove(exceptStr)
# myList.append(addStr)
# print(' '.join(myList))

# # Shallow Copy / Deep Copy
# from copy import *
# list1 = ['apple', 'banana', 'cherry']
# list2 = list1
# list3 = deepcopy(list1)
# list1[0] = 'melon'
# print(list1)
# print(list2)
# print(list3)

# liFruit = []
# while True:
#     inputValue = input("Enter Fruit : ")
#     if inputValue == 'zzz':
#         break
#     else:
#         liFruit.append(inputValue)
#
# print(len(liFruit))
# print(liFruit)

# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
#
# for item in list1:
#     if item in list2:
#     # if list2.__contains__(item):
#         list2.remove(item)
#
# list1.extend(list2)
# print(list1)

# from copy import *
# mumList = [1, 3, 5, 7, 9]
# numShallow = mumList
# numDeep = deepcopy(mumList)
#
# numShallow.append(91)
# numDeep.append(111)
#
# print(mumList)
# print(numShallow)
# print(numDeep)

# list = [9, 7, 5, 3, 1]
# print(sum(list))
# print(sorted(list))

# intNum = round(23.5123123, 2)
# print(intNum)

def calculate_avg(num1, num2, num3):
    result = (num1 + num2 + num3) / 3
    return result

a = 1000
b = 3000
c = 400

print(calculate_avg(a, b, c))