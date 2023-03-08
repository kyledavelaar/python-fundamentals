print('--------------LISTS----------------')
# lists can be changed and can be of any type
myList = ['a', 'b', 'c']

for letter in myList:
    print(letter)

myList.append(5)

for letter in myList:
    print(letter)


print('--------------TUPLES----------------')
# tuple order can't change
tup = (3, 4, 1)

print('--------------SETS----------------')
# set is unordered and unchangeable but can add/remove items
mySet = {'1', 2, "word"}
mySet.add('added this')
mySet.remove('1')

for x in mySet:
    print(x)


print('--------------DICTIONARY----------------')
# as of python 3.7 dictionaries are ordered
myDict = {
    "one": 1,
    "two": 2
}
myDict['three'] = 3
print(myDict)

for key in myDict:
    print(key)
