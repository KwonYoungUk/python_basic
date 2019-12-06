import random

# .### -> class Method / ### -> function
# list Addtional
# list init
myList = ['es1', 'es2', 'es3', 'es4']
print(myList)

# .append(element)/.insert(index, element)
myList.append('es5');
myList.insert(0, 'es0');
print(myList)

# delete element
del myList[2]
print(myList)

# .clear()
myList.clear()
print(myList)

# .append(element)
for i in range(1, 100):
    myList.append('es' + str(i))
print(myList)

# .index(element)
print(myList.index('es3'))

# list index access
print(myList[4])

# slicing(startIndex : endIndex)
print(myList[1:3])

# random data generate
myList.clear()
testIndex = []
for i in range(1, 10):
    suffix = random.randint(1, 10)
    if testIndex.__contains__(suffix):
        continue
    else:
        testIndex.append(suffix)
        myList.append('test' + str(suffix))

print(myList)
# .sort()
myList.sort()
print(myList)

# .count('element')
print(myList.count('test1'))

# len(Collection)
print(len(myList))

# Tuple
# init Tuple -> a = ('a', 'b', 'c', ...) or 'a', 'b', 'c'...
myTuple = (1, 2, 3)
print(type(myTuple))
myTuple2 = 1, 2, 3
print(type(myTuple2))

# inner Loop
for outer in range(2, 10):
    for inner in range(2, 10):
        print('{}X{}={}'.format(outer, inner, outer*inner))
    print()

# Comprehension
# forLoop oddNumberList generate
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
oddNumbers = []
for number in numbers:
    if number % 2 != 0:
        oddNumbers.append(number)

print(oddNumbers)

# Comprehension oddNumberList generate
print([number for number in range(1, 11) if number % 2 == 1])