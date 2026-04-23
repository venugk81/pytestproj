# Create a list called fruits with elements 'apple', 'banana', 'orange', 'mango', and 'kiwi'.
# Create a new list by slicing fruits to include only the citrus fruits ('orange' and 'mango").
# * Create a new list called tropical by slicing fruits to include only the tropical fruits ('banana" and "kiwi').
# Concatenate citrus and tropical lists to create a new list called combined. Print combined.

lst = ['apple', 'banana', 'orange', 'mango', 'kiwi']
print('All Fruits: ', lst)
print(lst)
citrus_fruits = lst[2:4]
print("citrus_fruits: ", citrus_fruits)
tropical_fruits = [lst[1], lst[4]]
print("tropical_fruits: ", tropical_fruits)

combined_fruits = citrus_fruits + tropical_fruits
print("combined_fruits: ", combined_fruits)

