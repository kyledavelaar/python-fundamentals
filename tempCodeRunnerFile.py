
# mean = grouped.mean()
# print(mean, '\n')
# """
# key1
# a    2.0
# b    3.5
# Name: data1, dtype: float64
# """

# # can also group by multiple things
# grouped2 = df['data1'].groupby([df['key1'], df['key2']]).mean()
# print(grouped2, '\n')
# """
# key1  key2
# a     1       0.0
#       2       1.0
# b     1       4.0
#       2       3.0
# Name: data1, dtype: float64
# """

# print(grouped2.unstack(), '\n')
# """
# key2    1    2
# key1
# a     0.0  1.0
# b     4.0  3.0
# """















