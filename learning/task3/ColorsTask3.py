# Create a list called colors with repeated elements 'red', 'blue', 'red', 'green', 'red'.
# Print the number of occurrences of 'red' in the list. Remove all occurrences of 'red'
# from the list. Print the updated list.

lst =  ['red', 'blue', 'red', 'green', 'red']
print("lst: ", lst)
red_count = lst.count('red')
print("red_count: ", red_count)
for item in lst:
    if item == 'red':
        lst.remove(item)

print("lst: ", lst)
# lst:  ['blue', 'green']

