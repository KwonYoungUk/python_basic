# name = 'apple'
# print(name[0])
#
# s1 = 'cutty'
# s2 = 'cat'
# s3 = s1 + s2
# print(s3)
#
# print("@" * 3)

# s1 = 'cat'
# s2 = 'Cat'
#
# print(s1 == s2)
# print(s1 == 'cat')

# print(len('kyo5213'))
#
# myStr = 'Monty Python'
# s1 = myStr[0:2]
# print(s1)

# s = 'apple'
# s2 = ''
# for ch in s:
#     s2 += ch
#     print(s2)

# s = 'apple'
# print(s)
# print(s.upper())

# word = 'banana'
# print(word.find('a'))
# print(word.find('na'))
# print(word.find('na', 3))

# word = input("Enter Target Word : ")
# rpWord = input("Enter Replace Word : ")
#
# if rpWord in word:
#     word = word.replace(rpWord, rpWord.upper())
#
# print(word)

# word = input("Enter Word : ")
# word = word.swapcase()
#
# upperCount = 0
# lowerCount = 0
# for ch in word:
#     if ch.isupper():
#         upperCount += 1
#     elif ch.islower():
#         lowerCount += 1
#
# print(word)
# print("Upper Count = {}".format(upperCount))
# print("Lower Count = {}".format(lowerCount))

# cheese = ['cheddar', 'edam', 'gouda']
# numbers = [1, 3, 5, 7, 9, 11]
#
# for ch in cheese:
#     print(ch)
#
# for num in numbers:
#     print(num * 2)

# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# d = a * 3
# print(c)
# print(d)

# listSize = int(input("Enter List Size : "))
# list = []
#
# for i in range(listSize):
#     list.append(input())
#
# print(list)

# l1 = ['x', 'y', 'z']
# l1.append('a')
# print(l1)
#
# l1.insert(0, 'b')
# print(l1)
#
# l1.sort()
# print(l1)
#
# l1.pop(0)
# print(l1)
#
# l1.remove('b')
# print(l1)

# dList = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(dList)

outerList = []
for num1 in range(2, 10):
    innerList = []
    for num2 in range(2, 10):
        innerList.append(num1 * num2)
    outerList.append(innerList)
    print(innerList)
