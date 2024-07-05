


a = ("one", "two", "three")
b = ("four", "five", "six")

def zipTuples(a, b):
    c = ()
    for i, v in enumerate(a):
        d = ((v, b[i]),) # need to add , at end for tuples!
        c = c + d

    return c


res = zipTuples(a,b)
print(res)



list1 = ["cat", "dog"]
list2 = ["bird", "parrot"]

def zipLists(a, b):
    c = []
    for i, v in enumerate(a):
        c.append([v, b[i]])
    return c

print(zipLists(list1, list2))