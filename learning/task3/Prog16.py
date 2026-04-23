# Create a dictionary with key-value pairs for a person's name and age.
# Add a new key-value pair "city" with the value "Delhi" to the person dictionary.
# Remove the key-value pair with the key "age" from the person dictionary.
# Sort the person's dictionary by its keys.


person = {
    "name": "Venu",
    "age": 18
}
print(person)
city = {
    "city": "Delhi"
}

person.update(city)
print(person)
person.pop("age")
print(person)

sorted_person = dict(sorted(person.items()))
print(sorted_person)

print(type(sorted(person.items()))) #<class 'list'>
print(sorted(person.items()))   #[('city', 'Delhi'), ('name', 'Venu')]