import numpy as np
import pandas as pd
from pandas import Series, DataFrame

v = Series(['apple', 'orange', 'apple'] * 2)
print(v, '\n')

print(v.unique())
print(v.value_counts())

# often data is stored in DIMENSION TABLES so data is more compactly and efficiently stored
# zero represents apples and one represents oranges
v = Series([0,1,0,0] * 2)
d = Series(['apples', 'oranges'])
# with "take" we can put both together to see how values match up
t = d.take(v)
print(t, '\n')
# see that this data will take up much less space than writing apples and oranges n times

######### converting to categorical pandas type ############################
fruits = ['apple', 'orange', 'apple', 'apple'] * 2
N = len(fruits)
rng = np.random.default_rng(seed=12345)
df = DataFrame({
    'fruit': fruits,
    'basket_id': np.arange(N),
    'range': rng.integers(3,15, size=N),
    'weight': rng.uniform(0, 4, size=N)
}, columns=['fruit', 'basket_id', 'range', 'weight'])
print(df, '\n')

fc = df['fruit'].astype('category')
print(fc, '\n')
# shows array of all values as well as unique Categories
print(fc.array, '\n')
# type is a pandas Categorical
print(type(fc.array), '\n')
# get distinct Categories
print(fc.array.categories, '\n')
# get 0,1 codes for each value in entire array
print(fc.array.codes, '\n')
# get dict of codes to categories {0: 'apple', 1: 'orange'}
print(dict(enumerate(fc.array.categories)), '\n')

# can create Categorical type this way as well
c = pd.Categorical(['foo', 'baz', 'bar'])
print(c, '\n')

# can put codes and categories together like this
codes = [0,1,0,2,1,1]
categories = ['foo', 'baz', 'bar']
# put ordered True if categories need to be kept in order you wrote them above. Otherwise there is no guarantee that 1 will equal baz
x = pd.Categorical.from_codes(codes, categories, ordered=True)
print(x, '\n')


############## Categorical methods ################
s = Series(['a', 'b', 'c', 'd'] * 2)
cs = s.astype('category')
print(cs, '\n')
# use .cat property
print(cs.cat.categories, '\n')
print(cs.cat.codes, '\n')
# may want to add new category later.  here we add 'e'
cs2 = cs.cat.set_categories(['a', 'b', 'c', 'd', 'e'])
# a-d values remain unchanged
print(cs2, '\n')
# but now we have the ability to add more data for e
print(cs2.value_counts(), '\n')

# can remove unused categories (useful after filtering)
cs3 = cs2[cs2.isin(['b', 'd'])]
print(cs3, '\n')
cs4 = cs3.cat.remove_unused_categories()
print(cs4, '\n')


###### make one hot encoding ##########
s = Series(['a', 'b', 'c', 'd'] * 2, dtype='category')
# one column with either a,b,c or d as the value for each row
print(s, '\n')
"""
0    a
1    b
2    c
3    d
4    a
5    b
6    c
7    d
"""
# spreads a,b,c,d out to 4 columns and value for each row is either a 1 or 0
t = pd.get_dummies(s, dtype='float')
print(t, '\n')
"""
     a    b    c    d
0  1.0  0.0  0.0  0.0
1  0.0  1.0  0.0  0.0
2  0.0  0.0  1.0  0.0
3  0.0  0.0  0.0  1.0
4  1.0  0.0  0.0  0.0
5  0.0  1.0  0.0  0.0
6  0.0  0.0  1.0  0.0
7  0.0  0.0  0.0  1.0
"""













