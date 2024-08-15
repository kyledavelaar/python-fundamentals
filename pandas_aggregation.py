import numpy as np
import pandas as pd

df = pd.DataFrame({
    'key1': ["a", "a", None, "b", "b", "a", None],
    'key2': pd.Series([1, 2, 1, 2, 1, None, 1], dtype="Int64"),
    # 'data1': np.random.standard_normal(7),
    'data1': np.arange(7),
    # 'data2': np.random.standard_normal(7)
    'data2': np.arange(7)
})

print(df, '\n')
"""
   key1  key2  data1  data2
0     a     1      0      0
1     a     2      1      1
2  None     1      2      2
3     b     2      3      3
4     b     1      4      4
5     a  <NA>      5      5
6  None     1      6
"""

# group object like { a: [0,1,5], b: [3,4] } etc.
grouped = df['data1'].groupby(df['key1'])
# above is identical to df.groupby("key1")["data1"]

# see how many items are in each group.   a: 3, b: 2
print(grouped.size(), '\n')

# to include na indices as well
groupedNa = df['data1'].groupby(df['key1'], dropna=False).size()
print(groupedNa, '\n')

# count removes na row values
# size keeps na row values
print(df['key2'].groupby(df['key1'], dropna=False).count(), '\n') # a: 2
print(df['key2'].groupby(df['key1'], dropna=False).size(), '\n') # a: 3


mean = grouped.mean()
print(mean, '\n')
"""
key1
a    2.0
b    3.5
Name: data1, dtype: float64
"""

# can also group by multiple things
grouped2 = df['data1'].groupby([df['key1'], df['key2']]).mean()
print(grouped2, '\n')
"""
key1  key2
a     1       0.0
      2       1.0
b     1       4.0
      2       3.0
Name: data1, dtype: float64
"""

print(grouped2.unstack(), '\n')
"""
key2    1    2
key1
a     0.0  1.0
b     4.0  3.0
"""

#########################################
## Iterate over groups
#########################################

for name, group in df.groupby('key1'):
    print("name is: ", name)
    print(group, '\n')
"""
name is:  a
  key1  key2  data1  data2
0    a     1      0      0
1    a     2      1      1
5    a  <NA>      5      5
name is:  b
  key1  key2  data1  data2
3    b     2      3      3
4    b     1      4      4
"""

# have tuple when group by multiple keys
for (k1, k2), group in df.groupby(['key1', 'key2']):
    print(k1, k2)
    print(group, '\n')

# convert to a dict
d = {name: group for name, group in df.groupby('key1')}
print(d, '\n')

# can group by columns as well (here grouping based on dict where I specify which columns I want in each group)
group = df.groupby(
    {
        'key1': 'k',
        'key2': 'k',
        'data1': 'd',
        'data2': 'd'
    },
    axis='columns'
)

for group_key, group_values in group:
    print('group_key', group_key, '\n')
    print(group_values, '\n')


# can also groupby using a function to determine how groups are formed
def byLength(n):
    return len(n) > 4
group = df.groupby(byLength, axis='columns')

# should print same as above
for group_key, group_values in group:
    print('group_key', group_key, '\n')
    print(group_values, '\n')

# can move what used to be displayed as an index (key1, key2) to a column
group = df.groupby(['key1', 'key2'], as_index=False)
print(group.mean(), '\n')
"""
  key1  key2  data1  data2
0    a     1    0.0    7.0
1    a     2    1.0    6.0
2    b     1    4.0    3.0
3    b     2    3.0    4.0
"""

#########################################
## Aggregation Methods
#########################################
df['data2'] = np.arange(7, 0, -1)
print(df, '\n')
"""
   key1  key2  data1  data2
0     a     1      0      7
1     a     2      1      6
2  None     1      2      5
3     b     2      3      4
4     b     1      4      3
5     a  <NA>      5      2
6  None     1      6      1
"""

# prints index and value of smallest, can change 1 to n to get any number of smallest values
grouped = df.groupby('key1')
smallest = grouped['data2'].nsmallest(1)
print(smallest, '\n')
"""
key1
a     5    2
b     4    3
Name: data2, dtype: int64
"""

# can use .agg to pass custom aggregation function
def myFunc(arr):
    return len(arr)

lengths = df.agg(myFunc)
print(lengths, '\n')
"""
key1     7
key2     7
data1    7
data2    7
dtype: int64
"""

