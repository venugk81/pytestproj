# Set Operations with Lists Create a Python list with duplicate elements
# and convert it into a set to remove duplicates.
# Then, write a program to count how many duplicates were removed.

lst = [1,1,2,3,4,5,5,3,2,2,4,5,3]
list_size = len(lst)
set1 = set(lst)
set_size = len(set1)
print("set elements: ", set1)
print("total number of duplicate elements removed from list: ", (list_size-set_size))