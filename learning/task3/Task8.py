# Create a Python tuple containing the names of your favorite fruits.
# Write a Python program to print each fruit name from the tuple.




tup = ('apple', 'banana', 'orange', 'mango', 'kiwi')
for fruit in tup:
    print(fruit)


# Tuple Operations Given two tuples, write a Python program to concatenate
# them into a single tuple and then find the length of the resulting tuple.

tup1 = ('apple', 'banana', 'orange', 'mango', 'kiwi')
tup2 = (1,2,4)
tup3= tup1 + tup2
print(tup3)
print("tup len: ", len(tup3))

# Tuple and Set Conversion Write a Python program that takes a tuple of integers and converts it into a set.
# Then, find and print the maximum and minimum value from the set.

tup2 = (1,9,4)
set1 = set(tup2)
print(set1)
print("min: ", min(set1))
print("max: ", max(set1))


