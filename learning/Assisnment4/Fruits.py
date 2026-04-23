# Write a Python program that defines a dictionary containing the names of fruits as keys and
# their corresponding colors as values (e.g., 'apple': 'red').
# Do at least 5 dictionary methods on it.

fruits =["banana", "apple", "orange", "dragon", "grapes"]
colors = ["yellow","red", "orange", "pink", "black"]

fruits_dict = {}
for i, fruit in enumerate(fruits):
    fruits_dict[fruit] = colors[i]
print(fruits_dict)

fruits_dict.pop("orange")
fruits_dict.popitem()
print(fruits_dict.values())
print(fruits_dict.keys())
fruits_dict.get("banana")
fruits_dict["pineapple"]="yellow"
fruits_dict.update({"cherry":"red"})
print(fruits_dict)

l = [None] * 10
print(len(l))

l1 = [1,2,4,5,4]
print(l1[:-1])