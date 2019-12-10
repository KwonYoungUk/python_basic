# string index
myStr = 'python';
print(myStr[0])
print(myStr[-1])

# string slicing
myStr = 'Hello World! My name is Python'
print(myStr[1:5])
print(myStr[5:])
print(myStr[:5])

# string.split()
myStr = 'Hello World! My name is Python'
print(myStr.split())
print(myStr.split('!'))

# Docstring
""" 
이것도 주석입니다. 
아무것도 하지 않죠.
주로 함수에 관한 설명을 달기 위한 주석입니다
"""

# print()
print('Hello', end=' World!')
print('Hello')
print('Hello', end='')
print()

# packing / unpacking
"""
packing => myTuple = 1, 2, 3
unPacking => myTupleNumber1, myTupleNumber2, myTupleNumber3 = myTuple
"""
myTuple = (1, 2, 3)
print(myTuple)
tuple1, tuple2, tuple3 = myTuple
print('{}, {}, {}'.format(tuple1, tuple2, tuple3))

num1 = 1
num2 = 2
print('{}, {}'.format(num1, num2))

num1, num2 = num2, num1
print('{}, {}'.format(num1, num2))

# for Loop
for num1 in range(1, 100):
    print("for Loop : {}".format(num1))

# range()
for num1 in [0, 1, 2]:
    print(num1)

for num1 in range(0, 3):
    print(num1)

"""
# while Loop
while Condition:
    code1
    code2
    ....
value = 1
while value < 5:
    print(value)
    value += 1

"""
