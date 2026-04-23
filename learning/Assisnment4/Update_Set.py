# Update the first set with items that don't exist in the second set.
# s1={150,200,400}
# s2={200,750,650}
# Expected output: s1={150,400}

s1={150,200,400}
s2={200,750,650}

s1.difference_update(s2)
print(s1)