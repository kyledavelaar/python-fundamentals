import numpy as np
import pandas as pd
from pandas import Series, DataFrame

############### Series ##########

# default index of 0,1,2,3 given to values since no "label" was provided
obj = Series([4,5,6,7])
print(obj)
"""
0 4
1 5
2 6
3 7
dtype int64
"""

# can get array and index values separately
print(obj.array)
print(obj.index)

# can add specific "index/label" to each item
x = Series([3,4,5], index=["three", "four", "five"])
print(x)
print(x.three) # 3

# can perform operations just like in np
print(x[x>3])
print(x ** 2)
# print(x) # operations above do not mutate original

# a Series can be created directly from a Python dictionary
d = { "one": 1, "two": 2 }
x = Series(d)
print(x)
# and it can be converted back to a dict
print(x.to_dict())

# can also exclude keys or re-order dict
y = Series(d, ["two"])
print(y) # only has two key/value


################ DataFrame ##################################
# has both columns and rows
# it is a dictionary of Series all which share the same index

# create DataFrame from dict with equal length lists
data = {
    "state": ["CA", "IL", "NE"],
    "population": [33, 22, 11],
    "year": [2011, 2012, 2013]
}
x = DataFrame(data)
print(x)
"""
  state  population  year
0    CA          33  2011
1    IL          22  2012
2    NE          11  2013
"""

# head() gets first five rows
# tail() gets last five
# print(x.head())

# can put columns in specific order or exclude them
x = DataFrame(data, columns=["year", "state"])
print(x)

# can use dot notation to get entire column and the index
print(x.state)

# can use loc and iloc to get specific values
print(x.loc[1])
"""
year     2012
state      IL
Name: 1, dtype: object
"""

# assign value in every row for a particular column
x.year = 2022
print(x)

# if pass array each row will use the value at each index
x.year = np.arange(2022, 2025)
print(x)

# can create new columns and delete them (cannot create with dot notation)

x["is_cool"] = x.state == "CA"
print(x)
del x["is_cool"]
print(x)

######## nested dictionaries
# the outer dict key will be used as the column label
# the inner dict key will be used as the row index
# if don't want the inner keys to be used as indices you can pass custom ones with index=["twenty-one", "twenty-two"]
d = {
    "CA": { 2021: 1.5, 2022: 3.0 },
    "IL": { 2021: 4.2, 2022: 9.9 },
}
x = DataFrame(d)
print(x)
"""
       CA   IL
2021  1.5  4.2
2022  3.0  9.9
"""

# if need to swap this use "transpose" or T
print(x.T)
# warning transposing disregards the column's type information if they do not all have the same data type

# cast to numpy array (indices are discarded)
print(x.to_numpy()) # [[1.5, .4.2], [3., 9.9]]


################## Indices ############################
# indices are immutable so can be used across multiple DataFrames without issue
# indices can have duplicate values (unlike plain Python)
# if select data["duplicateIndex"] it will select all values for that index,


################### Re-indexing #####################
# create new object with values realigned to new index
x = Series([1,2,3,4], index=["a", "b", "c", "d"])
print(x)

# x remains unchanged
# indices can be re-ordered but any new index value will result in a NaN value or None for a different type
y = x.reindex(["d", "c", "q", "a", "b"])
print(y)
"""
d    4.0
c    3.0
q    NaN
a    1.0
b    2.0
dtype: float64
"""

# can fill values that don't have one for the new index using forward fill
x = Series(["red", "blue", "green"], index=[1,3,5])
print(x)
y = x.reindex(np.arange(1,7), method="ffill")
print(y)

# can reindex columns too if have 2d DataFrame
x = DataFrame({
    "Kyle": { "age": 22, "weight": 180 },
    "Charlie": { "age": 44, "weight": 200 }
})
print(x)
z = x.reindex(columns=["Charlie", "Kyle"])
print(z)

# can also reindex using "loc"
z = x.loc[["weight", "age"], ["Charlie", "Kyle"]]
print(z)


############ Drop entries from an axis ################
x = Series(np.arange(3), index=["a", "b", "c"])
print(x)
y = x.drop(["a", "c"])
print(y)

# can do the same for columns if have a DataFrame
x = DataFrame({
    "Kyle": { "age": 22, "weight": 180 },
    "Charlie": { "age": 44, "weight": 200 }
})
y = x.drop(columns=["Charlie"], index=["weight"])
print(y)
"""
     Kyle
age    22
"""

############## Selection and Filtering ###########
# loc: lookup by label name and/or index name if use [][]
# iloc: lookup by integer position (like traditional Python list index)

x = Series(np.arange(4), index=["a", "b", "c", "d"])
print(x)
# can select using index or typical numpy indexing
print(x["b"]) # 1
print(x.loc["b"]) # 1 (this is preferred way b/c if index is an integer x[1] will not be the position but the label called 1) so to avoid this confusion use loc
print(x[1:3])
"""
b    1
c    2
dtype: int64
"""
# identical to above x[1:3]
print(x[["b", "c"]])

# warning: slicing with labels is inclusive
print(x["b":"c"])


print(x[x > 2]) # only returns 4th item.
# could also use this to assign
x[x > 2] = 99
print(x)
"""
a     0
b     1
c     2
d    99
dtype: int64
"""

# can evaluate expression on every item
print(x > 1)
"""
a    False
b    False
c     True
d     True
dtype: bool
"""


