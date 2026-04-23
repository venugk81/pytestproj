# Create a list called groceries with initial items: 'bread', 'milk', 'eggs', 'butter'.
# Print the final list of groceries.
# Add 'cheese' to the end of the list. Remove 'milk' from the list.
# Insert 'yogurt' at index 1.

lst = ['bread', 'milk', 'eggs', 'butter']

print("lst: ", lst)
# lst:  ['bread', 'milk', 'eggs', 'butter']
lst.append('cheese')
print("lst: ", lst)
# lst:  ['bread', 'milk', 'eggs', 'butter', 'cheese']
lst.remove("milk")
lst.insert(1, "yogurt")
print("lst: ", lst)

# lst:  ['bread', 'yogurt', 'eggs', 'butter', 'cheese']