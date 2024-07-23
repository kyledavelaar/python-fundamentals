import numpy as np
import pandas as pd
from pandas import Series, DataFrame


######################################################
## hierarchical indexing
######################################################
s = Series(
    np.random.uniform(size=9),
    index=[
        ["a", "a", "a", "b", "b", "c", "c", "d", "d"],
        [1, 2, 3, 1, 3, 1, 2, 2, 3]
    ]
)
print(s, '\n')
"""
a  1    0.533901
   2    0.512907
   3    0.166826
b  1    0.495279
   3    0.865113
c  1    0.547459
   2    0.934798
d  2    0.663387
   3    0.374975
dtype: float64
"""

# can now select parts of data for just letter indexes
print(s['b':'c'])
"""
b  1    0.236520
   3    0.740408
c  1    0.358694
   2    0.524192
dtype: float64
"""

print(s.loc[['a', 'd']])
"""
a  1    0.916834
   2    0.730898
   3    0.459966
d  2    0.398426
   3    0.835761
dtype: float64
"""

# can select "inner" layer too
# get value for index 2 on every outer (letter) index
# note: b had no value for 2, only index 1 and 3
print(s.loc[:,2])
"""
a    0.386676
c    0.265601
d    0.367414
dtype: float64
"""

# UNSTACK takes 2 indices and uses one as a column
x = s.unstack()
print(x, '\n')
"""
          1         2         3
a  0.759018  0.976466  0.990083
b  0.939451       NaN  0.888737
c  0.145833  0.212338       NaN
d       NaN  0.356054  0.909908
"""

# STACK does the opposite
y = x.unstack()
print(y, '\n')


# columns can be hierarchical too
df = pd.DataFrame(
    np.arange(12).reshape((4, 3)),
    index=[
        ["a", "a", "b", "b"],
        [1, 2, 1, 2]
    ],
    columns=[
        ["Ohio", "Ohio", "Colorado"],
        ["Green", "Red", "Green"]
    ]
)
print(df, '\n')


######################################################
## Re-ordering and Sorting
######################################################


# df = DataFrame({
#     'name': ['kyle', 'bill', 'charlie'],
#     "age": [23, 33, 11],
# }, index=['user1', 'user2', 'user3'])
# print(df, '\n')

# multi-level can sort by second level, in this case the integers
s = df.sort_index(level=1)
print(s, '\n')
"""
     Ohio     Colorado
    Green Red    Green
a 1     0   1        2
b 1     6   7        8
a 2     3   4        5
b 2     9  10       11
"""

# put integer index on outside and letter index on inside
s = df.swaplevel()
print(s, '\n')
"""
     Ohio     Colorado
    Green Red    Green
1 a     0   1        2
2 a     3   4        5
1 b     6   7        8
2 b     9  10       11
"""

######################################################
## Make index from data frame column
######################################################

df = DataFrame({
    'a': range(7),
    'b': range(7, 0, -1),
    'c': ['one'] * 3 + ['two'] * 4,
    'd': [0,1,2,0,1,2,3]
})
print(df, '\n')
"""
   a  b    c  d
0  0  7  one  0
1  1  6  one  1
2  2  5  one  2
3  3  4  two  0
4  4  3  two  1
5  5  2  two  2
6  6  1  two  3
"""

df2 = df.set_index(['c', 'd']) # drop=False if don't want columns removed
print(df2, '\n')
"""
       a  b
c   d
one 0  0  7
    1  1  6
    2  2  5
two 0  3  4
    1  4  3
    2  5  2
    3  6  1
"""

# put index back as rows
df3 = df2.reset_index()
print(df3, '\n')



######################################################
## Join
######################################################


df1 = DataFrame({
    'key': ["b", "b", "a", "c", "a", "a", "b"],
    'data1': Series(range(7), dtype='Int64')
})
print(df1, '\n')
"""
  key  data1
0   b      0
1   b      1
2   a      2
3   c      3
4   a      4
5   a      5
6   b      6
"""

df2 = DataFrame({
    'key': ['a', 'b', 'd'],
    'data2': Series(range(3), dtype='Int64')
})
print(df2, '\n')
"""
  key  data2
0   a      0
1   b      1
2   d      2
"""

# many to one
# data2 is the one value (one value for a, one for b, etc.), think primary key in sql
# data1 is the many that uses primary key of other 'table'
# merging on the key column
df3 = pd.merge(df1, df2, on='key')
print(df3, '\n')
"""
  key  data1  data2
0   b      0      1
1   b      1      1
2   a      2      0
3   a      4      0
4   a      5      0
5   b      6      1
"""

# when column names are different you can specify which to choose and which order to put them
df1 = DataFrame({
    "lkey": ["b", "b", "a", "c", "a", "a", "b"],
    "data1": pd.Series(range(7), dtype="Int64")
})
df2 = DataFrame({
    "rkey": ["a", "b", "d"],
    "data2": pd.Series(range(3), dtype="Int64")
})

