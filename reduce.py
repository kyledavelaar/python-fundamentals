from functools import reduce

################ without lambda
def add(a,b):
    return a + b

y = reduce(add, [1,2,3])
print(y)


############### with lambda
x = reduce(lambda a,b: a+b, [1,2,3], 0)
print(x)


############ reduce dictionary
def build(acc, curr):
    acc[curr] = True
    return acc

x = reduce(build, [1,2,3], {})
print(x)





