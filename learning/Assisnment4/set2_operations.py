# Set Operations Given two sets, write a Python program to
# find the union, intersection, and difference of these sets.

set1 = {1,2,3,4,5,6,7}
set2 = {10,2,30,4,50,6,70}

union_set = set1.union(set2)
print("Union set: ", union_set)
intersection_set = set1.intersection(set2)
print("Intersection set: ", intersection_set)
intersection_set = set1.difference(set2)
print("Intersection set: ", intersection_set)

# Union set:  {1, 2, 3, 4, 5, 6, 7, 70, 10, 50, 30}
# Intersection set:  {2, 4, 6}
# Intersection set:  {1, 3, 5, 7}

