# Set Operations and Methods Write a Python program that takes a set of numbers and performs the following operations:
# Add a new number to the set.
# Remove a number from the set.
# Check if a specific number is in the set.
# Find the size of the set.

set1 = {10,2,30,4,50,6,70}
set1.add(11)
print("number added: ", set1)
print(type(set1))

#  Note: Set items are unchangeable, but you can remove items and add new items.
set1.remove(6)
print("number removed: ", set1)

check_num = 6
def check_number_in_set(set1, num):
    found = False
    for item in set1:
        if item == check_num:
            print("Set has a number: ", num)
            found = True
            break
    if not found:
        print("Set has no number: ", num)

check_num = 6
check_number_in_set(set1, check_num)

print("size of the set: ", len(set1) , " and its elements: ", set1)
