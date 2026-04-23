# Set Creation Create a Python set containing the first 10 even numbers {2, 4, 6,8,10}.
# Write a program to display this set.

set1 = set(range(2, 11, 2))
print(set1)         # {2, 4, 6, 8, 10}
set1_tuple = (2,4,6,8,10)
print("set1_tuple: ", set1_tuple)       ##set1_tuple:  (2, 4, 6, 8, 10)

set2 = {}
lst = []
for i in range(1, 11):
    if i%2 == 0:
        lst.append(i)
set2 = set(lst)

print(set2)
# {2, 4, 6, 8, 10}
