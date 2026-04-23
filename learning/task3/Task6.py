# Now that you have a nested list from the above output.
# Write a program to extend it by adding a sublist ["h", "i", "j"] in such a way that output will look like the following list below.
# Expected Output :
# [10, 20, [300, 400, [5000, 6000, 7000,"h", "i", "j"], 500], 30, 40]

lst = [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
lst[2][2].extend(["h", "i", "j"])
print(lst)
# [10, 20, [300, 400, [5000, 6000, 7000, 'h', 'i', 'j'], 500], 30, 40]



