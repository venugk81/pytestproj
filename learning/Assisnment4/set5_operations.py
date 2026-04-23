# Construct a set1 using range () with elements from 500 to 700 elements inside it,
# Remove element 1000 such that it doesn’t throw an error in output.
# Add elements from 750 to 850 in the set.
# Say, set2={600,745,824,580}. Perform all set operations.

set1 = set(range(500, 700, 20))
print("set: ", set1)

# set1.remove(100)
# #### throws an error if tried to remove an element which doesn't contain in a set
set1.discard(1000)
# duscard removes and element and doesn't throw exception if item is not foudn

print("set: ", set1)

set1.update(set(range(750, 900, 50)))
print("set: ", set1)

set2={600,745,824,580}
# All Operations:

set2_union = set1.union(set2)
print("set2_union: ", set2_union)
# set2_union:  {640, 800, 580, 520, 680, 745, 620, 750, 560, 850, 824, 500, 660, 600, 540}
set3_diff = set1.difference(set2)
print("set3_diff: ", set3_diff)
# set3_diff:  {640, 800, 520, 680, 620, 750, 560, 850, 500, 660, 540}
set4_common = set1.intersection(set2)
print("set4_common: ", set4_common)
# set4_common:  {600, 580}

set4_common.add(1000)
print("set4_common: ", set4_common)
set4_common.remove(1000)
print("set4_common: ", set4_common)
set4_common.discard(1000)
print("set4_common: ", set4_common)
set4_common.pop()
print("set4_common: ", set4_common)