x = DataFrame({
    "Kyle": { "age": 22, "weight": 180 },
    "Charlie": { "age": 44, "weight": 200 }
})
print(x)
"""
        Kyle  Charlie
age       22       44
weight   180      200
"""

# loc with index, column
print(x.loc[["weight"], ["Kyle"]])
"""
        Kyle
weight   180
"""

# iloc gets every row for index at position 1 only
print(x.iloc[1])
"""
Kyle       180
Charlie    200
Name: weight, dtype: int64
"""

# select row at position index 0 (for age) and column at position index 1 (Charlie)
print(x.iloc[0,1]) # 44

# swap positions for age and weight
print(x.iloc[[1,0]])
"""
        Kyle  Charlie
weight   180      200
age       22       44
"""

# swap positions for age/weight and Kyle/Charlie
print(x.iloc[[1,0], [1,0]])
"""
        Charlie  Kyle
weight      200   180
age          44    22
"""

# can also use : for splitting or getting everything
print(x.iloc[:,1:]) # get all rows but only for Charlie b/c his column is at index position 1
"""
        Charlie
age          44
weight      200
"""

# set all Charlie's values
x.iloc[:, 1] = [99, 100]
print(x)

# set all weights to 5
x.iloc[1] = 5
print(x)

############### arithmetic  #####################

# if row/columns not in both datasets, you'll get null values
# you can set these values to whatever you want by using the fill_value option
# here we set x.c values to 0 so the addition won't result in NaN for those items
x = DataFrame(np.arange(4.).reshape(2,2), columns=list("ab"))
print(x)
y = DataFrame(np.arange(6.).reshape(2,3), columns=list("abc"))
print(y)
z = x.add(y, fill_value=0)
print(z)

# operations between DataFrame and Series

# subtraction using one row's values
frame = DataFrame(np.arange(12.).reshape(3,4), columns=list('abcd'), index=['Utah', 'Colorado', 'California'])
series = frame.iloc[0] # 0,1,2,3 gets values from first row
print(frame)
"""
              a    b     c     d
Utah        0.0  1.0   2.0   3.0
Colorado    4.0  5.0   6.0   7.0
California  8.0  9.0  10.0  11.0
"""
print(series)
row_subtracted = frame - series
print(row_subtracted)
# original frame remains unchanged

# subtraction using one column's values
column_b = frame['b']
print(column_b) # 1,5,9
column_subtracted = frame.sub(column_b, axis="index") # need to use .sub() with axis keyword arg to subtract over columns
print(column_subtracted)
"""
              a    b     c     d
Utah        -1.0  0.0   1.0   2.0
Colorado    -1.0  0.0   1.0   2.0
California  -1.0  0.0   1.0   2.0
"""

################### run function on every item #######################

# can run a function on each item
positives = np.abs(column_subtracted)
print(positives)

# also any custom function using "apply"
def add_one(x):
    return x + 1

plus_one = positives.apply(add_one)
print(plus_one)


# can run function across different axis as well
def get_max(n):
    return n.max()

# here columns is a little confusing b/c columns actually gets the max value for every row (across all columns)
max = plus_one.apply(get_max, axis="columns")
print(max) # 3,3,3

# can also return something completely new in different shape
def min_max(n):
    return Series([n.min(), n.max()], index=["min", "max"])

mm = plus_one.apply(min_max, axis="columns")
print(mm)
"""
            min  max
Utah        1.0  3.0
Colorado    1.0  3.0
California  1.0  3.0
"""


################## sort ##############################
x = Series(np.arange(4), index=list('cbad'))
print(x)
sorted_by_index = x.sort_index()
print(sorted_by_index) # sorted a,b,c,d
print(sorted_by_index.sort_values()) # sorted 0,1,2,3

x = DataFrame(np.arange(12).reshape(3,4), index=list('rts'), columns=list('zwyx'))
print(x)
print(x.sort_index())
print(x.sort_index(axis="columns"))
print(x.sort_index(axis="columns", ascending=False))

# can sort values for a particular column
x = DataFrame(np.arange(12, 0, -1).reshape(3,4), index=list('rts'), columns=list('zwyx'))
print(x)
print(x.sort_values(['y'])) # note that all rows will be re-arranged according to the sort order of column y, so you won't just see changes to the order of values in column y but you'll see them for all the other columns as well


################ ranking items #######################
# rank is giving each item a number where they are at in the order
# so -1 is first so it would get a rank of 1, 0 is next so it would get a rank of 2, etc.
# note rank does not sort them
x = Series([3,5,2,-1,0])
print(x.rank()) # 4,5,3,1,2

############ reduction type operations ###################

# sum
x = DataFrame(np.arange(12).reshape(4,3), columns=list('abc'))
print(x)
"""
   a   b   c
0  0   1   2
1  3   4   5
2  6   7   8
3  9  10  11
"""
print(x.sum()) # each column produces a sum of values across all rows // 18, 22, 26
print(x.sum(axis="columns")) # each row produces a sum of values across all columns 3, 12, 21, 30

# describe
print(x.describe())

# unique and value counts
x = Series(['a', 'b', 'c', 'd', 'a', 'd', 'x', 'b', 'c'])
print(x.unique())
print(x.value_counts())
print(x.isin(['x'])) # returns index/bool for if that value(s) exist at that index









