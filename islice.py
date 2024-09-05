from itertools import islice

"""
    can stream any iterator and slice it so entire list is not needed to be stored in memory while looping
    often used for reading files b/c don't want entire file in memory
"""

# works for built in iterators
n = [1,2,3,4,5]

for i in islice(n, 2):
    print(i)


# works for custom built iterators
class MyIter:
    def __init__(self, n):
        self.n = n
    def __iter__(self):
        return iter(list(range(self.n)))

myIter = MyIter(5)

for i in islice(myIter, 2):
    print(i)
