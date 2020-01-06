# myTuple = (3, 5, 7, 1, 2, 6, 54)
# myList = list(myTuple)
# myList.sort()
# print(myList)
#
# myList1 = 'aabcd'
# myList2 = [6, 12, 5, 77, 12]
# print(list(zip(myList1, myList2)))

# import random
#
# def select_item(list, n):
#     result = random.sample(list, n)
#     return result
#
# r = select_item([1, 3, 5, 7, 11, 15, 21], 5)
#
# myStr = 'Kmooc'
# myTuple = tuple(r)
# print(list(zip(myStr, myTuple)))

# s = 'abcdefghijklmnopqrstuvwxyz'
# Num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
#
# print(list(zip(s, Num)))
#
# import random
#
# inputStr = input('Enter String : ')
# outputStr = []
# s = 'abcdefghijklmnopqrstuvwxyz'
# base_s = []
# base_s = random.sample(s, 26)
# baseTuple = list(zip(s, base_s))
# print(baseTuple)
#
# for letter in inputStr:
#     for i in range(26):
#         if letter == baseTuple[i][0]:
#             outputStr.append(baseTuple[i][1])
#
#
# print(outputStr)

# birthday = {}
# for i in range(3):
#     name = input('Enter Name : ')
#     birth = input('Enter BirthDay : ')
#     birthday[name] = birth
#
# print(birthday)
# # printName = input('Enter Name : ')
# # print(birthday[printName])
#
# deleteName = input("Enter Name : ")
# birthday.pop(deleteName)
# print(birthday)
# print(deleteName in birthday)

# phone = {'kim': 123, 'lee': 345, 'park': 999}
# print(phone.keys())
# print(phone.values())

subjects = {'김경미': ['수학', '과학'], '최영희': ['영어', '수학'], '강동원': ['영어'], '정필수': ['사회', '역사'], '박희수': ['국어'], '이승철': ['수학', '과학']}
inputSub = input('Enter Subject : ')
for entry in subjects:
    if subjects[entry].__contains__(inputSub):
        print(entry)
