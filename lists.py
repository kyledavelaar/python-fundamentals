

list1 = ['a', 'b', 'c']
print(list1[0:1]) # a
print(list1[:-2]) # a
print(list1[1:2]) # b

# can add "step" as third arg
l1 = [1,2,3,4,5,6]
print(l1[::2])
# step of -1 would reverse the list
print(l1[::-1])

list2 = [['a', 'b'], ['c', 'd']]
# print(list2[0:1,0:1]) # numpy notation


# can also assign to multiple items at once
l3 = [1,2,3,4]
l3[1:3] = [5,6]
print(l3)



# extend: append multiple items to list with
a = [1,2,3]
a.extend([4,5,6])
print(a)

# use enumerate to get access to index
for index, value in enumerate(a):
    print(index, value)

# sort
print(sorted([3,2,1,5,3,2]))

# zip
seq1 = ["one", "two", "three"]
seq2 = ["uno", "dos", "tres"]
zipped = list(zip(seq1, seq2))
print(zipped) # [(one, uno), (two, dos), (three, tres)]

# reversed
r = list(reversed(range(10)))
print(r)

# map
words = ['one', 'two', 'three']
caps = list(map(str.upper, words))
print(caps)
















