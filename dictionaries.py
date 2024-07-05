


myDict = { 'a': 'a_value', 'b': 'b_value'}
print(list(myDict.keys()))
print(list(myDict.values()))

for key, value in myDict.items():
    print(key, value)

# shorthand for dictionary manipulation (this sets the value as the key and the key as the value)
myDict2 = {v: k for k, v in myDict.items()}
print(myDict2)

# breaking it down
# items() is similar to Object.entries() in javascript
print("items", myDict.items()) # dict_items([('a', 'a_value'), ('b', 'b_value')])

for k, v in myDict.items():
    print(k, v)

# can also add a filter if desire
myDictFiltered = {k: v for k,v in myDict.items() if k == "a" }
print("filtered", myDictFiltered)


#similar type of shorthand as above but for Arrays.
myDict3 = {
    "input_ids": [
        [1,3,4],
        [0,22],
        [4,5,6,7]
    ]
}
myArr2 = [len(x) for x in myDict3["input_ids"]]
print(myArr2) # [3,2,4]


# merge dictionaries
d1 = { "a": 1, "b": 2 }
d1.update({ "b": 3, "c": 4 })
print(d1)


# can create a dict from list of tuples with 2 items each
l1 = [(1, "z"), (2, "x")]
d3 = dict(l1)
print(d3)

# same as above
tuples = zip(range(5), reversed(range(5)))
d2 = dict(tuples)
print(d2)

# get with default value
print(d1.get(1, 'my_default'))

# setdefault gets value if exists, if not it sets with second arg
d4 = {}
d4.setdefault(0, [])
d4.setdefault(0, 'stuff') # doesn't set b/c already exists
d4.setdefault(0, []).append('new one') # shows that setdefault returns value if exists, so we can use that to append to that list
print(d4)

############ defaultdict ##################################################
from collections import defaultdict

# similar to setdefault, if not found sets it for first time, otherwise adds it however you define in function passed to defaultdict
# adding in list is via list.append()
by_letter = defaultdict(list)
print(by_letter)
words = ["apple", "orange", "banana", "bum"]
for word in words:
    by_letter[word[0]].append(word)
print(by_letter)


# dict with char: countOfChar
# adding in int is via +=
char_count = defaultdict(int)
print(char_count)

for char in "hello world":
    char_count[char] += 1

print(char_count)


