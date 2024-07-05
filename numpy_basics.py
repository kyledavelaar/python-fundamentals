import numpy as np

# ndarray must be of same type
data = np.array([[1.5, -0.1, 3], [0, -3, 6.5]])
md = data * 100
print(md)
print(data) # note that data object does not change

ad = data + data
print(ad)

print(data.shape) # (2,3) two arrays of 3 items each
print(data.dtype)

zeros = np.zeros(10)
print(zeros)
ones = np.ones(10)
print(ones)

two_d_zeros = np.zeros((3,5)) # 3 inner arrays with 5 zeros each
print(two_d_zeros)

five_numbers = np.arange(5)
print(five_numbers)

# can cast type
ints = np.array([1,2,3])
floats = ints.astype(np.float64)
print(ints.dtype) # once again original ndarray remains unchanged
print(floats.dtype)

################## slicing ############################
# changes to array do mutate original array
# this is different from standard python

x1 = np.arange(10)
print(x1[5:8]) # [5,6,7]
x1[5:8] = 0 # sets 0 on index 5 through 8
print(x1) # does mutate original array

x2 = np.arange(10)
x2[:] = 100 # assigns to every item
print(x2)

# if you don't want to mutate original array you need to use "copy"
x3 = np.arange(10)
x3_copy = x3[5:8].copy()
print(x3_copy)
x3_copy[:] = 100
print(x3) # original not mutated.  if you remove .copy() you'd see x3 would get mutated
print(x3_copy)

################ 2D arrays #######################################

x4 = np.array([[1,2], [3,4], [5,6]])
print(x4[0]) # [1,2]
print(x4[0][1]) # 2
print(x4[0,1]) # 2 np allows this syntax for easier typing

x5 = x4[:2] # [[1,2], [3.4] get 0-2 rows, no comma so get all columns in those rows
print(x5)
x6 = x4[:1,1:] # [[2]] get 0-1 rows and 1-end columns in those rows
print(x6)
x7 = x4[:,:1] # [[1], [3], [5]] get all rows and only first column in those rows
print(x7)
x8 = x4[:,0] # [1,3,5] no colon means put all values for column 0 in single array
print(x8)

# assigning assigns to entire section selected
x4[:,:1] = 99
print(x4) # [[99,2], [99,4], [99,6]]

############## Booleans ##############

names = np.array(["kyle", "bill"])
ages = np.array([32, 77])
print(names == "bill") # [False, True]
# can then use this expression to only return the age for bill
print(ages[names == "bill"]) # [77]
# arrays must be same length for this to work

# ~(x == y) is same as doing x != y
print(~(names == "bill")) # [True, False]

# use & | instead of python's and or
print((names == "kyle") | (names == "bill")) # [True, True]

# set all negative values to 0
n2 = np.array([[-1, 1], [33, -32], [23, 3]])
n2[n2 < 0] = 0
print(n2)

customers = np.array(["microsoft", "disney", "google"])
# if have 1d array you can set entire array inside 2d array to a certain value
n2[customers == "disney"] = 100
print(n2) # [[0,1], [100, 100], [23, 3]]


############ fancy indexing #############################
# can select any indices in any order
n4 = np.array([[1,1,1], [4,4,4], [7,8,9], [3,2,1]])
print(n4[[3,0,2]]) # [[3,2,1], [1,1,1], [7,8,9]]

# negative indices will select from back

# can also pass two arrays to select specific items from the selected array
print(n4[[2,3], [0,0]]) # [7, 3]

########## Transposing ###########################
# T swaps axis
n5 = np.array([[1,2], [3,4], [5,6]])
n6 = n5.T
print(n6) # [[1,3,5], [2,4,6]]
print(n5) # original remains unchanged

# matrix multiplication uses this often (dot product)
print(np.dot(n5.T, n5))

# @ also does matrix multiplication
print(n5.T @ n5) # same output as above




########## Conditionals ####################

# choose x or y depending on c
x1 = [1,2,3]
y1 = [4,5,6]
c1 = [True, False, True]

# how it would be done in standard Python
z = [(x if c else y) for x,y,c in zip(x1,y1,c1)]
print(z) # [1,5,3]

# with np
res = np.where(np.array(c1), np.array(x1), np.array(y1))
print(res) # [1,5,3]

# replace all values with scalar.  which scalar to choose depends on condition
x = np.array([1,3,5,7,8,10])
res2 = np.where(x > 5, 1, 0)
print(res2) # [0,0,0,1,1,1]

# make no changes if doesn't meet condition
res3 = np.where(x > 5, 2, x)
print(res3) # [1,3,5,2,2,2]

############## sum, mean, std #######################

x = np.array([
    [1,2],
    [3,4]
])
print(x.sum()) # 10
# can limit to only certain axis
print(x.sum(axis=0)) # [4,6] (sum each column)
print(x.sum(axis=1)) # [3,7] (sum each row)

# cumulative sum
print(x.cumsum()) # [1,3,6,10]

# min/max
print(x.min()) # 1
print(x.max()) # 4

# index of min/max
print(x.argmin()) # 0
print(x.argmax()) # 3

######### Find count of true false values ###########

x = np.array([True, False, True, False, False])
print((x==1).sum()) # 2
print((x==0).sum()) # 3

# any True? all True?
print(x.any()) # True
print(x.all()) # False


######### sort ###############
x = np.array([4,3,2,6,1,0])
x.sort() # sort does not return anything but mutates original
print(x)
# can also sort only for specific axis by passing axis=0, etc.


########## unique ###############
# gets unique items and sorts them
x = np.array([1,3,1,5,3,2,1,4,6])
print(np.unique(x))

# Python equivalent
x5 = ["c", "d", "c", "a"]
print(sorted(set(x5))) # add set so all values unique


########## save/load np objects ###############
x = np.arange(10)
np.save('./np_objects/range-10', x)

y = np.load('./np_objects/range-10.npy')
print(y)

# can save multiple objects in same file if keyword them and use savez
np.savez('./np_objects/x-and-y', x=x, y=y)

xy = np.load('./np_objects/x-and-y.npz') # note extension is different!  npz
print(xy["x"])
print(xy["y"])



