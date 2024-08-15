import pandas as pd
from pandas import Series, DataFrame
import numpy as np

# dataFrame to numpy
df = DataFrame({
    'a': [1,2,3],
    'b': [4,5,6]
})
print(df, '\n')
n = df.to_numpy()
print(n, '\n')
# put it back
df = DataFrame(n, columns=['a', 'b'])
print(df, '\n')

# should only use to_numpy when data is of same type, otherwise won't be a numpy array but standard python object

# only want one column
n = df.loc[:, 'b'].to_numpy()
print(n, '\n') # [4,5,6]

###################################################
## Movie Dataset Example
###################################################

users = DataFrame({
    'user_id': np.arange(1,6),
    'gender': ['F', 'M', 'F', 'M', 'M'],
})
print(users, '\n')

ratings = DataFrame({
    'user_id': [1,1,2,3,4],
    'movie_id': [1,2,1,2,2],
    'rating': [5,4,5,2,1]
})
print(ratings, '\n')

movies = DataFrame({
    'movie_id': [1,2,3,4],
    'title': ['toy story', 'rambo', 'forest gump', 'avengers']
})
print(movies, '\n')

data = pd.merge(pd.merge(users, ratings), movies)
print(data, '\n')
print(data.iloc[0], '\n')

mean_ratings = data.pivot_table(
    'rating',
    index='title',
    columns='gender',
    aggfunc='mean'
)
print(mean_ratings, '\n')

# see how many ratings each title has
ratings_by_title = data.groupby('title').size()
print(ratings_by_title, '\n')

# see movies with more than 2 reviews
highly_reviewed = ratings_by_title.index[ratings_by_title > 2]
print(highly_reviewed, '\n')

highly_reviewed_mean = mean_ratings.loc[highly_reviewed]
print(highly_reviewed_mean, '\n')

top_female_ratings = mean_ratings.sort_values("F", ascending=False)
print(top_female_ratings, '\n')





