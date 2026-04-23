# 3. Write a function called "calculate_average" that takes a list of numbers as input and returns the average of those numbers.

def calculate_average(lst):
    return sum(lst) / len(lst)
print(calculate_average([1, 2, 3, 4, 5]))