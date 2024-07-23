import numpy as np
import pandas as pd
from pandas import Series, DataFrame

##################################################################################
## read csv
##################################################################################
df = pd.read_csv('./examples/ex1.csv')
print(df, '\n')

# if no headers, pandas will auto create headers for you
df = pd.read_csv('./examples/ex2.csv', header=None)
print(df, '\n')

# or you can pass your own headers
df = pd.read_csv('./examples/ex2.csv', names=['a', 'b', 'c', 'd', 'message'])
print(df, '\n')

# can use a column as the row indices if want
df = pd.read_csv('./examples/ex1.csv', index_col="message")
print(df, '\n')
"""
         a   b   c   d
message
hello    1   2   3   4
world    5   6   7   8
foo      9  10  11  12
"""

# can use regex for your splitter if not comma separated.  here we search for blank spaces
df = pd.read_csv("./examples/ex3.txt", sep="\s+")
print(df, '\n')

# can skip rows
df = pd.read_csv("./examples/ex4.csv", skiprows=[0,2,3])
print(df, '\n')

# pandas fills in missing data with NaN when it infers most data in colum is an int
# can also explicitly make anything a missing value by adding them to the na_values list
df = pd.read_csv("examples/ex5.csv", na_values=['foo'])
print(df, '\n')

# can also turn off pandas filling in missing data
df = pd.read_csv("examples/ex5.csv", keep_default_na=False)
print(df, '\n')
# because we told pandas to not label anything as na above, isna will return False for every value
print(df.isna())

# can also mix and match na_values and keep_default_na=False to only have na values that you custom add, not any na replacements that pandas adds by default
df = pd.read_csv("examples/ex5.csv", keep_default_na=False, na_values=["NA"])
print(df, '\n')

# can also specify na values per column by passing in a dict to na_values
sentinels = {"message": ["foo", "NA"], "something": ["two"]}
df = pd.read_csv("examples/ex5.csv", na_values=sentinels, keep_default_na=False)
print(df, '\n')

##################################################################################
## read text files in pieces
##################################################################################
# pd.options.display.max_rows = 10
# now all files over 10 rows will shrink down to show only 10

# can also specify num rows here
df = pd.read_csv("examples/ex1.csv", nrows=2)
print(df, '\n')

# chunk size allows you to iterate over chunks
chunker = pd.read_csv("examples/ex6.csv", chunksize=2)
tot = pd.Series([], dtype='int64')
for piece in chunker:
    tot = tot.add(piece["key"].value_counts(), fill_value=0)
tot = tot.sort_values(ascending=False)
print(tot, '\n')
"""
key
Q    3.0
G    2.0
L    2.0
R    2.0
B    1.0
dtype: float64
"""


##################################################################################
## writing
##################################################################################

df = pd.read_csv("examples/ex5.csv")
df.to_csv('examples/out.csv')

# write to stdout, replace na values with NULL, include index/column names or not, etc.
import sys
df.to_csv(sys.stdout, sep="|", na_rep="NULL")
df.to_csv(sys.stdout, sep="|", header=False)
df.to_csv(sys.stdout, sep="|", index=False, columns=['c', 'd', 'message'])

# df = pd.read_csv('examples/ex7.csv')
# print(df, '\n')

##################################################################################
## JSON
##################################################################################
obj = """
{"name": "Wes",
 "cities_lived": ["Akron", "Nashville", "New York", "San Francisco"],
 "pet": null,
 "siblings": [{"name": "Scott", "age": 34, "hobbies": ["guitars", "soccer"]},
              {"name": "Katie", "age": 42, "hobbies": ["diving", "art"]}]
}
"""

import json

# convert to python (null changes to None)
jd = json.loads(obj)
print(jd, '\n')

# convert back to json
js = json.dumps(jd)
print(js, '\n')

# use json.loads result to create data frame
df = DataFrame(jd['siblings'], columns=['name', 'age'])
print(df, '\n')

# can also create data frame directly from json if json is in correct format for a data frame (each object is a row)
from io import StringIO
o2 = """
[{"a": 1, "b": 2, "c": 3},
 {"a": 4, "b": 5, "c": 6},
 {"a": 7, "b": 8, "c": 9}]
"""
df = pd.read_json(StringIO(o2))
print(df, '\n')

# can output to json
df = pd.read_csv('./examples/ex1.csv')
dfj = df.to_json()
print(dfj, '\n')


##################################################################################
## Fetch from api and put in data frame
##################################################################################

import requests
url = "https://api.github.com/repos/pandas-dev/pandas/issues"
resp = requests.get(url)
resp.raise_for_status()
print(resp.json()[0]['title'], '\n')

df = DataFrame(resp.json(), columns=['number', 'title'])
print(df[:10], '\n')












