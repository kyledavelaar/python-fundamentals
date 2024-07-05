



# immutable and fixed length

a = ("a", "b", "c")
print(a)

# don't need () for a tuple
b = "d", "e", "f"
print(b)

# can cast list to tuple
c = tuple([1,2,3,4])
print(c)

# if object inside tuple is mutable, you can mutate that.  But can't mutate boolean for example
d = (True, [1,2], False)
d[1].append(3)
print(d)

# can use + to concatenate tuples
e = (1,2) + (3,4)
print(e)

# can use * to copy values n times
f = ("foo", "zoo") * 3
print(f)

# can destructure (unpack) tuples
g = ("do", "re", "mi")
do, re, mi = g
print(do, re, mi)

# destructing is common when iterating
h = ((1,2), (2,3), (3,4))
for a,b in h:
    print(a,b)

# use * to pluck values
i = (1,2,3,4)
one,two,*rest = i
print(one)
print(two)
print(rest)

# count: counts number of occurrences of a value
print(i.count(3)) # 1