df3 = pd.merge(df1, df2, left_on="lkey", right_on="rkey")
print(df3, '\n')
"""
  lkey  data1 rkey  data2
0    b      0    b      1
1    b      1    b      1
2    a      2    a      0
3    a      4    a      0
4    a      5    a      0
5    b      6    b      1
"""
# note that this is an INNER join, meaning only values found in both tables will be used. c and d are not present above

# if you want outer, left or right joins you can specify this
# outer join (like in sql) will fill empty values with NA or NaN
df3 = pd.merge(df1, df2, left_on="lkey", right_on="rkey", how='outer')
print(df3, '\n')
"""
  lkey  data1 rkey  data2
0    a      2    a      0
1    a      4    a      0
2    a      5    a      0
3    b      0    b      1
4    b      1    b      1
5    b      6    b      1
6    c      3  NaN   <NA>
7  NaN   <NA>    d      2
"""

# many to many (cartesian product)
# key from first table matched to every value it exists in second table...keep doing this for all values
# first b (0, 1), (0, 3)
# second b (1, 1), (1, 3)
# etc.
df1 = pd.DataFrame({
    "key": ["b", "b", "a", "c", "a", "b"],
    "data1": pd.Series(range(6), dtype="Int64")
})
print(df1, '\n')
"""
  key  data1
0   b      0
1   b      1
2   a      2
3   c      3
4   a      4
5   b      5
"""
df2 = pd.DataFrame({
    "key": ["a", "b", "a", "b", "d"],
    "data2": pd.Series(range(5), dtype="Int64")
})
print(df2, '\n')
"""
  key  data2
0   a      0
1   b      1
2   a      2
3   b      3
4   d      4
"""
df3 = pd.merge(df1, df2, on='key', how='left')
print(df3, '\n')

"""
   key  data1  data2
0    b      0      1
1    b      0      3
2    b      1      1
3    b      1      3
4    a      2      0
5    a      2      2
6    c      3   <NA>
7    a      4      0
8    a      4      2
9    b      5      1
10   b      5      3
"""

# can merge using index
l = DataFrame({
    'key': ["a", "b", "a", "a", "b", "c"],
    'value': Series(range(6), dtype='Int64')
})
r = DataFrame(
    {'group_val': [3.0, 7.5]},
    index=['a', 'b']
)

m = pd.merge(l, r, left_on='key', right_index=True)
print(m, '\n')
"""
  key  value  group_val
0   a      0        3.0
1   b      1        7.5
2   a      2        3.0
3   a      3        3.0
4   b      4        7.5
"""
# note that c is dropped b/c merge is "inner" by default.  can use how="outer" to include c

# can use pd.join() as well to merge by index


######################################################
## Concat
######################################################

s1 = Series([0,1], index=['a', 'b'])
s2 = Series([2,3], index=['c', 'd'])
s3 = pd.concat([s1, s2])
print(s3, '\n')
"""
a    0
b    1
c    2
d    3
dtype: int64
"""

# concating on columns makes a data frame
s3 = pd.concat([s1, s2], axis='columns', keys=['first', 'second'])
print(s3, '\n')
"""
   first  second
a    0.0     NaN
b    1.0     NaN
c    NaN     2.0
d    NaN     3.0
"""

######################################################
## Overlap
######################################################
s1 = Series(
    [np.nan, 2, 1, 99],
    index=['f', 'e', 'd', 'g']
)
s2 = Series(
    [100, np.nan, np.nan, 3],
    index=['g', 'd', 'e', 'f']
)
# use value in s1 if it exists, otherwise use value in s2 (for that index)
c = s1.combine_first(s2)
print(c, '\n')
"""
d     1.0
e     2.0
f     3.0
g    99.0
"""

# patch missing values based on column in data frame
df1 = DataFrame({
    'a': [1, np.nan, 3],
    'b': [np.nan, 5, 6]
})
df2 = DataFrame({
    'a': [9, 10, 11]
})
x = df1.combine_first(df2)
print(x, '\n')
"""
      a    b
0   1.0  NaN
1  10.0  5.0
2   3.0  6.0
"""


######################################################
## Reshape
######################################################

# stack switches rows and columns and turns df into a series with 2 indices
df = DataFrame(
    np.arange(6).reshape(2,3),
    index=pd.Index(['Ohio', 'Cali'], name='state'),
    columns=pd.Index(['one', 'two', 'three'], name='number')
)
print(df, '\n')
"""
number  one  two  three
state
Ohio      0    1      2
Cali      3    4      5

"""
x = df.stack()
print(x, '\n')
"""
state  number
Ohio   one       0
       two       1
       three     2
Cali   one       3
       two       4
       three     5
dtype: int64
"""
# unstack switches rows to columns (putting it back to original)
print(x.unstack())

# can also unstack for certain levels
print(x.unstack(level="state"))
"""
state   Ohio  Cali
number
one        0     3
two        1     4
three      2     5
"""
















