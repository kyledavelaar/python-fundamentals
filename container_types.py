print('--------------LISTS----------------')
# lists can be changed and can be of any type
myList = ['a', 'b', 'c']

for letter in myList:
    print(letter)

myList.append(5)

for letter in myList:
    print(letter)


print('--------------TUPLES----------------')
# tuple:
# immutable, order can't change, can't add/remove items, can't reassign items,
# can have duplicates
tup = (3, 4, 1, 1)
for i in tup:
    print(i)

print('--------------SETS----------------')
# unordered and unchangeable but can add/remove items
# don't allow duplicate entries
mySet = {'1', 2, "word", 2}
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