# describe can be used on groups
print(grouped.describe(), '\n')

###########################################################
# Column-Wise and Multiple Function Application
###########################################################

# can use different aggregate functions for different columns.  here tip_pct is a column and size is another
# we're also using the built in aggregate functions that pandas provides.  we could have created our own as well
# grouped.agg({
#     "tip_pct" : ["min", "max", "mean", "std"],
#     "size" : "sum"
# })


###########################################################
# Apply (the most general purpose groupby method)
###########################################################


data = {
    'Category': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'A'],
    'Values': [10, 20, 15, 10, 25, 20, 5, 30]
}
df = pd.DataFrame(data)
print(df, '\n')

def calculate_range(arr):
    return np.max(arr) - np.min(arr)

# apply runs a custom function on each of the groups and writes new value to the specified column
res = df.groupby('Category', as_index=False)['Values'].apply(calculate_range)
print(res, '\n')
"""
  Category  Values
0        A      25
1        B       5
2        C      10
"""

# can also pass other arguments to the apply method if desired
def sum_with_constant(arr, n):
    return np.sum(arr) + n

res = df.groupby('Category')['Values'].apply(sum_with_constant, 100)
print(res, '\n')


###########################################################
# Common Examples
###########################################################

# fill missing values with the mean
s = pd.Series(np.random.standard_normal(6))
s[::2] = np.nan
print(s, '\n')
s = s.fillna(s.mean())
print(s, '\n')

# fill missing values based on group
states = ['CA', 'NE', 'IA', 'NE']
group_key = ['West', 'West', 'East', 'East']
s2 = pd.Series([100, 200, 10, 30], index=states)
s2.loc[['CA', 'IA']] = np.nan
print(s2, '\n')

def fill_with_mean(group):
    return group.fillna(group.mean())
s3 = s2.groupby(group_key).apply(fill_with_mean)
print(s3, '\n')

# can also fill with default values based on group name
fill_values = { 'East': 44, 'West': 99 }
def fill_with_default(group):
    return group.fillna(fill_values[group.name])
s4 = s2.groupby(group_key).apply(fill_with_default)
print(s4, '\n')

###########################################################
# Transform (like apply but with more restrictions)
###########################################################
df = pd.DataFrame({
    'key': ['a', 'b', 'c'] * 4,
    'value': np.arange(12.)
})
print(df, '\n')

g = df.groupby('key')['value']
print(g.mean(), '\n')

# replace each value in df with its grouped mean value
def get_mean(group):
    return group.mean()
h = g.transform(get_mean)
print(h, '\n')

# for built in aggregation functions we can do this
h = g.transform('mean')
print(h, '\n')


###########################################################
# Pivot Table
###########################################################
df = pd.DataFrame({
    'A': ['foo', 'foo', 'foo', 'foo', 'foo',
          'bar', 'bar', 'bar', 'bar'],
    'B': ['one', 'one', 'one', 'two', 'two',
          'one', 'one', 'two', 'two'],
    'C': ['small', 'large', 'large', 'small',
          'small', 'small', 'large', 'small', 'large'],
    'D': [1, 2, 2, 3, 3, 4, 5, 6, 7],
    'E': [2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5]
})

print("Original DataFrame:\n", df, "\n")

pivot_table = pd.pivot_table(df, values='D', index=['A', 'B'],
                             columns=['C'], aggfunc=np.sum, fill_value=0)

print("Pivot Table:\n", pivot_table)
"""
 C        large  small
A   B
bar one      5      4
    two      7      6
foo one      4      1
    two      0      6
"""


###########################################################
# Cross Tab (get counts of values)
###########################################################

df = pd.DataFrame({
    'A': ['foo', 'foo', 'foo', 'foo', 'foo',
          'bar', 'bar', 'bar', 'bar'],
    'B': ['one', 'one', 'one', 'two', 'two',
          'one', 'one', 'two', 'two'],
    'C': ['small', 'large', 'large', 'small',
          'small', 'small', 'large', 'small', 'large'],
    'D': [1, 2, 2, 3, 3, 4, 5, 6, 7],
    'E': [2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5]
})

print("Original DataFrame:\n", df, "\n")

crosstab = pd.crosstab(df['A'], df['C'])

print("Crosstab:\n", crosstab)
"""
 C    large  small
A
bar      2      2
foo      2      3
"""











