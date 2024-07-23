import numpy as np
import pandas as pd
from pandas import Series, DataFrame

###############################################
##  Missing Data
###############################################


############ filter out missing data

s = Series([1,2,np.nan, 9])
d = s.dropna()
print(s, '\n') # original remains unchanged
print(d, '\n')

# data frames by default drop any row with na values if use dropna
df = DataFrame([[1,2,3], [np.nan, 3,4], [4,4,5]])
d = df.dropna()
print(d, '\n')
# only drop if all values are na
d = df.dropna(how='all')
print(d, '\n')

# how to drop columns instead of rows
d = df.dropna(axis='columns')
print(d, '\n')

# can also set a threshold
d = df.dropna(thresh=2)
print(d, '\n')

############# fill in missing data

d = df.fillna(0)
print(d, '\n')

# fill different values depending on column
d = df.fillna({0: 10, 1: 20, 2: 30})
print(d, '\n')

# can fill by using mean
d = df.fillna(df.mean())
print(d, '\n')


###############################################
## Data Transformation
###############################################

df = DataFrame({
    "k1": ["one", "two"] * 3 + ["two"],
    "k2": [1,1,2,3,3,4,4]
})
print(df, '\n')

# find duplicate rows (all row values equal)
print(df.duplicated(), '\n')

d = df.drop_duplicates()
print(d, '\n')

# if only want to drop rows if certain columns have same values
d = df.drop_duplicates(subset=["k1"])
print(d, '\n')
# by default first values are kept but can change this by adding keep="last"


############# map ########################

df = DataFrame({
    'food': ['bacon', 'egg'],
    'ounces': [23, 9]
})
print(df, '\n')

meet_to_animal = {
    'bacon': 'pig',
    'egg': 'chicken'
}

# map can accept an object or a function
df['animal'] = df['food'].map(meet_to_animal)
print(df, '\n') # adds animal column that maps to meet
"""
    food  ounces   animal
0  bacon      23      pig
1    egg       9  chicken
"""

# map with function
def get_animal(x):
    return meet_to_animal[x]
d = df['food'].map(get_animal)
print(d, '\n')


# replace

s = Series([1,2,3,4])
t = s.replace(3, 99)
print(t, '\n')

# can replace multiple values at once
t = s.replace([2,4], 0)
print(t, '\n')

# can replace with different values too
t = s.replace([2,4], [33,34])
print(t, '\n')

# can also use a dict to do this
t = s.replace({2:33, 3:34})
print(t, '\n')

# can update index names
df = DataFrame(np.arange(12).reshape(3,4), index=["Ohio", "california", "nevada"], columns=["one", "two", "three", "four"])
print(df, '\n')
def transform(x):
    return x[:4].upper()
df.index = df.index.map(transform)
print(df, '\n')

# can rename anything (original unaffected)
d = df.rename(index={'OHIO': 'INDIANA'}, columns={'three': 'tres'})
print(d, '\n')




###############################################
## outliers
###############################################

df = DataFrame(np.random.standard_normal((1000, 4)))
print(df, '\n')

col = df[2] # gets all rows in column position 2
# print(col, '\n')
# get all values in this column above 3
x = col[col.abs() > 3]
print(x, '\n')

# show entire row if any of the row's columns have a value > 3
x = df[(df.abs() > 3).any(axis="columns")]
print(x, '\n')

# if need to cap values between certain amount (here -3 to 3)
df[df.abs() > 3] = np.sign(df) * 3
print(df, '\n')


###############################################
## get_dummies (categorical values expand to multiple columns)
###############################################

df = DataFrame([['A',33,'bill'],['B',44,'claire']], columns=['cabin', 'age', 'name'])
print(df, '\n')
"""
  cabin  age    name
0     A   33    bill
1     B   44  claire
"""
x = pd.get_dummies(df['cabin'], prefix="cabin")
y = df[['age', 'name']].join(x)
print(y, '\n')
"""
   age    name  cabin_A  cabin_B
0   33    bill     True    False
1   44  claire    False     True
"""

# what if column has multiple values? (like movie genres) how create a dummy variable for that?
df = DataFrame([['die hard', 'action|comedy'], ['forest gump', 'romance|comedy']], columns=['title', 'genre'])
print(df, '\n')
d = df['genre'].str.get_dummies("|")
print(d, '\n')
e = df.join(d.add_prefix('Genre_'))
print(e, '\n')


















