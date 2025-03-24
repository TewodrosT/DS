# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

netflix_df.value_counts('type')
netflix_movies_df = netflix_df.loc[netflix_df['type'] == "Movie"]
netflix_movies_df.head()
long_movies_s1990 = netflix_movies_df.loc[netflix_movies_df['release_year'].between(1990,1999)]
duration_dist = long_movies_s1990.value_counts('duration')
long_movies_s1990['duration'].value_counts()
print(duration_dist.max())
duration = duration_dist.idxmax()
short_movie= netflix_movies_df.loc[(netflix_movies_df['release_year'].between(1990,1999)) 
                                         & (netflix_movies_df['duration'] < 90) &(netflix_movies_df['genre'] == 'Action') ]
short_movie_count = len(short_movie)
print(duration)