import numpy as np
import pandas as pd
from pandas import Series, DataFrame


d = {
    "user1": "kyle@yahoo.com",
    "user2": "bill@gmail.com",
    "user3": np.nan
}
df = Series(d)
print(df, '\n')

# returns boolean for each row
print(df.str.contains("gmail"), '\n')

# convert na to strings
x = df.astype('string')
print(x, '\n')

# can use regular expressions too
x = df.str.findall(r"(\w+)@(\w+)")
print(x, '\n')
"""
user1       [(kyle, yahoo)]
user2       [(bill, gmail)]
user3                NaN
dtype: object
"""

# to get one group value from multiple groups
g = x.str[0] # groups are wrapped in a list so just get the () part
print(g, '\n')
h = g.str.get(1) # now get the value at index 1 in the tuple
print(h, '\n')
"""
user1    yahoo
user2    gmail
user3      NaN
dtype: object
"""

# can slice any string as well
x = df.str[:2]
print(x, '\n')
"""
user1     ky
user2     bi
user3    NaN
dtype: object
"""

# extract will make groups into a data frame
y = df.str.extract(r"(\w+)@(\w+)")
print(y, '\n')
"""
          0      1
user1  kyle  yahoo
user2  bill  gmail
user3   NaN    NaN
"""








