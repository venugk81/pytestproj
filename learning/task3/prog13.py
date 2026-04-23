# Tuple and Set Combinations Create a tuple containing the names of your friend's favorite movies and
# a set containing the names of your favorite movies. Write a Python program to find and display common elements


my_friend_movies_tup = {"movie 1", "movie 2", "movie 3", "movie 4"}
friend_movies_set = ("my movie 1", "my movie 2", "movie 2", "movie 4")

common_movies = my_friend_movies_tup.intersection(friend_movies_set)
print("Common movies: ", common_movies)

uncommon_movies = my_friend_movies_tup.difference(friend_movies_set)

print("uncommon movies:", uncommon_movies)

# Common movies:  {'movie 2', 'movie 4'}
# uncommon movies: {'movie 3', 'movie 1'}
